import os
from PIL import Image

def batch_resize(input_folder, output_folder, new_size):
    try:
        os.makedirs(output_folder, exist_ok=True)
        
        for filename in os.listdir(input_folder):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                input_path = os.path.join(input_folder, filename)
                output_path = os.path.join(output_folder, filename)
                
                image = Image.open(input_path)
                resized_image = image.resize(new_size, Image.ANTIALIAS)
                resized_image.save(output_path)
                
        print("批量图片大小转换成功！")
    except Exception as e:
        print("发生错误：", str(e))

if __name__ == "__main__":
    input_folder = r"C:\Users\Lazzy\Desktop\All\1"  # 输入文件夹路径
    output_folder = r"C:\Users\Lazzy\Desktop\All\change"  # 输出文件夹路径
    new_size = (800, 600)  # 新的图片尺寸，宽度 x 高度
    
    batch_resize(input_folder, output_folder, new_size)
