from PIL import Image
import numpy as np
import sys

# 元となる画像の読み込み
input1 = Image.open('input1.bmp')
input2 = Image.open('input2.bmp')
input3 = Image.open('input3.bmp')
#オリジナル画像のサイズの一致を確認後、サイズを取得

if (input1.size != input2.size)or(input1.size != input3.size):
    print("error")
    sys.exit(1)

width, height = input1.size
print(width, height)

#データを配列（行列）に格納
input1_pixels = np.array([[input1.getpixel((x,y)) for y in range(height)] for x in range(width)])
input2_pixels = np.array([[input2.getpixel((x,y)) for y in range(height)] for x in range(width)])
input3_pixels = np.array([[input3.getpixel((x,y)) for y in range(height)] for x in range(width)])


#出力画像を用意
output1 = Image.new("1",(width*2, height*2))
output2 = Image.new("1",(width*2, height*2))

#描画パターンごとの命令、putpixelでのvalueは0が黒
#黒２つ、白２つのパターン。 upは上半分が黒い
def up(tgt,x,y):
    if tgt == 1:
        output1.putpixel((2 * x + 0, 2 * y + 0), 0)
        output1.putpixel((2 * x + 1, 2 * y + 0), 0)
        output1.putpixel((2 * x + 0, 2 * y + 1), 1)
        output1.putpixel((2 * x + 1, 2 * y + 1), 1)
    elif tgt == 2:
        output2.putpixel((2 * x + 0, 2 * y + 0), 0)
        output2.putpixel((2 * x + 1, 2 * y + 0), 0)
        output2.putpixel((2 * x + 0, 2 * y + 1), 1)
        output2.putpixel((2 * x + 1, 2 * y + 1), 1)
    else:
        print("error")
def down(tgt,x,y):
    if tgt == 1:
        output1.putpixel((2 * x + 0, 2 * y + 0), 1)
        output1.putpixel((2 * x + 1, 2 * y + 0), 1)
        output1.putpixel((2 * x + 0, 2 * y + 1), 0)
        output1.putpixel((2 * x + 1, 2 * y + 1), 0)
    elif tgt == 2:
        output2.putpixel((2 * x + 0, 2 * y + 0), 1)
        output2.putpixel((2 * x + 1, 2 * y + 0), 1)
        output2.putpixel((2 * x + 0, 2 * y + 1), 0)
        output2.putpixel((2 * x + 1, 2 * y + 1), 0)
    else:
        print("error")
def left(tgt,x,y):
    if tgt == 1:
        output1.putpixel((2 * x + 0, 2 * y + 0), 0)
        output1.putpixel((2 * x + 1, 2 * y + 0), 1)
        output1.putpixel((2 * x + 0, 2 * y + 1), 0)
        output1.putpixel((2 * x + 1, 2 * y + 1), 1)
    elif tgt == 2:
        output2.putpixel((2 * x + 0, 2 * y + 0), 0)
        output2.putpixel((2 * x + 1, 2 * y + 0), 1)
        output2.putpixel((2 * x + 0, 2 * y + 1), 0)
        output2.putpixel((2 * x + 1, 2 * y + 1), 1)
    else:
        print("error")
def right(tgt,x,y):
    if tgt == 1:
        output1.putpixel((2 * x + 0, 2 * y + 0), 1)
        output1.putpixel((2 * x + 1, 2 * y + 0), 0)
        output1.putpixel((2 * x + 0, 2 * y + 1), 1)
        output1.putpixel((2 * x + 1, 2 * y + 1), 0)
    elif tgt == 2:
        output2.putpixel((2 * x + 0, 2 * y + 0), 1)
        output2.putpixel((2 * x + 1, 2 * y + 0), 0)
        output2.putpixel((2 * x + 0, 2 * y + 1), 1)
        output2.putpixel((2 * x + 1, 2 * y + 1), 0)
    else:
        print("error")
def slash(tgt,x,y):
    if tgt == 1:
        output1.putpixel((2 * x + 0, 2 * y + 0), 1)
        output1.putpixel((2 * x + 1, 2 * y + 0), 0)
        output1.putpixel((2 * x + 0, 2 * y + 1), 0)
        output1.putpixel((2 * x + 1, 2 * y + 1), 1)
    elif tgt == 2:
        output2.putpixel((2 * x + 0, 2 * y + 0), 1)
        output2.putpixel((2 * x + 1, 2 * y + 0), 0)
        output2.putpixel((2 * x + 0, 2 * y + 1), 0)
        output2.putpixel((2 * x + 1, 2 * y + 1), 1)
    else:
        print("error")
