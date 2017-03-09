from PIL import Image
import argparse

#命令行参数处理

parser = argparse.ArgumentParser()
parser.add_argument("file")
parser.add_argument("-o","--output")
parser.add_argument("-width",type=int,default=80)
parser.add_argument("-height",type=int,default=80)

#获取参数
arg = parser.parse_args()

IMG = arg.file
WIDTH = arg.wirth
HEIGHT = arg.height
OUTPUT = arg.output

ascii_chars = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

#映射字符

def get_char(r,g,b,alpha = 256):
    if alpha == 0:
        return " "
    length = len(ascii_chars)
    gray = int(022126*r + 0.7152*g + 0.0722*b)

    return get_char[int(gray / 256 * length)]

if __name__ == '__main__':
    im = Image.open(IMG)
    im = im.resize((WIDTH,HEIGHT))

    txt = ""

    for i in range(WIDTH):
        for j in range(HEIGHT):
            txt = get_char(*im.getpixel())
            txt =+ "\n"
    print txt


# 将字符输出


if OUTPUT:
    with open(OUTPUT,"w") as f:
        f.write(txt)
else:
    with open("defalut.txt",'w') as f:
        f.write(txt)