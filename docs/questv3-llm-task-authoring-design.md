# QuestV3（任务）现状梳理 + LLM/Agent 建任务能力设计

> 状态：设计草案（未实现），先梳理 metopia 的 questV3 现状，再给出用 LLM/Agent 自动创建任务的接口设计。
> 关联文档：`metopia-service` 仓库外的 `/home/ubuntu/campaign-task-unification-plan.md`（campaign/task 三系统统一化总计划）。

## 1. 背景

Metopia 正在把 raffle / questV1 / questV2(academyV1) 三套旧系统合并成统一的 **quest_v3**（对外概念叫 "Task"）。
一个 **Campaign** 是容器，1:N 包含 Task / Academy / Credential；quest_v3 表通过 `campaign_id` 归属到某个 campaign。

现状：Task 只能通过 `/build/campaign` 里的表单向导手工创建，向导目前只暴露了 3 种任务类型（Farcaster/X 转发、人工审核），后端模型其实支持更多类型（quiz、投票、表单、链上 criteria 等）但没有 UI 入口。这是本设计要解决的缺口——用 LLM 或 agent，从一句自然语言描述直接生成一个可用的 Task 草稿，覆盖手工表单没暴露的能力。

## 2. 现状：QuestV3 数据结构

### 2.1 `quest_v3` 表（`src/models/v3/questV3.ts`）

| 字段 | 类型 | 说明 |
|---|---|---|
| `slug` | string, unique | URL 标识 |
| `title` / `body` / `cover` | string / JSON / string | 基本信息 |
| `start` / `end` | bigint (unix seconds) | 起止时间 |
| `project_id` / `campaign_id` | int | 归属的 project / campaign |
| `eligibilities` | `UnifiedEligibility[]` | 参与门槛（进入 Task 前的资格校验，raffle 模式下才用这个） |
| `tasks` | `UnifiedEligibility[]` | 需要完成的步骤（quest/filtered 模式下用这个） |
| `rewards` | `TypeReward[]`（含 multiplier） | 奖励配置 |
| `pass_address` / `pass_metadata` | string / JSON | referral/passcard 相关 |
| `display_mode` | enum `general_star` \| `academy_v1` | 前端展示壳 |
| `reward_mode` | enum `instant` \| `filtered` \| `raffle` | 完成即发 / 结束后人工筛选 / VRF 抽奖 |
| `task_flow` | enum `single` \| `sequential` \| `any_order` | 单任务 / 顺序步骤 / 任意顺序 |
| `raffle_config` | JSON | `{ poolId, poolParams, seed, onchain_id }` |
| `steps` | JSON | academy_v1 展示模式的分步内容块 |
| `category` / `difficulty` / `is_private` | — | 分类、难度、是否私有 |

关键点：`eligibilities` 和 `tasks` 是同一个类型（`UnifiedEligibility`），只是用途不同——raffle 模式把资格条件放 `eligibilities`（不需要"完成步骤"，达标即可参与抽奖）；quest/filtered 模式把要做的步骤放 `tasks`。

### 2.2 `UnifiedEligibility`（`src/models/v3/unifiedEligibility.ts`）

两种模式二选一：

- **Mode A：`calculatorChain`**（老 raffle/questV1 风格）：`{ entry?, threshold?, params: [{ type, ... }] }`，走已有的 Calculator 链（`DefaultValidator`）。
- **Mode B：`taskType`**（questV2/academy 风格结构化任务），目前支持的 `StructuredTaskType`：

  | taskType | 说明 | 校验方式 |
  |---|---|---|
  | `text` / `link` / `twitter` / `discord` | 无校验，提交即通过 | 直接 pass |
  | `vote-s` / `vote-m` | 单选/多选投票 | 只检查有提交、选项数不超限 |
  | `quiz-s` / `quiz-m` | 单/多答案测验 | `answers` 比对（走 `INTERNAL_CALCULATOR_TYPE_QUIZ`） |
  | `form` | 表单字段 | 逐字段比对（走 `INTERNAL_CALCULATOR_TYPE_FORM`） |
  | `criteria` | 外部链上/风控条件（data.metopia.xyz） | `TYPE_ADAPTER` calculator，`criteriaSlug` + `params` |
  | `criteria-f` | 同上，但走 Farcaster custody address | `INTERNAL_CALCULATOR_TYPE_CRITERIA_FARCASTER` |
  | `referral` | campaign referral passcard mint 数 | `INTERNAL_CALCULATOR_TYPE_CAMPAIGN_REFERRAL` |
  | `manual-review` | 用户提交材料，人工审核 | 不自动判定，`reason: 'pending_review'`，走 `reviewQuestSubmission` |

