#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
short-drama-maker · 项目脚手架
用法: python init_project.py <项目名> [输出根目录，默认当前目录]
生成标准短剧项目目录与阶段空白模板，配合 SKILL.md 流水线使用。
"""
import os
import sys

# 阶段模板文件：(相对路径, 内容)
TEMPLATES = {
    "00_concept.md": "# 短剧概念卡：{{标题}}\n- 题材：\n- 核心钩子（前三秒）：\n- 目标受众：\n- 主角：\n- 第一幕最大冲突：\n- 情绪曲线：\n- 差异化点：\n- 建议集数 / 单集时长：\n",
    "01_outline.md": "# 大纲：{{标题}}（共 N 集，单集 秒）\n## 第一幕 钩子幕\n## 第二幕 冲突升级幕\n## 第三幕 反转/危机幕\n## 第四幕 高潮/收束幕\n",
    "02_characters.md": "## 角色：{{姓名}}\n- 年龄/性别：\n- 外貌（用于资产护照）：\n- 性格：\n- 动机（想要什么）：\n- 阻碍（被什么阻止）：\n- 弧光：\n- 口头禅：\n- 人物关系：\n",
    "03_art.md": "# 美术设定：{{标题}}\n- 画风：\n- 主色调：\n- 年代/世界观：\n- 质感关键词（全剧共用）：\n- 禁忌：\n",
    "04_script.md": "# 剧本：{{标题}} 第 n 集\n| 场号 | 场景 | 人物 | 动作 | 台词 | 时长 |\n|----|----|----|----|----|----|\n| 1 |  |  |  |  |  |\n- 本集钩子（结尾悬念）：\n",
    "05_breakdown.md": "| 镜头号 | 场次 | 景别 | 机位 | 运镜 | 时长 | 关联角色 |\n|------|----|----|----|----|----|------|\n| S1-01 |  |  |  |  |  |  |\n",
    "06_reference_board.md": "# 参考板\n- 角色定妆：\n- 关键场景气氛：\n- 道具：\n",
    "07_asset_passport.md": "## 护照：{{角色名}}\n[锁定描述，逐字复制进每个镜头提示词]\n\n## 护照：{{场景名}}\n[锁定描述]\n",
    "08_shot_prompts.md": "## S1-01\n- 画面：[护照片段]+\n- 运镜：\n- 声音：\n- 时长：\n- 模型提示词：\n",
}

SUBDIRS = ["assets/characters", "assets/scenes", "assets/props", "video", "edit"]


def init_project(name, root):
    base = os.path.join(root, name)
    os.makedirs(base, exist_ok=True)
    for d in SUBDIRS:
        os.makedirs(os.path.join(base, d), exist_ok=True)
    for fname, content in TEMPLATES.items():
        path = os.path.join(base, fname)
        if not os.path.exists(path):
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)
    # 资产护照速查说明
    readme = os.path.join(base, "README.md")
    if not os.path.exists(readme):
        with open(readme, "w", encoding="utf-8") as f:
            f.write(
                "# 短剧项目：%s\n\n阶段文件：00→08 按 SKILL.md 流水线依次填写。\n"
                "一致性铁律：07_asset_passport.md 的描述须逐字复制进每个镜头提示词。\n"
                "素材图放 assets/，视频放 video/，成片放 edit/。\n" % name
            )
    print("✅ 已生成项目目录：%s" % base)
    for f in sorted(TEMPLATES):
        print("   - %s" % f)
    for d in SUBDIRS:
        print("   - %s/ (目录)" % d)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python init_project.py <项目名> [输出根目录]")
        sys.exit(1)
    name = sys.argv[1]
    root = sys.argv[2] if len(sys.argv) > 2 else os.getcwd()
    init_project(name, root)
