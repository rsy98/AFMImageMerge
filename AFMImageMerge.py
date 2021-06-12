'''
本程序用于原子力显微镜图片或其他同尺寸图片合并，可设定合成图为几行几列，并对各个子图按顺序进行字母标注和标尺标注
#使用方法：将本程序置于待合并图片文件夹内，image_array 内输入需合并图片的文件名，运行程序
Author: Ran S.Y. , E-mail: rsy98@163.com
2017年8月第一版，WZU-1B127
2019年5月第二版，修改标尺标注显示，图标扩充
'''

from PIL import Image, ImageDraw, ImageFont
# ttfont = ImageFont.truetype("simsun.ttc",30)     #设定标注字体，字号
ttfont = ImageFont.truetype("C:\Windows\Fonts\Arial.ttf", 24)
scalebar_font = ImageFont.truetype("C:\Windows\Fonts\Arial.ttf", 24)
image_array = ['figure1.png', 'figure2.png', 'figure3.png',
               'figure4.png', 'figure5.png', 'figure6.png']  # 待合并图片,后缀名可改为.bmp格式
img = Image.open(image_array[0])
width, height = img.size[0], img.size[1]  # 读取第一张图片宽度和高度，默认每张图片尺寸相同


label_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
               'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
label_lower = [i.lower() for i in label_upper]
label_upper_brace = ['(' + i + ')' for i in label_upper]
label_lower_brace = ['(' + i + ')' for i in label_lower]
label_upper_brace_half = [i + ')' for i in label_upper]
label_lower_brace_half = [i + ')' for i in label_lower]


image_row_number = 6  # 合成图行数，可根据需要改变数值
image_column_number = 3  # 合成图列数，可根据需要改变数值
Merge_Image = Image.new(
    'RGBA', (width*image_column_number, height*image_row_number))  # 合并成大的图片


image_index = 0
for i in range(image_row_number):
    for j in range(image_column_number):
        fromImage = Image.open(image_array[image_index])
        location_x = j*width
        location_y = i*height
        location = (location_x, location_y)
        draw = ImageDraw.Draw(fromImage)
        # fill=(255,255,255)文字为白色,如需黑色改为fill=(0,0,0)；label_upper可改为不同图标显示格式譬如label_lower
        draw.text((10, 5), label_upper[image_index],
                  fill=(255, 255, 255), font=ttfont)

        # if i==image_row_number-1 and j==image_column_number-1:
        #     draw.line(xy=[(400,480),(400+width/5,480)],fill=(255,255,255),width=3)   #标尺
        #     draw.text((415,482),'0.5 μm', fill=(255, 255, 255),font=scalebar_font)  #标尺文字标注
        # elif i==0 and j==0:
        #     draw.line(xy=[(400, 480), (400 + width / 5, 480)], fill=(255, 255, 255), width=3)  # 标尺
        #     draw.text((415, 482), '0.5 μm', fill=(255, 255, 255), font=scalebar_font)  # 标尺文字标注
        # else:
        #     pass

        draw.line(xy=[(400, 480), (400+width/5, 480)],
                  fill=(255, 255, 255), width=3)  # 标尺
        draw.text((415, 482), '0.5 \u03bc'+'m', fill=(255,
                                                      255, 255), font=scalebar_font)  # 标尺文字标注, 如是5umx5um图片,将标尺'0.5 \u03bc'+'m'改为'1 \u03bc'+'m'

        print(location)
        Merge_Image.paste(fromImage, location)
        image_index = image_index+1

Merge_Image.save('merged.jpg')  # 后缀名可改为其他格式
Merge_Image.show()
