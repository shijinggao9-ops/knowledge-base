#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Obsidian 游戏拆解知识库 - 快速创建文件脚本
用法: python create_obsidian_files.py [目标目录路径]
默认在当前目录下创建文件
"""

import os
import sys
from datetime import datetime

# ==================== 文件列表 ====================
FILES = [
    "90-2-1-1 拆解总索引_MOC.md",
    "90-2-1-2 底层驱动分类图谱.md",
    "90-2-1-3 拆解维度标准SOP.md",
    "90-2-1-4 【模板】单款游戏深度拆解卡片.md",
    "90-2-1-5 【模板】横向对比分析报告.md",
    "90-2-1-6 拆解数据速查表.md",
    "90-2-1-7 魔兽世界_数值与DPS模拟.md",
    "90-2-1-8 只狼_动作帧与拼刀手感.md",
    "90-2-1-9 英雄联盟_对线博弈与团战帧数.md",
    "90-2-1-10 赛博朋克2077_沉浸感与叙事欺骗.md",
    "90-2-1-11 EVE Online_完全体经济战争.md",
    "90-2-1-12 梦幻西游_回合制数值卡点.md",
    "90-2-1-13 三国志战略版_战损比与配将逻辑.md",
    "90-2-1-14 王者荣耀_技能前摇与走位博弈.md",
    "90-2-1-15 崩坏3_极限闪避与QTE触发机制.md",
    "90-2-1-16 原神_元素反应与开放世界引导.md",
    "90-2-1-17 重返未来1999_审美调性与英配沉浸.md",
    "90-2-1-18 逆水寒手游_智能NPC与MMO社交减负.md",
    "90-2-1-19 专题_付费心理学模型对比.md",
    "90-2-1-20 专题_DAU曲线与弃坑拐点分析.md",
    "90-2-1-21 专题_社交结构金字塔.md",
    "90-2-1-22 专题_赛季制与版本更新节奏研究.md",
]

# ==================== 模板内容生成器 ====================
def get_frontmatter(filename):
    """根据文件名生成基础 frontmatter"""
    name = filename.replace('.md', '')
    tags = []

    # 自动标签
    if '模板' in name:
        tags.append('模板')
    if '专题' in name:
        tags.append('专题')
    if 'MOC' in name or '索引' in name:
        tags.append('MOC')
        tags.append('索引')
    if 'SOP' in name:
        tags.append('SOP')
    if '图谱' in name:
        tags.append('图谱')
    if '速查' in name:
        tags.append('速查表')

    # 游戏标签
    games = ['魔兽世界', '只狼', '英雄联盟', '赛博朋克2077', 'EVE Online', 
             '梦幻西游', '三国志战略版', '王者荣耀', '崩坏3', '原神', 
             '重返未来1999', '逆水寒手游']
    for game in games:
        if game in name:
            tags.append(game)
            break

    tags_str = ', '.join([f'#{t}' for t in tags]) if tags else ''

    return f"""---
created: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
tags: {tags_str}
status: 待完善
---

# {name}

> 创建时间: {datetime.now().strftime('%Y-%m-%d')}

## 概述

（在此填写内容概要）

---

## 正文

（在此展开详细内容）

---

## 关联笔记

- 

## 参考来源

- 
"""


def get_moc_content():
    """MOC 索引文件的特殊内容"""
    links = []
    for f in FILES[1:]:  # 排除自己
        basename = f.replace('.md', '')
        links.append(f"- [[{basename}]]")

    return f"""---
created: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
tags: #MOC #索引
cssclass: moc
---

# 游戏拆解知识库总索引

> 本知识库编号规则: `90-2-1-X`
> - `90` 代表大类（游戏研究）
> - `2` 代表子类（拆解分析）
> - `1` 代表具体项目
> - `X` 为文件序号

---

## 📋 框架与标准

- [[90-2-1-2 底层驱动分类图谱]]
- [[90-2-1-3 拆解维度标准SOP]]
- [[90-2-1-6 拆解数据速查表]]

