# -*- coding: utf-8 -*-
# @Time    : 2025/3/9
# @Author  : Zhong Zhijie

import matplotlib.pyplot as plt
import seaborn as sns

# 设置合适的字体和大小
# 使用 LaTeX 字体（适用于数学公式和一致的论文风格）
# 作用: 提升论文中的可读性，保证风格与正文一致。
plt.rcParams.update({
    "text.usetex": True,  # 启用 LaTeX 渲染
    "font.family": "serif",  # 使用衬线字体
    "axes.labelsize": 10,  # 轴标签大小
    "font.size": 10,  # 其他字体大小
    "legend.fontsize": 8,  # 图例字体大小
    "xtick.labelsize": 8,  # x 轴刻度大小
    "ytick.labelsize": 8  # y 轴刻度大小
})

# 调整图像尺寸
# 论文中通常使用 单列（3.5 英寸 ≈ 8.9 cm）或 双列（7 英寸 ≈ 17.8 cm）布局：
# 作用: 避免图像过大导致排版混乱。
fig, ax = plt.subplots(figsize=(3.5, 2.5))  # 适用于单列排版

# 使用紧凑布局
# Matplotlib 默认会留较大的边距，可以使用 tight_layout() 让布局更紧凑：
# 作用: 避免子图之间重叠，提高排版效率。
fig.tight_layout()

# 提高分辨率
# 使用高 DPI（如 300 或 600），避免图像在打印或缩小时模糊：
# 作用: 保证论文中插图高清、不失真。
fig.savefig("output.pdf", dpi=300, bbox_inches='tight', pad_inches=0.05)

# 颜色与线条优化
# 使用 seaborn 样式（提高可读性）
sns.set_context("paper")  # 适用于论文
sns.set_style("whitegrid")  # 白色背景 + 网格
sns.set_palette("deep")  # 选择论文友好的颜色
# 更细的线条（防止打印时颜色混淆）
# 作用: 让图表清晰且适合黑白打印（避免花哨的颜色）。
x = [1]
y = [1]
ax.plot(x, y, linestyle='-', linewidth=1, color='black')

# 适当调整图例
# 作用: 避免图例遮挡数据，提高美观性。
ax.legend(loc='best', frameon=False)  # 让 Matplotlib 自动选择最佳位置，并去掉图例框

# 确保刻度合理
# 论文中一般不希望刻度太密集，避免混乱：
ax.set_xticks([0, 1, 2, 3])
ax.set_yticks([0, 5, 10, 15])

# 保存为矢量格式
# 推荐 PDF（矢量格式） 而不是 PNG（位图格式），避免放大后失真：
# 作用: 确保图像可以无损缩放，适用于学术出版。
fig.savefig("output.pdf", format="pdf", bbox_inches='tight')

# 避免边框过重
# 默认边框有四条（上、下、左、右），可以隐藏上和右边框，让图表更简洁：
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# 设置合适的刻度方向
# 默认刻度朝内外，但论文中更清晰的方式是只朝内：
ax.tick_params(direction='in')  # 让刻度朝内

# 避免网格线过于显眼
# 论文图表通常不需要特别强烈的网格线，可以让其变淡：
ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