def back(tgt, x, y):
    if tgt == 1:
        output1.putpixel((2 * x + 0, 2 * y + 0), 0)
        output1.putpixel((2 * x + 1, 2 * y + 0), 1)
        output1.putpixel((2 * x + 0, 2 * y + 1), 1)
        output1.putpixel((2 * x + 1, 2 * y + 1), 0)
    elif tgt == 2:
        output2.putpixel((2 * x + 0, 2 * y + 0), 0)
        output2.putpixel((2 * x + 1, 2 * y + 0), 1)
        output2.putpixel((2 * x + 0, 2 * y + 1), 1)
        output2.putpixel((2 * x + 1, 2 * y + 1), 0)
    else:
        print("error")
#黒３つ、白１つのパターン。upltは左上が白い。
def uplt(tgt,x,y):
    if tgt == 1:
        output1.putpixel((2 * x + 0, 2 * y + 0), 1)
        output1.putpixel((2 * x + 1, 2 * y + 0), 0)
        output1.putpixel((2 * x + 0, 2 * y + 1), 0)
        output1.putpixel((2 * x + 1, 2 * y + 1), 0)
    elif tgt == 2:
        output2.putpixel((2 * x + 0, 2 * y + 0), 1)
        output2.putpixel((2 * x + 1, 2 * y + 0), 0)
        output2.putpixel((2 * x + 0, 2 * y + 1), 0)
        output2.putpixel((2 * x + 1, 2 * y + 1), 0)
    else:
        print("error")
def uprt(tgt,x,y):
    if tgt == 1:
        output1.putpixel((2 * x + 0, 2 * y + 0), 0)
        output1.putpixel((2 * x + 1, 2 * y + 0), 1)
        output1.putpixel((2 * x + 0, 2 * y + 1), 0)
        output1.putpixel((2 * x + 1, 2 * y + 1), 0)
    elif tgt == 2:
        output2.putpixel((2 * x + 0, 2 * y + 0), 0)
        output2.putpixel((2 * x + 1, 2 * y + 0), 1)
        output2.putpixel((2 * x + 0, 2 * y + 1), 0)
        output2.putpixel((2 * x + 1, 2 * y + 1), 0)
    else:
        print("error")
def dnlt(tgt,x,y):
    if tgt == 1:
        output1.putpixel((2 * x + 0, 2 * y + 0), 0)
        output1.putpixel((2 * x + 1, 2 * y + 0), 0)
        output1.putpixel((2 * x + 0, 2 * y + 1), 1)
        output1.putpixel((2 * x + 1, 2 * y + 1), 0)
    elif tgt == 2:
        output2.putpixel((2 * x + 0, 2 * y + 0), 0)
        output2.putpixel((2 * x + 1, 2 * y + 0), 0)
        output2.putpixel((2 * x + 0, 2 * y + 1), 1)
        output2.putpixel((2 * x + 1, 2 * y + 1), 0)
    else:
        print("error")
def dnrt(tgt,x,y):
    if tgt == 1:
        output1.putpixel((2 * x + 0, 2 * y + 0), 0)
        output1.putpixel((2 * x + 1, 2 * y + 0), 0)
        output1.putpixel((2 * x + 0, 2 * y + 1), 0)
        output1.putpixel((2 * x + 1, 2 * y + 1), 1)
    elif tgt == 2:
        output2.putpixel((2 * x + 0, 2 * y + 0), 0)
        output2.putpixel((2 * x + 1, 2 * y + 0), 0)
        output2.putpixel((2 * x + 0, 2 * y + 1), 0)
        output2.putpixel((2 * x + 1, 2 * y + 1), 1)
    else:
        print("error")


def DOwww(x,y):
    r=0
    r= np.random.randint(6)
    if r==0:
        slash(1,x,y)
        left(2,x,y)
    elif r==1:
        back(1,x,y)
        down(2,x,y)
    elif r==2:
        up(1,x,y)
        slash(2,x,y)
    elif r==3:
        down(1,x,y)
        right(2,x,y)
    elif r==4:
        left(1,x,y)
        back(2,x,y)
    elif r==5:
        right(1,x,y)
        up(2,x,y)
    else:
        print("error")
def DOwwb(x,y):
    r=0
    r = np.random.randint(6)
    if r==0:
        slash(1,x,y)
        back(2,x,y)
    elif r==1:
        back(1,x,y)
        slash(2,x,y)
    elif r==2:
        up(1,x,y)
        down(2,x,y)
    elif r==3:
        down(1,x,y)
        up(2,x,y)
    elif r==4:
        left(1,x,y)
        right(2,x,y)
    elif r==5:
        right(1,x,y)
        left(2,x,y)
    else:
        print("error")
