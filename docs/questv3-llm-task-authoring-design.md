# QuestV3（任务）Model 字段与 Create 接口说明

> 用途：供外部系统（用 LLM/Agent 自动生成任务）对接参考。LLM/Agent 部分由外部实现，本仓库不负责；这里只把 metopia-service 现有的 **quest_v3 数据模型**和 **创建接口** 讲清楚，外部系统按此拼装请求即可。
> 关联文档：`metopia-service` 仓库外的 `/home/ubuntu/campaign-task-unification-plan.md`（campaign/task 三系统统一化总计划）。

## 1. 背景

Metopia 正在把 raffle / questV1 / questV2(academyV1) 三套旧系统合并成统一的 **quest_v3**（对外概念叫 "Task"）。
一个 **Campaign** 是容器，1:N 包含 Task / Academy / Credential；quest_v3 表通过 `campaign_id` 归属到某个 campaign。

现状：Task 目前只能通过 `/build/campaign` 表单向导手工创建，向导只暴露了 3 种任务类型（Farcaster/X 转发、人工审核）。后端模型其实支持更多类型（quiz、投票、表单、链上 criteria 等），但没有 UI 入口——外部系统如果直接对接下面的 model/接口，是可以拿到比手工向导更丰富的能力的，但要注意第 4 节里"当前 create 接口的映射限制"。

## 2. Model 字段：`quest_v3` 表

来源：`metopia-service/src/models/v3/questV3.ts`

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `slug` | string, unique | 自动生成 | 由 `title` 生成唯一 URL 标识，不用手动传 |
| `title` | string(500) | 是 | 任务标题 |
| `body` | JSON（实际存字符串/富文本） | 否 | 任务描述 |
| `cover` | string(500) | 否 | 封面图 URL，建议 2:1 比例 |
| `start` / `end` | bigint (unix seconds) | 是 | 起止时间，接口层传 ISO 字符串，内部会转成 unix 秒 |
| `project_id` | int | 自动关联 | 由 `owner` 对应的 `ProjectCollection` 决定，没有则自动创建 |
| `campaign_id` | int | 否 | 归属的 campaign，可为空（当前 `create` 接口暂未接收这个参数，见第 4 节） |
| `eligibilities` | `UnifiedEligibility[]` | 否，默认 `[]` | **进入门槛**：raffle 模式下才写这里（达标即可参与抽奖，不需要"完成步骤"） |
| `tasks` | `UnifiedEligibility[]` | 否，默认 `[]` | **要完成的步骤**：quest/filtered 模式下写这里 |
| `rewards` | `TypeReward[]` | 否，默认 `[]` | 奖励配置，见第 3 节 |
| `pass_address` / `pass_metadata` | string / JSON | 否 | referral/passcard 相关，`create` 接口暂不接收 |
| `participant_count` | int | 自动 | 参与人数，只读 |
| `display_mode` | enum `general_star` \| `academy_v1` | 自动 | 前端展示壳；`create` 接口固定写 `general_star` |
| `reward_mode` | enum `instant` \| `filtered` \| `raffle` | 由 `campaign.type` 推导 | `instant`=完成即领奖，`filtered`=活动结束后管理员筛选发放，`raffle`=VRF 抽奖 |
| `task_flow` | enum `single` \| `sequential` \| `any_order` | 自动 | `create` 接口规则：`tasks.length > 1` → `any_order`，否则 `single`（目前没有生成 `sequential` 的路径） |
| `raffle_config` | JSON `{ poolId, poolParams, seed, onchain_id }` | 否 | 仅 raffle 模式用，`create` 接口暂不接收，需另外调用 raffle 相关流程补 |
| `steps` | JSON | 否 | 仅 `academy_v1` 展示模式用的分步内容块，`create` 接口不产出 |
| `category` | JSON | 否 | 分类标签 |
| `difficulty` | int | 否 | 难度 |
| `is_private` | boolean | 自动 | `create` 接口固定写 `false` |

**关键点**：`eligibilities` 和 `tasks` 是同一个类型（`UnifiedEligibility`），只是用途不同——不要把两者混淆着填。

## 3. Model 字段：`UnifiedEligibility`（`eligibilities[]` / `tasks[]` 里的每一项）

来源：`metopia-service/src/models/v3/unifiedEligibility.ts`

```ts
interface UnifiedEligibility {
  title: string;

  // Mode A：calculatorChain（老 raffle/questV1 风格，走已有 Calculator 链）
  calculatorChain?: {
    entry?: number;       // raffle 抽奖权重（负数=按 value 计算）
    threshold?: number;
    params: { type: number; [key: string]: any }[];
  };

  // Mode B：taskType（结构化任务类型，二选一，不要同时给 calculatorChain 和 taskType）
  taskType?: StructuredTaskType;
  answers?: number[][] | { [key: string]: string }[][]; // quiz-s/m、form 用
  options?: number[][];         // vote-m 用：每题可选项数上限
  criteriaSlug?: string;        // criteria / criteria-f 用
  threshold?: number;           // criteria / referral 用
  passAddress?: string;         // referral 用（不传则取任务的 pass_address）
  params?: Record<string, any>; // criteria / criteria-f 透传给 adapter 的额外参数
  formFields?: { name: string; label: string; type: 'text' | 'textarea' | 'image' }[]; // manual-review 用
}
```