### 2.3 Reward 结构

`rewards: TypeReward[]`，每项含 multiplier 字段；实际编辑时字段是 `{ type: 'erc20' | 'other', network, tokenAddress, amount, supply }`（见 `CampaignForm` 里 `ERC20RewardsSetter`）。`reward_mode` 决定发放方式：`instant`（完成即发）/ `filtered`（结束后管理员挑选 `distributeRewards`）/ `raffle`（`drawWinners` 走 VRF）。

## 3. 现状：API 一览（`/api/v3/quest`，`questV3Router.ts`）

| Method & Path | 用途 | 鉴权 |
|---|---|---|
| `GET /` | 列表（project_id/campaign_id/display_mode/reward_mode 过滤） | 否 |
| `GET /:slug` | 详情 + 参与状态 | 否 |
| `GET /:questId/participants` | 已完成参与者列表 | 否 |
| `POST /create` | 从 build 向导创建 | 是 |
| `POST /check-eligibility` | 校验资格（不改状态） | 否 |
| `POST /validate` | 校验并持久化某一步 | 否 |
| `POST /claim` | 领取奖励（instant） | 否 |
| `POST /join` | 加入抽奖 | 否 |
| `POST /draw` | 开奖（admin） | 否 |
| `POST /distribute` | 发放奖励（filtered，admin） | 否 |
| `GET /review/pending` | 人工审核列表（admin） | 是 |
| `POST /review` | 审核通过/拒绝（admin） | 是 |

> 注：目前多数写操作接口没挂 `auth` 中间件（`create`/`review*` 除外），这是现状记录，不在本次设计范围内评估。

## 4. 现状：创建流程与局限（`createQuestFromBuildWizard`）

- 入参极简：`project{title,description,cover,pool_address}` + `campaign{title,body,cover,start,end,type,rewards,eligibilities.filters}`。
- `mapBuildWizardFilterToUnified()` 把向导里的 filter 映射成 `UnifiedEligibility`，但**只识别 3 种**：
  - `calculatorParams[0].slug` 存在 → `taskType: 'criteria'`
  - `actionType === 'farcaster_repost' | 'x_repost'` → `taskType: 'link'`（**无实际校验**，只是留痕）
  - `actionType === 'manual_review'` → `taskType: 'manual-review'`
  - 其他一律 fallback 成 `taskType: 'text'`（无校验）
- 也就是说：`quiz-s/m`、`form`、`vote-s/m`、`criteria-f`、`referral` 这些后端已经支持校验的类型，**手工表单完全没有入口去配置**——这正是 LLM/agent 建任务能力要补的缺口：不建新的校验能力，而是把已有能力通过自然语言描述"解锁"出来。

## 5. 统一化计划进度（摘要）

来自 `campaign-task-unification-plan.md`（2026-07-13 状态）：

- Phase 1（Calculator 扩展）～Phase 7（前端改造）：均标记【未开始】，只有零散子项完成（如聚合首页 6.1-6.4、Academy 板块 7.1/7.3）。
- Phase 8（数据迁移）🚧 进行中：8.1 quest_v2→quest_v3 迁移 371/371 全部成功；8.2 academy→quest_v3 脚本未写（327 条未迁）；8.4 下线旧端点未做。
- 结论：quest_v3 目前是"新表 + 部分迁移数据 + 简化版创建向导"共存的过渡态，Calculator 体系尚未按计划统一，本设计中的 LLM 能力应基于**当前已跑通的校验类型**（text/link/manual-review/criteria/quiz/form/vote/referral 均已有 Calculator 实现，只是 UI 未开放），不要等 Phase 1-7 完成再做。

