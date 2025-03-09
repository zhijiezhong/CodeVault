import os
from pypdf import PdfReader, PdfWriter

# todo: 这个函数不在需要了，因为matplotlib可以保存图片时候，可以自动去除空白区域


def cm_to_points(cm):
    return cm * 28.35  # 1厘米约等于28.35点


def crop_pdf(input_directory, left_cm, right_cm, top_cm, bottom_cm):
    # 将厘米转换为点
    left = cm_to_points(left_cm)
    right = cm_to_points(right_cm)
    top = cm_to_points(top_cm)
    bottom = cm_to_points(bottom_cm)

    # 确保输出目录存在
    output_directory = os.path.join(input_directory, 'cropped')
    os.makedirs(output_directory, exist_ok=True)

    # 遍历输入目录中的所有文件
    for filename in os.listdir(input_directory):
        if filename.endswith('.pdf'):
            input_path = os.path.join(input_directory, filename)
            output_path = os.path.join(output_directory, filename)

            # 读取PDF
            reader = PdfReader(input_path)
            writer = PdfWriter()

            # 裁剪每一页
            for page in reader.pages:
                media_box = page.mediabox
                page.mediabox.lower_left = (media_box.lower_left[0] + left, media_box.lower_left[1] + bottom)
                page.mediabox.upper_right = (media_box.upper_right[0] - right, media_box.upper_right[1] - top)
                writer.add_page(page)

            # 写入裁剪后的PDF
            with open(output_path, 'wb') as output_pdf:
                writer.write(output_pdf)

    print(f'All PDFs in {input_directory} have been cropped and saved to {output_directory}')


# # 示例
# input_directory = '.'
# left_cm = 0
# right_cm = 0
# top_cm = 0
# bottom_cm = 0
# crop_pdf(input_directory, left_cm, right_cm, top_cm, bottom_cm)
