# -*- coding: utf-8 -*-
# @Time    : 2025/3/7
# @Author  : Zhong Zhijie

import matplotlib.pyplot as plt
import os


# 画Parameter Tuning的图
def plot_double_line(x, y1, y2, x_index, xlabel, labels, colors, filename):
    """
    绘制两条折线图，并保存为PDF文件。

    参数：
    - x: x轴数据（列表）
    - y1: 第一条折线的y轴数据（列表）
    - y2: 第二条折线的y轴数据（列表）
    - x_index: x轴刻度标签（列表）
    - xlabel: x轴标签（字符串）
    - labels: 图例标签（列表，包含两个字符串）
    - colors: 颜色列表（列表，包含两个颜色代码字符串）
    - filename: 保存的PDF文件名（字符串）
    """
    # 设置字体
    plt.rcParams["font.sans-serif"] = ["Times New Roman"]
    # 解决负号显示问题
    plt.rcParams["axes.unicode_minus"] = False

    plt.figure(figsize=(7, 6))
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.tick_params(labelsize=16)

    # 设置x轴的刻度
    plt.xticks(x)
    # 设置x轴标注
    plt.xlabel(xlabel, fontsize=22)

    # 设置x轴坐标范围
    plt.xlim(x[0] - 0.5, x[-1] + 0.5)
    # 设置y轴坐标范围
    plt.ylim(min(min(y1), min(y2)) - 0.002, max(max(y1), max(y2)) + 0.002)

    # 绘制折线
    plt.plot(x, y1, lw=1, c=colors[0], marker='s', ms=6, label=labels[0])
    plt.plot(x, y2, lw=1, c=colors[1], marker='^', ms=6, label=labels[1])
    _ = plt.xticks(x, x_index)

    # 设置y轴保留小数点后3位
    plt.gca().yaxis.set_major_formatter('{:.3f}'.format)
    # 标出图例
    plt.legend(fontsize='x-large')

    # 确保保存目录存在
    save_dir = 'figs'
    os.makedirs(save_dir, exist_ok=True)
    # 保存图表为 PDF 格式
    plt.savefig(f'{save_dir}/{filename}.pdf', format='pdf', bbox_inches='tight', dpi=300, pad_inches=0.05)
    plt.show()  # 显示图表


# 示例一

# x数据
x = [1, 2, 3, 4, 5]
x_index = ['32', '64', '128', '256', 512]
xlabel = 'Dimension of the second hidden layer'

# y1和y2数据
y1 = [0.9405, 0.9432, 0.9497, 0.9640, 0.9583]
y2 = [0.9451, 0.9526, 0.9583, 0.9676, 0.9653]

# 调用函数，传入labels和colors
labels = ['AUC', 'AP']
colors = ['#4169E1', '#FF0000']

filename = 'cora_param_hl2'

plot_double_line(x, y1, y2, x_index, xlabel, labels, colors, filename)


# 示例二
'''
from plot_double_line import plot_double_line

# x数据
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
x_index = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
xlabel = 'Number of k'

# y1和y2数据
y1 = [0.9567, 0.9571, 0.9583, 0.9617, 0.9619, 0.9625, 0.9640, 0.9631, 0.9630, 0.9631, 0.9624, 0.9631, 0.9631, 0.9621, 0.9619]
y2 = [0.9595, 0.9623, 0.9630, 0.9657, 0.9660, 0.9658, 0.9676, 0.9666, 0.9670, 0.9667, 0.9662, 0.9665, 0.9668, 0.9662, 0.9656]

# 调用函数，传入labels和colors
labels = ['AUC', 'AP']
colors = ['#4169E1', '#FF0000']

filename = 'cora_param_k'

plot_double_line(x, y1, y2, x_index, xlabel, labels, colors, filename)
'''