## 6. 目标：LLM/Agent 建任务能力

### 6.1 目标 / 非目标

**目标**：给定一段自然语言描述（如"帮我建一个任务，转发这条推文 + 做一个 3 题测验，奖励每人 10 USDC，7 天后结束"），由 LLM/agent 生成一份符合 `QuestV3` schema 的**草稿 JSON**，经校验和人工确认后落库为真实 Task。

**非目标**：
- 不改变现有校验逻辑（Calculator 体系保持不变）。
- 不允许 LLM 绕过校验直接写库——LLM 只产出"草稿"，最终落库前必须走和手工创建一样的 schema 校验 + 人工确认步骤。
- 不在本阶段处理 raffle 的链上 VRF 配置（`raffle_config`），先覆盖 `instant` / `filtered` 两种更结构化、更容易生成的模式。

### 6.2 整体流程

```
自然语言描述
    │
    ▼
① LLM 草稿生成（agent 可多轮追问缺失信息：奖励代币/网络/数量、结束时间等）
    │  输出：符合 QuestV3CreateDraft schema 的 JSON + 未决问题列表
    ▼
② 服务端 schema 校验（zod/类型守卫）
    │  - 结构不对 → 打回 LLM 重试（带错误信息）一次
    │  - 引用了不存在的 taskType / calculatorSlug → 拒绝该字段，fallback 为 text 并在草稿里标红提示人工确认
    ▼
③ 草稿预览（返回给调用方 / 前端），人工可编辑
    │
    ▼
④ 确认创建：复用现有 createQuestFromBuildWizard 的落库路径（或其扩展版本）
```

草稿阶段**不写库**，只有第 ④ 步才创建 `QuestV3Model` 记录——这样即使 LLM 生成质量不稳定，也不会污染数据。

### 6.3 新增接口设计（建议落在 `metopia-service`，见 6.6）

```
POST /api/v3/quest/ai-draft
Auth: 是（owner 必须已登录）
Request:
{
  "prompt": "帮我建一个任务，转发这条推文 https://x.com/... ，
             再回答一个单选题：Metopia 主网在哪条链？选项 Base/Ethereum/Polygon，
             正确答案 Base。奖励每人 5 USDC（Base 链），7 天后结束。",
  "context"?: {
    "project_id"?: number,
    "campaign_id"?: number,
    "conversationId"?: string   // 多轮追问时用于延续上下文
  }
}

Response 200:
{
  "draft": {
    "title": "转发推文 + 答题任务",
    "body": "...",
    "start": "2026-07-13T00:00:00",
    "end": "2026-07-20T00:00:00",
    "type": "quest",                 // quest | raffle | filtered
    "tasks": [
      { "title": "转发指定推文", "taskType": "link" },
      { "title": "选择 Metopia 主网所在的链", "taskType": "quiz-s",
        "answers": [[0]], "options": [["Base","Ethereum","Polygon"]] }
    ],
    "rewards": [{ "type": "erc20", "network": "base", "tokenAddress": "...", "amount": "5", "supply": null }]
  },
  "warnings": [
    "未识别到 USDC 在 Base 链上的合约地址，请手动填写 tokenAddress"
  ],
  "clarifyingQuestions": [
    "这个任务的奖励总名额（supply）是多少？"
  ]
}
```

```
POST /api/v3/quest/ai-create
Auth: 是
Request:
{
  "draft": { ...同上，允许人工改过的版本... },
  "project": { ... },     // 同 createQuestFromBuildWizard 的 project 参数
  "campaign": { ... }     // 同上；draft 内容 merge 进 campaign 参数
}
Response 200:
{ "quest": { ...QuestV3 落库后的完整记录... } }
```

`ai-create` 内部直接调用现有的 `createQuestFromBuildWizard(owner, project, campaign)`，**不新建一套落库逻辑**——LLM 只负责把自然语言"翻译"成 `createQuestFromBuildWizard` 已经认识的 `campaign.eligibilities.filters` 结构（或者直接扩展该函数支持接收已经是 `UnifiedEligibility[]` 形式的 `tasks`/`eligibilities`，跳过 `mapBuildWizardFilterToUnified` 的有限映射）。

