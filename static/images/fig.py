from PIL import Image

def remove_white_border(img_path, output_path):
    img = Image.open(img_path)
    
    # 转换为RGB模式（如果是RGBA）
    if img.mode == 'RGBA':
        # 创建白色背景
        background = Image.new('RGB', img.size, (255, 255, 255))
        background.paste(img, mask=img.split()[3])
        img = background
    
    # 转为灰度图，反转颜色（白变黑，黑变白）
    gray = img.convert('L')
    from PIL import ImageOps
    inverted = ImageOps.invert(gray)
    
    # 获取非白色区域的边界框
    bbox = inverted.getbbox()
    
    if bbox:
        cropped = img.crop(bbox)
        cropped.save(output_path)
        print(f"裁剪成功: {bbox}")
    else:
        print("未检测到边界，保存原图")
        img.save(output_path)

# 使用
remove_white_border('/cpfs/user/fanhuiming/index/static/images/Gemini_Generated_Image_v8bu8wv8bu8wv8bu.png', 'logo.png')
