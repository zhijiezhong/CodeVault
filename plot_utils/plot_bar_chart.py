# -*- coding: utf-8 -*-
# @Time    : 2025/3/7
# @Author  : Zhong Zhijie
import os

import matplotlib.pyplot as plt


def plot_bar_chart(labels, data, x_label, y_label, filename, bar_color='skyblue'):
    """
    绘制柱状图并保存为 PDF 文件。

    参数：
    - labels: 类别标签列表（X 轴）
    - data: 每个类别对应的数值（Y 轴）
    - x_label: X 轴标签
    - y_label: Y 轴标签
    - output_filename: 输出 PDF 文件名（不带扩展名）
    - bar_color: 柱状图颜色，默认为 'skyblue'
    """
    plt.figure(figsize=(7, 6))  # 设置图表大小
    bars = plt.bar(labels, data, color=bar_color)  # 绘制柱状图

    # 在每个条形上方显示数值
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, height, f'{height:.1f}',
                 ha='center', va='bottom', fontsize=10)

    # plt.xlabel(x_label)  # 设置 X 轴标签
    plt.ylabel(y_label)  # 设置 Y 轴标签
    plt.xticks(rotation=0)  # X 轴标签旋转角度
    plt.grid(axis='y', linestyle='--', alpha=0.5)  # 添加 Y 轴方向的网格线，提高可读性

    # 确保保存目录存在
    save_dir = 'figs'
    os.makedirs(save_dir, exist_ok=True)
    # 保存图表为 PDF 格式
    plt.savefig(f'{save_dir}/{filename}.pdf', format='pdf', bbox_inches='tight', dpi=300, pad_inches=0.05)
    plt.show()  # 显示图表


# 示例
model_names = ["GNAE", "ARGA", "ARVGA", "A$^3$VGAE"]
execution_times = [27.7, 35.0, 36.4, 32.1]
dataset_name = 'Cora'
time_label = 'Time cost (sec)'
chart_color = 'skyblue'

plot_bar_chart(model_names, execution_times, dataset_name, time_label, 'bar_chart1', chart_color)
#
# execution_times = [30.5, 35.6, 36.3, 41.2]
# dataset_name = 'Citeseer'
# plot_bar_chart(model_names, execution_times, dataset_name, time_label, 'bar_chart2', chart_color)
#
#
# execution_times = [185.8, 210.4, 221.1, 247.1]
# dataset_name = 'PubMed'
# plot_bar_chart(model_names, execution_times, dataset_name, time_label, 'bar_chart3', chart_color)
#
#
# execution_times = [214.5, 267.3, 265.7, 287.4]
# dataset_name = 'ScholarNet'
# plot_bar_chart(model_names, execution_times, dataset_name, time_label, 'bar_chart4', chart_color)

