# lwg-haibao-design

WorkBuddy 技能。设计"海报风格"的演讲/展示类单页 HTML，并基于用户投喂的图文设计图沉淀可复用配色与构图规则。使用时机：(1) 用户投喂一张或多张图文设计参考图，要求分析配色、构图、字体、装饰并沉淀为可复用设计规则；(2) 用户给出需求（主题内容、情绪调性、指定页面比例），要求生成海报风格演讲页、金句页、观点页、图文排版页等单页 HTML，比例为任意值（16:9、9:16、4:3、1:1、自定义等）。生成 HTML 以本技能自带的 baseline.md 与 checklist.md 为准；环境若装有 html skill 可额外读取其设计规范。

## 安装到 WorkBuddy

本仓库以「一个仓库 = 一个技能」组织，根目录即技能本体（`SKILL.md` + 可选 `references/` `scripts/`），没有同名嵌套层。

**方式 A｜上传技能包**：把本仓库目录打包成 zip（zip 内以含 `SKILL.md` 的目录为根），在 WorkBuddy 走「专家·技能·连接器 → 技能 → 添加技能 → 上传技能」导入。
> GitHub 的 "Download ZIP" 会自动加一层 `lwg-haibao-design-main/`，请以真正含 `SKILL.md` 的那一层为准。

**方式 B｜本机直接复制**：把仓库目录复制到 `~/.workbuddy/skills/lwg-haibao-design/`（用户级，所有项目可用）。

## 适配状态

已适配 WorkBuddy：`html` skill 为可选增强依赖，未安装时按技能自带的 `references/baseline.md` 与 `references/checklist.md` 出稿与验收；旧平台的硬编码路径已移除，安装路径为 `~/.workbuddy/skills/lwg-haibao-design/`。

## 说明

- GitHub 更新后，WorkBuddy 中已安装的技能不会自动刷新，需要重新导入一次。
- 本地母版（全量备份 + 打包源）另存于 `~/workbuddy-skills`。