## 📝 模板

- [[90-2-1-4 【模板】单款游戏深度拆解卡片]]
- [[90-2-1-5 【模板】横向对比分析报告]]

## 🎮 单款游戏拆解

### 动作/ARPG
- [[90-2-1-8 只狼_动作帧与拼刀手感]]
- [[90-2-1-15 崩坏3_极限闪避与QTE触发机制]]
- [[90-2-1-16 原神_元素反应与开放世界引导]]

### MOBA
- [[90-2-1-9 英雄联盟_对线博弈与团战帧数]]
- [[90-2-1-14 王者荣耀_技能前摇与走位博弈]]

### MMO
- [[90-2-1-7 魔兽世界_数值与DPS模拟]]
- [[90-2-1-11 EVE Online_完全体经济战争]]
- [[90-2-1-18 逆水寒手游_智能NPC与MMO社交减负]]

### 回合制/策略
- [[90-2-1-12 梦幻西游_回合制数值卡点]]
- [[90-2-1-13 三国志战略版_战损比与配将逻辑]]

### 开放世界/叙事
- [[90-2-1-10 赛博朋克2077_沉浸感与叙事欺骗]]

### 二次元/风格化
- [[90-2-1-17 重返未来1999_审美调性与英配沉浸]]

## 🔬 专题研究

- [[90-2-1-19 专题_付费心理学模型对比]]
- [[90-2-1-20 专题_DAU曲线与弃坑拐点分析]]
- [[90-2-1-21 专题_社交结构金字塔]]
- [[90-2-1-22 专题_赛季制与版本更新节奏研究]]

---

## 全部文件列表

{chr(10).join(links)}
"""


def create_files(target_dir, overwrite=False):
    """创建所有文件"""
    created_count = 0
    skipped_count = 0

    print(f"\n📁 目标目录: {os.path.abspath(target_dir)}")
    print("=" * 50)

    for filename in FILES:
        filepath = os.path.join(target_dir, filename)

        # 检查文件是否已存在
        if os.path.exists(filepath) and not overwrite:
            print(f"⏭️  跳过（已存在）: {filename}")
            skipped_count += 1
            continue

        # 生成内容
        if "MOC" in filename or "索引" in filename:
            content = get_moc_content()
        else:
            content = get_frontmatter(filename)

        # 写入文件
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"✅ 创建成功: {filename}")
        created_count += 1

    print("=" * 50)
    print(f"\n📊 统计: 创建 {created_count} 个 | 跳过 {skipped_count} 个 | 总计 {len(FILES)} 个")

    if created_count > 0:
        print(f"\n💡 提示: 如需覆盖已存在文件，请添加 --overwrite 参数")


def main():
    # 解析参数
    target_dir = "."
    overwrite = False

    args = sys.argv[1:]

    for i, arg in enumerate(args):
        if arg in ('--overwrite', '-o'):
            overwrite = True
        elif arg in ('--help', '-h'):
            print(__doc__)
            print("\n参数:")
            print("  [路径]        指定 Obsidian 库根目录路径")
            print("  --overwrite   覆盖已存在的文件")
            print("  --help        显示帮助信息")
            print("\n示例:")
            print("  python create_obsidian_files.py")
            print("  python create_obsidian_files.py /path/to/vault")
            print("  python create_obsidian_files.py /path/to/vault --overwrite")
            return
        elif not arg.startswith('-'):
            target_dir = arg

    # 确保目录存在
    if not os.path.exists(target_dir):
        response = input(f"目录不存在: {target_dir}\n是否创建? [Y/n]: ").strip().lower()
        if response in ('', 'y', 'yes'):
            os.makedirs(target_dir)
            print(f"📂 已创建目录: {target_dir}")
        else:
            print("❌ 已取消")
            return

    # 创建文件
    create_files(target_dir, overwrite)


if __name__ == "__main__":
    main()