`StructuredTaskType` 枚举与每种类型必须/可选带的字段：

| taskType | 必须字段 | 可选字段 | 说明 / 校验方式 |
|---|---|---|---|
| `text` | — | — | 无校验，提交即通过 |
| `link` | — | — | 无校验，提交即通过（用于"转发/关注"类留痕，不验证真实性） |
| `twitter` | — | — | 同上 |
| `discord` | — | — | 同上 |
| `vote-s` | — | — | 单选投票，只检查有提交 |
| `vote-m` | — | `options` | 多选投票，检查选项数不超 `options` 长度 |
| `quiz-s` | `answers`（`number[][]`，如 `[[0]]` 表示第 0 题正确答案是选项 0） | — | 单答案测验，逐题比对 |
| `quiz-m` | `answers` | `options` | 多答案测验 |
| `form` | `answers`（此时是表单校验规则，格式见 `FormCalculator`） | — | 表单字段逐项比对 |
| `criteria` | `criteriaSlug` | `threshold`, `params` | 走 `data.metopia.xyz` 的外部 adapter，`criteriaSlug` **必须是已注册的 adapter slug**，不能编造 |
| `criteria-f` | `criteriaSlug` | `threshold`, `params` | 同上，但通过用户 Farcaster custody address 查询 |
| `referral` | — | `passAddress`, `threshold`（默认 1） | 校验 campaign referral passcard mint 数 |
| `manual-review` | `formFields`（至少 1 项） | — | 不自动判定，用户提交后状态为 `pending_review`，需人工在 `/review` 接口审核 |

**给外部系统的强约束**：
- `taskType` 只能是上表枚举值，不能生成表外的值（会被当前 mapping 兜底为 `text`，等于没校验，见第 4 节）。
- `criteriaSlug` 必须来自 metopia 已注册的 adapter 列表（目前没有对外暴露"可用 slug 列表"接口，这是一个待确认的开放问题，见第 6 节）。不确定时优先用 `manual-review`（人工审核兜底），不要瞎填。
- `tokenAddress`（见第 4 节 reward）同理，不能凭空编造，需来自项目已支持的代币列表或由人工确认。

## 4. Model 字段：`TypeReward`（`rewards[]` 里的每一项）

来源：`metopia-service/src/models/star/types.ts`

```ts
type TypeReward = {
  icon: string;
  type: 'nft' | 'erc20' | 'other' | 'xp';
  image: string;
  amount: number;
  supply: number;
  name: string;
  imageSize?: 'lg' | 'sm';
  network?: number;         // chainId，如 8453 = Base
  symbol?: string;
  decimal?: number;
  tokenAddress?: string;
  base_amount?: number;     // 应用 multiplier 前的原始 amount
  tier_power?: number;      // 用户 power 超过此值时应用 tier_multiplier
  tier_multiplier?: number;
  passcard_multiplier?: number; // 用户持有 passcard 时应用
  date_multiplier?: number;     // 在 date_limit 之前领取时应用
  date_limit?: string;
};
```

前端 `erc20` 类型奖励实际只用到 `{ type: 'erc20', icon, symbol, decimal, tokenAddress, network, amount, supply }` 这几个字段（`amount`/`supply` 前端是字符串，后端存 number，注意类型转换）。multiplier 相关字段（`tier_*`/`passcard_multiplier`/`date_*`）目前手工向导不产出，是给运营后台单独配置的，外部系统一般不需要填。

## 5. Create 接口：`POST /api/v3/quest/create`

来源：`questV3Router.ts` + `questV3Service.ts` 的 `createQuestFromBuildWizard`。

**鉴权**：需要 `auth` 中间件（登录态），`owner` 从鉴权上下文取（不是 body 里传的字段）。

### 请求体

```ts
{
  project?: {
    title?: string;
    description?: string;
    cover?: string;
    pool_address?: string;   // 若传入，会更新 Account.pool_address
  },
  campaign: {
    title: string;              // 必填，非空
    body?: string;
    cover?: string;
    start: string;              // 必填，ISO 日期字符串，如 "2026-07-13" 或 "2026-07-13T00:00:00"
    end: string;                // 必填，同上
    type: 'quest' | 'raffle' | 'filtered';  // 决定 reward_mode
    rewards?: TypeReward[];
    eligibilities?: {
      all?: number;
      filters?: any[];          // 见下方"filter 映射规则"
      params?: any[];
    }
  }
}
```