> 建议：给 `createQuestFromBuildWizard` 加一个可选参数 `rawEligibilities?: UnifiedEligibility[]`，当存在时跳过 `mapBuildWizardFilterToUnified`直接使用——这样 LLM 生成的 quiz/form/vote 等类型不会被现有的"只认 3 种 actionType"的映射函数打回 `text`。这是本设计里唯一必须动 `metopia-service` 现有代码的地方。

### 6.4 Prompt / Schema 约束策略

- **不要让 LLM 自由发挥 JSON 结构**：system prompt 里内嵌 `UnifiedEligibility` 的 TypeScript 类型定义 + 每种 `taskType` 的 1-2 个示例（few-shot），明确列出允许的 `taskType` 枚举值，禁止生成枚举外的值。
- **强制走一次服务端 schema 校验**（用 zod 定义 `QuestV3CreateDraft`），校验失败时把具体错误（哪个字段、期望类型）喂回给 LLM 重试，最多重试 1-2 次，超过则该字段整体 fallback 为 `taskType: 'text'` 并加入 `warnings`。
- **`criteria` / `criteria-f` 类型不允许 LLM 直接编造 `criteriaSlug`**：这类 slug 对应链上/风控的具体 adapter，必须从已注册的 slug 白名单里选，不在白名单里则整条 fallback 为 `manual-review`（更保守，需人工审核）并提示。
- **奖励代币地址**：不允许 LLM 凭记忆编造 `tokenAddress`，只能从项目已配置的代币列表中选，或留空并加入 `clarifyingQuestions` 要求人工补充——避免地址填错导致资产损失。
- **草稿必须过一遍和运行时一致的校验函数**：`validateUnifiedEligibility` 本身是"校验用户提交"的函数，不直接复用；但其类型定义（`UnifiedEligibility`、`StructuredTaskType`）就是草稿 schema 的唯一真实来源（single source of truth），避免另建一套并慢慢和后端类型定义漂移。

### 6.5 校验与兜底策略小结

| 情况 | 处理 |
|---|---|
| LLM 输出的 JSON 结构损坏（parse 失败） | 重试一次，仍失败则整体拒绝，返回错误给调用方 |
| `taskType` 不在枚举内 | 该 task 项 fallback 为 `text`，加入 warnings |
| `criteriaSlug` 不在白名单 | fallback 为 `manual-review`，加入 warnings |
| 缺关键字段（奖励代币/数量/结束时间） | 不 fallback，加入 `clarifyingQuestions`，要求人工/多轮追问补全后才允许调用 `ai-create` |
| 一切正常 | 直接进入草稿预览，等待人工确认调用 `ai-create` |

### 6.6 落地位置建议

本设计描述的能力（LLM 生成 Task 草稿）**逻辑上属于 `metopia-service`**，因为：
1. 它要落库到 `quest_v3` 表，依赖 `metopia-service` 里的 `QuestV3Model` / `UnifiedEligibility` / Calculator 白名单等，这些不适合脱离该仓库单独存在。
2. `ai-draft` / `ai-create` 应该挂在 `/api/v3/quest` 下，和现有 `create` 接口同源鉴权（`auth` 中间件、owner 归属校验）。

这份文档目前存放在 `focus-mind` 仓库仅作为设计草案的记录位置；正式实现落地时需要在 `metopia-service` 建对应的 router/service 改动（本文档第 6.3 节的接口）。

## 7. 开放问题 / 待确认

1. `ai-draft` 用哪个 LLM/API？
2. `criteria` / `criteria-f` 的 slug 白名单从哪里读取？是否已有现成的 adapter 注册表可以直接查询，还是需要新建一张"可用 criteria 列表"给 LLM 做 grounding？
3. `ai-create` 是否需要限流/审计日志（防止恶意 prompt 批量建垃圾任务）？现有 `create` 接口本身也没有限流，是否要一并补上？
4. raffle 模式（VRF `raffle_config`）要不要纳入第一版范围，还是像本文档 6.1 里说的先跳过？
