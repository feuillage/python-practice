# -*- coding:utf-8 -*-
# 第 0000 题：将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果

from PIL import Image, ImageDraw, ImageFont

def add_num(picPath, number):
    img = Image.open(picPath)
    draw = ImageDraw.Draw(img)
    myfont = ImageFont.truetype('arial.ttf', size=40)
    width, height = img.size
    draw.text((width-50, 10), str(number), font=myfont, fill='red')
    img.save('result.jpg')
	
if __name__ == '__main__':
    add_num('image.jpg', 55)