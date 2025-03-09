# -*- coding: utf-8 -*-
# @Time    : 2025/3/7
# @Author  : Zhong Zhijie

import os
import numpy as np
import matplotlib.pyplot as plt


def plot_multiple_bars(labels, *data, labels_list=None, colors_list=None, filename='output.pdf'):
    """
    绘制多组数据的柱状图，并保存为 PDF 文件。

    参数：
    - labels: list[str]，X 轴的类别标签。
    - *data: 可变数量的列表，每个列表代表一组柱状数据。
    - labels_list: list[str]，每组数据的图例标签（用于图例标注）。
    - colors_list: list[str]，每组数据的颜色（可选）。
    - filename: str，要保存的 PDF 文件名（不带扩展名）。
    """
    # 设置字体
    plt.rcParams["font.sans-serif"] = ["Times New Roman"]
    plt.rcParams["axes.unicode_minus"] = False  # 解决负号显示问题
    plt.rcParams['font.family'] = "Times New Roman"

    x = np.arange(len(labels))  # 生成 X 轴的刻度位置
    num_data = len(data)  # 计算数据集数量
    width = 0.8 / num_data  # 根据数据集数量调整柱子的宽度

    # 检查是否已有图形窗口，否则创建新窗口
    fig = plt.gcf() if plt.get_fignums() else plt.figure(figsize=(8, 6))
    ax = fig.gca()

    # 如果没有提供 labels_list，则自动生成
    if labels_list is None:
        labels_list = [f'数据集 {i + 1}' for i in range(num_data)]
    # 如果没有提供 colors_list，则使用默认颜色
    if colors_list is None:
        colors_list = ['#427AB2', '#F09148', '#A0D568', '#FFCE54', '#D8334A']

    # 遍历每组数据，绘制柱状图
    for i, data_set in enumerate(data):
        color = colors_list[i % len(colors_list)]  # 颜色不足时循环使用
        label = labels_list[i % len(labels_list)]  # 标签不足时循环使用
        ax.bar(x + (i - num_data / 2) * width + width / 2, data_set, width,
               label=label, color=color, ec='black', lw=0.5)  # ec=边框颜色，lw=边框宽度

    # 设置 Y 轴标签字体大小
    ax.tick_params(axis='y', direction='out', labelsize=16)
    # 设置 X 轴刻度
    ax.set_xticks(x)
    ax.set_xticklabels(labels, size=16)
    # 设定 Y 轴范围，保证数据对比清晰
    ax.set_ylim(bottom=0.92, top=1.0)
    # 添加图例
    ax.legend(fontsize='x-large')

    # 确保保存目录存在
    save_dir = 'figs'
    os.makedirs(save_dir, exist_ok=True)

    # 保存图形为 PDF 文件
    plt.savefig(f'{save_dir}/{filename}.pdf', format='pdf', bbox_inches='tight', dpi=300, pad_inches=0.01)
    plt.show()


# 示例数据
labels = ['Cora', 'Citeseer', 'PubMed', 'ScholarNet']

# AUC 数据
data_0 = [0.9640, 0.9784, 0.9676, 0.9910]
data_1 = [0.9600, 0.9737, 0.9763, 0.9891]
plot_multiple_bars(
    labels,
    data_0, data_1,
    labels_list=['Asymmetry', 'Symmetry'],
    colors_list=['#A8D8EA', '#FFC7C7'],
    filename='issymmetry_auc'
)

# # AP 数据
# data_0 = [0.9676, 0.9813, 0.9693, 0.9896]
# data_1 = [0.9642, 0.9770, 0.9788, 0.9882]
# plot_multiple_bars(
#     labels,
#     data_0, data_1,
#     labels_list=['Asymmetry', 'Symmetry'],
#     colors_list=['#A8D8EA', '#FFC7C7'],
#     filename='issymmetry_ap'
# )
