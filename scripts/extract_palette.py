#!/usr/bin/env python3
"""从设计图中提取主色板，供沉淀规则时获取精确色值。

用法:
    python3 extract_palette.py <图片路径> [--k 6]

输出: 按面积占比从大到小输出 hex 色值与占比。模型再结合目测判断主色/辅色/强调色/中性色。
依赖: Pillow（缺失时输出提示，不阻塞流程，可退回目测近似值）。
"""
import argparse
import sys
from collections import Counter

try:
    from PIL import Image
except ImportError:
    print("Pillow 未安装，无法提取精确色值；改用目测近似值并在条目中标注「近似」。", file=sys.stderr)
    sys.exit(2)


def rgb_to_hex(rgb):
    return "#{:02x}{:02x}{:02x}".format(*rgb)


def quantize(img, k):
    img = img.convert("RGB").resize((200, 200))
    q = img.quantize(colors=k, method=Image.FASTOCTREE).convert("RGB")
    colors = Counter(q.getdata())
    total = sum(colors.values())
    return [(rgb_to_hex(c), n / total) for c, n in colors.most_common(k)]


def main():
    ap = argparse.ArgumentParser(description="提取设计图主色板")
    ap.add_argument("image", help="图片路径")
    ap.add_argument("--k", type=int, default=6, help="返回颜色数量，默认 6")
    args = ap.parse_args()

    try:
        img = Image.open(args.image)
    except Exception as e:  # noqa: BLE001
        print(f"无法打开图片 {args.image}: {e}", file=sys.stderr)
        sys.exit(2)

    for hex_, frac in quantize(img, args.k):
        print(f"{hex_}  {frac * 100:.1f}%")


if __name__ == "__main__":
    main()
