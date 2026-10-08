# short-drama-maker

> 一个把"做 AI 短剧"从一团模糊，拆成**可复用流水线**的 WorkBuddy 技能包。
> 覆盖从创意立项到剪辑成片的所有中间环节，内置质量门与"资产护照"一致性机制。

[English below](#english)

---

## 它能帮你什么

你是不是也这样：收藏了一堆 AI 视频工具，真要做短剧时还是不知道从哪下手——写剧本的、拆分镜的、生视频的、剪辑的，各管一段，中间全靠手动接。

这个技能包就是把这套流程**装进 WorkBuddy**，让它按阶段帮你把脑子里的想法一路推到成片。

### 全流程六阶段（含全部中间环节）

| 阶段 | 干什么 | 关键产出 |
|---|---|---|
| 0 创意立项 | 用爆款 7 规则框方向 | `00_concept.md` 概念卡 |
| 1 剧本开发 | 大纲→角色→美术→剧本 | `01~04` 四份文档 + 14 道剧本质量门 |
| 2 分镜拆解 | 场景→参考板→**资产护照**→镜头卡 | `05~08` + 压力测试 |
| 3 美术素材 | ImageGen 出角色/场景/道具图 | `assets/` |
| 4 视频生成 | VideoGen 逐镜头图生视频 + 续帧 | `video/` |
| 5 剪辑成片 | 字幕/配音/配乐/特效/导出 | `edit/` 成片 |
| 6 配套图表（可选） | 路演/PPT 高级配图 | SVG/HTML |

### 核心机制：资产护照（一致性命门）

长片最怕角色的脸、衣服、年龄在相邻镜头漂移。本技能要求为每个角色/场景写一段**锁定不变的视觉描述（资产护照）**，生成每一个镜头时**逐字复制**进提示词——变化只改动作/机位，不改护照。靠纪律，不靠运气。

### 质量门

9 道质量门（Q0–Q5）分布在各阶段末尾，不达标不许进下一环，避免下游返工。

---

## 安装

### 方式一：git clone（推荐）

```bash
git clone https://github.com/sunchaosz/short-drama-maker.git ~/.workbuddy/skills/short-drama-maker
```

重启 WorkBuddy 后即可在对话中触发。

### 方式二：下载 ZIP

在仓库页面点 **Code → Download ZIP**，解压后把 `short-drama-maker` 文件夹整体复制到：

```
~/.workbuddy/skills/short-drama-maker/
```

（`~` 在 Windows 上为 `C:\Users\你的用户名\.workbuddy`）

---

## 使用

### 1. 直接对话触发

新会话里说："帮我做一个关于 XX 的短剧"，WorkBuddy 会按技能描述自动匹配并启动流程；
或在任意会话显式调用：

```
@skill:short-drama-maker 帮我做一个"负债逆袭"都市短剧
```

### 2. 先用脚手架搭项目目录

```bash
python ~/.workbuddy/skills/short-drama-maker/scripts/init_project.py 我的短剧 D:\短剧项目
```

会生成 `00_concept.md`～`08_shot_prompts.md` 和 `assets/ video/ edit/` 目录。

### 3. 按流水线推进

技能会带你走完六阶段，每阶段产出文件并过质量门。建议先用 1 集走通 0→5 验证风格，再批量量产。

---

## 工具映射

| 环节 | WorkBuddy 内置 | 外部替代（需自备） |
|---|---|---|
| 美术/素材图 | `ImageGen` | GPT-Image-2、Seedream、Nano Banana Pro、即梦 |
| 视频生成 | `VideoGen` | Seedance 2.0、Kling、Veo 3.1、即梦 CLI |
| 剪辑成片 | 手动 / 剪映专业版 | jianying-editor-skill |
| 配套图表 | 内置可视化 | diagram-design |

> 投外部模型时，按对应语法改写镜头提示词，但**资产护照片段保持原样**。

---

## 文件结构

```
short-drama-maker/
├── SKILL.md                  # 流程调度主文件（六阶段 + 质量门）
├── README.md                 # 本文件
├── references/
│   └── prompt-library.md     # 全部提示词模板 / 质量门清单 / 分镜模板
└── scripts/
    └── init_project.py       # 一键生成标准项目目录与空白模板
```

---

## 许可

MIT —— 随便用、随便改、随便二传，留个署名就好。

---

# English

A WorkBuddy Skill that turns "making an AI short drama" into a reusable pipeline — from concept to finished video, with quality gates and an **Asset Passport** consistency mechanism.

**Install:** `git clone <repo-url> ~/.workbuddy/skills/short-drama-maker`, then restart WorkBuddy.

**Use:** say "make me a short drama about X" or call `@skill:short-drama-maker`.

**Pipeline:** Concept → Script → Storyboard (with Asset Passport) → Art Assets (ImageGen) → Video (VideoGen) → Editing.

See `SKILL.md` and `references/prompt-library.md` for the full workflow and prompt templates.