def DOwbw(x,y):
    r = 0
    r = np.random.randint(6)
    if r==0:
        slash(1,x,y)
        uplt(2,x,y)
    elif r==1:
        back(1,x,y)
        uprt(2,x,y)
    elif r==2:
        up(1,x,y)
        dnlt(2,x,y)
    elif r==3:
        down(1,x,y)
        uplt(2,x,y)
    elif r==4:
        left(1,x,y)
        dnrt(2,x,y)
    elif r==5:
        right(1,x,y)
        dnlt(2,x,y)
    else:
        print("error")
def DOwbb(x,y):
    r = 0
    r = np.random.randint(6)
    if r == 0:
        slash(1, x, y)
        uprt(2, x, y)
    elif r == 1:
        back(1, x, y)
        dnrt(2, x, y)
    elif r == 2:
        up(1, x, y)
        uprt(2, x, y)
    elif r == 3:
        down(1, x, y)
        dnlt(2, x, y)
    elif r == 4:
        left(1, x, y)
        uplt(2, x, y)
    elif r == 5:
        right(1, x, y)
        dnrt(2, x, y)
    else:
        print("error")
def DObww(x,y):
    r = 0
    r = np.random.randint(6)
    if r == 0:
        slash(2, x, y)
        uplt(1, x, y)
    elif r == 1:
        back(2, x, y)
        uprt(1, x, y)
    elif r == 2:
        up(2, x, y)
        dnlt(1, x, y)
    elif r == 3:
        down(2, x, y)
        uplt(1, x, y)
    elif r == 4:
        left(2, x, y)
        dnrt(1, x, y)
    elif r == 5:
        right(2, x, y)
        dnlt(1, x, y)
    else:
        print("error")
def DObwb(x,y):
    r = 0
    r = np.random.randint(6)
    if r == 0:
        slash(2, x, y)
        uprt(1, x, y)
    elif r == 1:
        back(2, x, y)
        dnrt(1, x, y)
    elif r == 2:
        up(2, x, y)
        uprt(1, x, y)
    elif r == 3:
        down(2, x, y)
        dnlt(1, x, y)
    elif r == 4:
        left(2, x, y)
        uplt(1, x, y)
    elif r == 5:
        right(2, x, y)
        dnrt(1, x, y)
    else:
        print("error")
def DObbw(x,y):
    r=0
    r = np.random.randint(4)
    if r==0:
        uplt(1,x,y)
        uplt(2,x,y)
    elif r==1:
        uprt(1,x,y)
        uprt(2,x,y)
    elif r==2:
        dnlt(1,x,y)
        dnlt(2,x,y)
    elif r==3:
        dnrt(1,x,y)
        dnrt(2,x,y)
    else:
        print("error")
def DObbb(x,y):
    r=0
    r=np.random.randint(4)
    if r==0:
        uplt(1,x,y)
        dnrt(2,x,y)
    elif r==1:
        uprt(1,x,y)
        dnlt(2,x,y)
    elif r==2:
        dnrt(1,x,y)
        uplt(2,x,y)
    elif r==3:
        dnlt(1,x,y)
        uprt(2,x,y)
    else:
        print("error")

#ここから各ピクセルについての情報処理
white = [255,255,255]
black = [0,0,0]
w = 1
b = 0

for x in range(width):
    for y in range(height):
        value1 = input1_pixels[x][y]
        value2 = input2_pixels[x][y]
        value3 = input3_pixels[x][y]

        if np.allclose(value1, white):
            value1=w
        else:
            value1=b
        if np.allclose(value2, white):
            value2=w
        else:
            value2=b
        if np.allclose(value3, white):
            value3=w
        else:
            value3=b

        if value1 == w and value2 == w and value3 == w:
            DOwww(x,y)
        elif value1 == w and value2 == w and value3 == b:
            DOwwb(x,y)
        elif value1 == w and value2 == b and value3 == w:
            DOwbw(x,y)
        elif value1 == w and value2 == b and value3 == b:
            DOwbb(x,y)
        elif value1 == b and value2 == w and value3 == w:
            DObww(x,y)
        elif value1 == b and value2 == w and value3 == b:
            DObwb(x,y)
        elif value1 == b and value2 == b and value3 == w:
            DObbw(x,y)
        elif value1 == b and value2 == b and value3 == b:
            DObbb(x,y)
        else:
            print(x, y, "error")

#ピクセルごとのは処理おわり、のはず

#最後の出力
output1.save("output1.bmp")
output2.save("output2.bmp")
