import fitz

def convert_first_page_to_image(pdf_path, output_path, zoom_x=2, zoom_y=2):
    """
    将PDF第一页转换为高质量PNG图像
    
    参数:
        pdf_path: PDF文件路径
        output_path: 输出图片路径
        zoom_x: x方向缩放系数（默认2，值越大分辨率越高）
        zoom_y: y方向缩放系数（默认2，值越大分辨率越高）
    """
    # 打开PDF文件
    doc = fitz.open(pdf_path)
    
    # 获取第一页
    page = doc[0]
    
    # 设置缩放矩阵以提高清晰度
    mat = fitz.Matrix(zoom_x, zoom_y)
    
    # 将第一页转换为高质量图像
    pix = page.get_pixmap(matrix=mat, alpha=False)
    
    # 保存图像
    pix.save(output_path)
    
    # 关闭PDF文件
    doc.close()

# 调用函数进行高质量转换（使用3倍缩放）
convert_first_page_to_image(
    "/cpfs/user/fanhuiming/index/static/pdf/drawww.pdf",
    "/cpfs/user/fanhuiming/index/static/images/SoTA_p6.png",
    zoom_x=3,
    zoom_y=3
)
