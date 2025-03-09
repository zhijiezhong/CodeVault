# -*- coding: utf-8 -*-
# @Time    : 2025/3/9
# @Author  : Zhong Zhijie

import matplotlib.pyplot as plt
import seaborn as sns


def save_plot_as_pdf(fig, filename, dpi=300, pad_inches=0.1):
    """
    保存 Matplotlib 图像为 PDF，并去除多余的空白。
    参数：
    fig : matplotlib.figure.Figure
        需要保存的图像对象。
    filename : str
        输出的 PDF 文件名。
    dpi : int, optional
        分辨率（默认 300）。
    pad_inches : float, optional
        边缘留白大小（默认 0.1）。
    """
    fig.savefig(filename, format='pdf', bbox_inches='tight', dpi=dpi, pad_inches=pad_inches)


def set_paper_style():
    """
    设置适用于论文的 Matplotlib 样式。
    """
    plt.rcParams.update({
        # "text.usetex": True,  # 启用 LaTeX 以获得更好的公式排版
        "font.family": "serif",  # 设定字体为衬线体
        "axes.labelsize": 10,  # 坐标轴标签字体大小
        "font.size": 10,  # 全局字体大小
        "legend.fontsize": 8,  # 图例字体大小
        "xtick.labelsize": 8,  # x 轴刻度字体大小
        "ytick.labelsize": 8,  # y 轴刻度字体大小
        "axes.titlesize": 10,  # 坐标轴标题大小
        "lines.linewidth": 1,  # 线条宽度
        "lines.markersize": 4  # 标记点大小
    })
    sns.set_context("paper")  # 设定 seaborn 风格为论文格式
    sns.set_palette("deep")  # 设置颜色方案


def optimize_plot(ax):
    """
    优化 Matplotlib 轴，使其更适合论文格式。
    """
    ax.ticklabel_format(style='plain')  # 关闭科学计数法
    ax.tick_params(direction='in', length=3, width=0.8)  # 让刻度朝内，增强可读性
    ax.margins(0.05)  # 增加 5% 空隙，避免数据点贴边
    ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)  # 使用虚线网格，增强对比度
    ax.spines["top"].set_visible(False)  # 隐藏上边框，使图表更简洁
    ax.spines["right"].set_visible(False)  # 隐藏右边框


def set_legend(ax, loc='best'):
    """
    优化图例，使其更适合论文格式。
    """
    ax.legend(loc=loc, frameon=False, fontsize=8)  # 关闭图例边框，减少视觉干扰


def adjust_subplots(fig, wspace=0.3, hspace=0.3):
    """
    调整子图间距，避免过度紧凑或分散。
    """
    fig.subplots_adjust(wspace=wspace, hspace=hspace)


def format_axes(ax):
    """
    统一格式，控制刻度和边界。
    """
    ax.set_xlabel("X Label", fontsize=10, fontweight='bold')  # x 轴标签
    ax.set_ylabel("Y Label", fontsize=10, fontweight='bold')  # y 轴标签
    ax.xaxis.set_tick_params(width=0.8)  # 调整 x 轴刻度线宽度
    ax.yaxis.set_tick_params(width=0.8)  # 调整 y 轴刻度线宽度


def set_line_styles(ax, styles=None):
    """
    设置不同方法的线条样式，适用于黑白打印。
    """
    if styles is None:
        styles = ['-', '--', '-.', ':']  # 定义四种不同的线型
    for line, style in zip(ax.get_lines(), styles):
        line.set_linestyle(style)  # 应用线条样式


def add_annotations(ax, annotations):
    """
    在图表中添加标注。
    参数：
    annotations : list of tuples [(x, y, text), ...]
        需要标注的坐标和文本内容。
    """
    for x, y, text in annotations:
        ax.text(x, y, text, fontsize=8, color='red')  # 使用红色字体增加标注可见性


def create_figure(figsize=(3.5, 2.5)):
    """
    创建适用于论文的 Matplotlib 图像。
    参数：
    figsize : tuple, optional
        指定图表的尺寸（默认 3.5 x 2.5 英寸）。
    返回：
    fig, ax : tuple
        返回 Matplotlib 图像和轴对象。
    """
    fig, ax = plt.subplots(figsize=figsize)
    return fig, ax


# 示例用法
if __name__ == "__main__":
    set_paper_style()  # 设置论文格式
    fig, ax = create_figure()  # 创建图表
    x = [1, 2, 3, 4]  # x 轴数据
    y1 = [4, 5, 6, 7]  # 第一组数据
    y2 = [3, 4, 5, 6]  # 第二组数据

    ax.plot(x, y1, label="Method A", linestyle='-', color='black')  # 绘制第一条曲线
    ax.plot(x, y2, label="Method B", linestyle='--', color='gray')  # 绘制第二条曲线

    optimize_plot(ax)  # 优化坐标轴
    set_legend(ax)  # 添加图例
    format_axes(ax)  # 统一格式
    add_annotations(ax, [(2, 5, "Key Point"), (3, 6, "Another Point")])  # 添加标注

    fig.tight_layout()  # 调整布局，避免重叠
    save_plot_as_pdf(fig, "output.pdf")  # 保存为 PDF 文件
