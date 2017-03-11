from PIL import Image
import argparse



parser = argparse.ArgumentParser()
parser.add_argument("file")
parser.add_argument("-o","--output")
parser.add_argument("-width",type=int,default=100)
parser.add_argument("-height",type=int,default=100)


arg = parser.parse_args()

IMG = arg.file
WIDTH = arg.width
HEIGHT = arg.height
OUTPUT = arg.output

ascii_chars = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")



def get_char(r,g,b,alpha = 256):
    if alpha == 0:
        return ' '
    length = len(ascii_chars)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    unit = (256.0 + 1)/length
    return ascii_chars[int(gray/unit)]

if __name__ == '__main__':
    im = Image.open(IMG)
    im = im.resize((WIDTH,HEIGHT),Image.NEAREST)

    txt = ""

    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j,i)))
        txt += "\n"
    print txt







if OUTPUT:
    with open(OUTPUT,"w") as f:
        f.write(txt)
else:
    with open("defalut.jpg",'w') as f:
        f.write(txt)