**owner 归属逻辑**：按 `owner` 查 `ProjectCollection`，没有则自动创建一个（用 `project.title`/`project.description`/`project.cover`，缺省 fallback 到 `campaign` 同名字段）。也就是说**同一个 owner 只有一个 project**，多次调用 `create` 不会重复建 project。

**quest/raffle/filtered 的区别**：
- `type: 'raffle'` → `unifiedFilters` 写入 `eligibilities`，`tasks` 为空数组，`reward_mode: 'raffle'`
- `type: 'filtered'` → `unifiedFilters` 写入 `tasks`，`eligibilities` 为空数组，`reward_mode: 'filtered'`（完成步骤后不自动发奖，需管理员另调 `/distribute`）
- `type: 'quest'`（其余情况）→ 同 filtered 把 filters 写入 `tasks`，`reward_mode: 'instant'`（完成即可 `/claim`）

### `campaign.eligibilities.filters` → `UnifiedEligibility` 的映射规则（**当前唯一识别 3 种，重要**）

`create` 接口内部用 `mapBuildWizardFilterToUnified()` 把每个 filter 转成 `UnifiedEligibility`，**只认这 3 种输入形状**，其余一律 fallback 成 `{ taskType: 'text' }`（无校验，等于形同虚设）：

1. **外部 criteria**：`filter.params.calculatorParams[0].slug` 存在时
   ```json
   { "title": "...", "params": { "calculatorParams": [{ "slug": "xxx", "threshold": 1, "其他字段": "..." }] } }
   ```
   → `{ title, taskType: 'criteria', criteriaSlug: 'xxx', threshold: params.threshold, params: {其他字段} }`

2. **Farcaster/X 转发**：`filter.params.actionType === 'farcaster_repost' | 'x_repost'`
   ```json
   { "title": "Repost this cast on Farcaster", "img": "iconfarcaster", "link": "https://warpcast.com/...", "params": { "actionType": "farcaster_repost", "castUrl": "https://warpcast.com/..." } }
   ```
   → `{ title, taskType: 'link' }`（**无实际校验**，只是留痕，用户提交即算完成）

3. **人工审核**：`filter.params.actionType === 'manual_review'`
   ```json
   {
     "title": "Submit proof of attendance",
     "content": "Submit proof of attendance",
     "params": {
       "actionType": "manual_review",
       "formFields": [{ "name": "field_1", "label": "Screenshot", "type": "image" }]
     }
   }
   ```
   → `{ title, taskType: 'manual-review', formFields: [...] }`

4. **其他任何形状** → `{ title, taskType: 'text' }`（fallback，无校验）

**⚠️ 给外部系统的重要提示**：如果需要生成 `quiz-s/m`、`form`、`vote-s/m`、`criteria-f`、`referral`、`calculatorChain` 这些更丰富的类型，**当前 `create` 接口的 filter 映射不支持**，传了也会被 fallback 成 `text`。如果外部系统需要这些类型，需要 metopia-service 一侧扩展 `createQuestFromBuildWizard`，支持直接接收 `UnifiedEligibility[]`（跳过 `mapBuildWizardFilterToUnified`），而不是继续套用向导的 filter 形状。这是一个需要 metopia-service 侧配合的改动，本文档先记录清楚现状，具体是否要改由 metopia-service 团队评估排期。

### 响应

```ts
{ "quest": QuestV3 }  // 完整的 quest_v3 落库记录（plain object）
```

### 报错情况

| 情况 | HTTP | message |
|---|---|---|
| 未登录 / 无 owner | 400 | `owner is required` |
| `campaign.title` 为空 | 400 | `Please enter a title` |
| `campaign.start` / `campaign.end` 缺失 | 400 | `Please select a start/end date` |

## 6. 开放问题 / 待确认（给外部系统对接前需要拿到答案）

1. `criteria` / `criteria-f` 的 `criteriaSlug` 白名单从哪里读取？是否有现成接口可以查询"当前可用的 criteria slug 列表"，供外部系统做 grounding、避免编造不存在的 slug？
2. `rewards[].tokenAddress` 的可选代币列表从哪里获取？（前端目前是写死在 `CampaignForm.tsx` 的 `supportedTokenList`，外部系统是否要接同一份数据源）
3. 是否需要扩展 `createQuestFromBuildWizard` 支持直接传 `UnifiedEligibility[]`（见第 5 节 ⚠️ 提示），让外部系统能用到 quiz/form/vote/criteria-f/referral 这些类型？如果不扩展，外部系统目前只能生成 `link` / `manual-review` / `criteria`（且 criteria 依赖问题 1）/ `text` 四种。
4. `campaign_id` 归属：`create` 接口目前不接收 `campaign_id`，新建的任务不挂在任何 campaign 下。外部系统如果需要任务归属到指定 campaign，也需要 metopia-service 一侧补上这个参数透传。
