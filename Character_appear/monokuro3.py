from PIL import Image
import numpy as np

input1 = Image.open('original1.jpg')
input2 = Image.open('original2.jpg')
input3 = Image.open('original3.jpg')
if input1.size != input2.size or input1.size != input3.size:
    print("error")
width, height = input1.size
input1_pixels = np.array([[input1.getpixel((x,y)) for y in range(height)] for x in range(width)])
input2_pixels = np.array([[input2.getpixel((x,y)) for y in range(height)] for x in range(width)])
input3_pixels = np.array([[input3.getpixel((x,y)) for y in range(height)] for x in range(width)])
# 出力のImageオブジェクトを作成する
output1 = Image.new('RGB', (width*2, height*2))
output2 = Image.new('RGB', (width*2, height*2))

# 入力：input1_pixels, input2_pixels,input3_pixels
# 出力：output1, output2
# print(input1_pixels[0,0])


# それぞれのパターンを関数にする
# 白黒黒白
def func_1a(output):
    output.putpixel((x*2,y*2),(255,255,255))
    output.putpixel((x*2+1,y*2),(0,0,0))
    output.putpixel((x*2,y*2+1),(0,0,0))
    output.putpixel((x*2+1,y*2+1),(255,255,255))

# 黒白白黒
def func_1b(output):
    output.putpixel((x*2,y*2),(0,0,0))
    output.putpixel((x*2+1,y*2),(255,255,255))
    output.putpixel((x*2,y*2+1),(255,255,255))
    output.putpixel((x*2+1,y*2+1),(0,0,0))

# 黒黒白白
def func_2a(output):
    output.putpixel((x*2,y*2),(0,0,0))
    output.putpixel((x*2+1,y*2),(0,0,0))
    output.putpixel((x*2,y*2+1),(255,255,255))
    output.putpixel((x*2+1,y*2+1),(255,255,255))

# 白黒白黒
def func_2b(output):
    output.putpixel((x*2,y*2),(255,255,255))
    output.putpixel((x*2,y*2+1),(0,0,0))
    output.putpixel((x*2+1,y*2),(255,255,255))
    output.putpixel((x*2+1,y*2+1),(0,0,0))

# 白白黒黒
def func_2c(output):
    output.putpixel((x*2,y*2),(255,255,255))
    output.putpixel((x*2,y*2+1),(255,255,255))
    output.putpixel((x*2+1,y*2),(0,0,0))
    output.putpixel((x*2+1,y*2+1),(0,0,0))

# 黒白黒白
def func_2d(output):
    output.putpixel((x*2,y*2),(0,0,0))
    output.putpixel((x*2,y*2+1),(255,255,255))
    output.putpixel((x*2+1,y*2),(0,0,0))
    output.putpixel((x*2+1,y*2+1),(255,255,255))

# 白黒黒黒
def func_3a(output):
    output.putpixel((x*2+1,y*2),(255,255,255))
    output.putpixel((x*2,y*2+1),(0,0,0))
    output.putpixel((x*2,y*2),(0,0,0))
    output.putpixel((x*2+1,y*2+1),(0,0,0))

# 黒白黒黒
def func_3b(output):
    output.putpixel((x*2,y*2),(0,0,0))
    output.putpixel((x*2,y*2+1),(255,255,255))
    output.putpixel((x*2+1,y*2),(0,0,0))
    output.putpixel((x*2+1,y*2+1),(0,0,0))

# 黒黒黒白
def func_3c(output):
    output.putpixel((x*2,y*2),(0,0,0))
    output.putpixel((x*2,y*2+1),(0,0,0))
    output.putpixel((x*2+1,y*2),(0,0,0))
    output.putpixel((x*2+1,y*2+1),(255,255,255))

# 黒黒白黒
def func_3d(output):
    output.putpixel((x*2,y*2),(0,0,0))
    output.putpixel((x*2,y*2+1),(0,0,0))
    output.putpixel((x*2+1,y*2),(255,255,255))
    output.putpixel((x*2+1,y*2+1),(0,0,0))

def func_000(ary, output1, output2):
    r1=np.random.randint(6)
    r2=np.random.randint(4)
    if r1 == 0 and r2 == 0:
        func_1a(output1)
        func_2a(output2)
    elif r1 == 0 and r2 == 1:
        func_1a(output1)
        func_2b(output2)
    elif r1 == 0 and r2 == 2:
        func_1a(output1)
        func_2c(output2)
    elif r1 == 0 and r2 == 3:
        func_1a(output1)
        func_2d(output2)
    elif r1 == 1 and r2 == 0:
        func_1b(output1)
        func_2a(output2)
    elif r1 == 1 and r2 == 1:
        func_1b(output1)
        func_2b(output2)
    elif r1 == 1 and r2 == 2:
        func_1b(output1)
        func_2b(output2)
    elif r1 == 1 and r2 == 3:
        func_1b(output1)
        func_2c(output2)
    elif r1 == 2 and r2 == 0:
        func_2a(output1)
        func_1a(output2)
    elif r1 == 2 and r2 == 1:
        func_2a(output1)
        func_1b(output2)
    elif r1 == 2 and r2 == 2:
        func_2a(output1)
        func_2b(output2)
    elif r1 == 2 and r2 == 3:
        func_2a(output1)
        func_2d(output2)
    elif r1 == 3 and r2 == 0:
        func_2b(output1)
        func_1a(output2)
    elif r1 == 3 and r2 == 1:
        func_2b(output1)
        func_1b(output2)
    elif r1 == 3 and r2 == 2:
        func_2b(output1)
        func_2c(output2)
    elif r1 == 3 and r2 == 3:
        func_2b(output1)
        func_2a(output2)
    elif r1 == 4 and r2 == 0:
        func_2c(output1)
        func_1a(output2)
    elif r1 == 4 and r2 == 1:
        func_2c(output1)
        func_1b(output2)
    elif r1 == 4 and r2 == 2:
        func_2c(output1)
        func_2d(output2)
    elif r1 == 4 and r2 == 3:
        func_2c(output1)
        func_2b(output2)
    elif r1 == 5 and r2 == 0:
        func_2d(output1)
        func_1a(output2)
    elif r1 == 5 and r2 == 1:
        func_2d(output1)
        func_1b(output2)
    elif r1 == 5 and r2 == 2:
        func_2d(output1)
        func_2a(output2)
    elif r1 == 5 and r2 == 3:
        func_2d(output1)
        func_2c(output2)
    else:
        print("error(func_000)")

def func_001(ary, output1, output2):
    r1=np.random.randint(6)
    if r1 == 0:
        func_1a(output1)
        func_1b(output2)
    elif r1 == 1:
        func_1b(output1)
        func_1a(output2)
    elif r1 == 2:
        func_2a(output1)
        func_2c(output2)
    elif r1 == 3:
        func_2b(output1)
        func_2d(output2)
    elif r1 == 4:
        func_2c(output1)
        func_2a(output2)
    elif r1 == 5:
        func_2d(output1)
        func_2b(output2)
    else:
        print("error(func_001)")

def func_010(ary, output1, output2):
    r1=np.random.randint(6)
    r2=np.random.randint(2)
    if r1 == 0 and r2 == 0:
        func_1a(output1)
        func_3a(output2)
    elif r1 == 0 and r2 == 1:
        func_1a(output1)
        func_3c(output2)
    elif r1 == 1 and r2 ==0:
        func_1b(output1)
        func_3b(output2)
    elif r1 == 1 and r2 ==1:
        func_1b(output1)
        func_3d(output2)
    elif r1 == 2 and r2 == 0:
        func_2a(output1)
        func_3c(output2)
    elif r1 == 2 and r2 == 1:
        func_2a(output1)
        func_3d(output2)
    elif r1 == 3 and r2 == 0:
        func_2b(output1)
        func_3d(output2)
    elif r1 == 3 and r2 == 1:
        func_2b(output1)
        func_3a(output2)
    elif r1 == 4 and r2 == 0:
        func_2c(output1)
        func_3a(output2)
    elif r1 == 4 and r2 == 1:
        func_2c(output1)
        func_3b(output2)
    elif r1 == 5 and r2 == 0:
        func_2d(output1)
        func_3b(output2)
    elif r1 == 5 and r2 == 1:
        func_2d(output1)
        func_3c(output2)
    else:
        ptint("error(func_010)")

def func_011(ary, output1, output2):
    r1=np.random.randint(6)
    r2=np.random.randint(2)
    if r1 == 0 and r2 == 0:
        func_1a(output1)
        func_3b(output2)
    elif r1 == 0 and r2 == 1:
        func_1a(output1)
        func_3d(output2)
    elif r1 == 1 and r2 ==0:
        func_1b(output1)
        func_3a(output2)
    elif r1 == 1 and r2 ==1:
        func_1b(output1)
        func_3c(output2)
    elif r1 == 2 and r2 == 0:
        func_2a(output1)
        func_3a(output2)
    elif r1 == 2 and r2 == 1:
        func_2a(output1)
        func_3b(output2)
    elif r1 == 3 and r2 == 0:
        func_2b(output1)
        func_3b(output2)
    elif r1 == 3 and r2 == 1:
        func_2b(output1)
        func_3c(output2)
    elif r1 == 4 and r2 == 0:
        func_2c(output1)
        func_3c(output2)
    elif r1 == 4 and r2 == 1:
        func_2c(output1)
        func_3d(output2)
    elif r1 == 5 and r2 == 0:
        func_2d(output1)
        func_3d(output2)
    elif r1 == 5 and r2 == 1:
        func_2d(output1)
        func_3a(output2)
    else:
        ptint("error(func_011)")

def func_100(ary, output1, output2):
    r1=np.random.randint(4)
    r2=np.random.randint(3)
    if r1 == 0 and r2 == 0:
        func_3a(output1)
        func_1a(output2)
    elif r1 == 0 and r2 == 1:
        func_3a(output1)
        func_2b(output2)
    elif r1 == 0 and r2 == 2:
        func_3a(output1)
        func_2c(output2)
    elif r1 == 1 and r2 ==0:
        func_3b(output1)
        func_1b(output2)
    elif r1 == 1 and r2 ==1:
        func_3b(output1)
        func_2c(output2)
    elif r1 == 1 and r2 ==2:
        func_3b(output1)
        func_2d(output2)
    elif r1 == 2 and r2 == 0:
        func_3c(output1)
        func_1a(output2)
    elif r1 == 2 and r2 == 1:
        func_3c(output1)
        func_2d(output2)
    elif r1 == 2 and r2 == 2:
        func_3c(output1)
        func_2a(output2)
    elif r1 ==3 and r2 == 0:
        func_3d(output1)
        func_1b(output2)
    elif r1 ==3 and r2 == 1:
        func_3d(output1)
        func_2a(output2)
    elif r1 ==3 and r2 == 2:
        func_3d(output1)
        func_2b(output2)
    else:
        ptint("error(func_100)")

def func_101(ary, output1, output2):
    r1=np.random.randint(4)
    r2=np.random.randint(3)
    if r1 == 0 and r2 == 0:
        func_3a(output1)
        func_1b(output2)
    elif r1 == 0 and r2 == 1:
        func_3a(output1)
        func_2d(output2)
    elif r1 == 0 and r2 == 2:
        func_3a(output1)
        func_2a(output2)
    elif r1 == 1 and r2 ==0:
        func_3b(output1)
        func_1a(output2)
    elif r1 == 1 and r2 ==1:
        func_3b(output1)
        func_2a(output2)
    elif r1 == 1 and r2 ==2:
        func_3b(output1)
        func_2b(output2)
    elif r1 == 2 and r2 == 0:
        func_3c(output1)
        func_1b(output2)
    elif r1 == 2 and r2 == 1:
        func_3c(output1)
        func_2b(output2)
    elif r1 == 2 and r2 == 2:
        func_3c(output1)
        func_2c(output2)
    elif r1 ==3 and r2 == 0:
        func_3d(output1)
        func_1a(output2)
    elif r1 ==3 and r2 == 1:
        func_3d(output1)
        func_2c(output2)
    elif r1 ==3 and r2 == 2:
        func_3d(output1)
        func_2a(output2)
    else:
        ptint("error(func_101)")

def func_110(ary, output1, output2):
    r1=np.random.randint(4)
    if r1 == 0:
        func_3a(output1)
        func_3a(output2)
    elif r1 == 1:
        func_3b(output1)
        func_3b(output2)
    elif r1 == 2:
        func_3c(output1)
        func_3c(output2)
    elif r1 == 3:
        func_3d(output1)
        func_3d(output2)
    else:
        print("error(func_110)")

def func_111(ary, output1, output2):
    r1=np.random.randint(4)
    r2=np.random.randint(3)
    if r1 == 0 and r2 == 0:
        func_3a(output1)
        func_3b(output2)
    elif r1 == 0 and r2 == 1:
        func_3a(output1)
        func_3c(output2)
    elif r1 == 0 and r2 == 2:
        func_3a(output1)
        func_3d(output2)
    elif r1 == 1 and r2 ==0:
        func_3b(output1)
        func_3c(output2)
    elif r1 == 1 and r2 ==1:
        func_3b(output1)
        func_3d(output2)
    elif r1 == 1 and r2 ==2:
        func_3b(output1)
        func_3a(output2)
    elif r1 == 2 and r2 == 0:
        func_3c(output1)
        func_3d(output2)
    elif r1 == 2 and r2 == 1:
        func_3c(output1)
        func_3a(output2)
    elif r1 == 2 and r2 == 2:
        func_3c(output1)
        func_3b(output2)
    elif r1 ==3 and r2 == 0:
        func_3d(output1)
        func_3a(output2)
    elif r1 ==3 and r2 == 1:
        func_3d(output1)
        func_3b(output2)
    elif r1 ==3 and r2 == 2:
        func_3d(output1)
        func_3c(output2)
    else:
        ptint("error(func_111)")

num = 0

# output1用とoutput2用の乱数の生成
rand = np.random.randint(0,12,(height*width,2))
# rand[x(0~71)][y(0,1)]
for y in range(height):
    for x in range(width):
        # 場合分け
        tmp = []
        # print(tmp)
        if all(input1_pixels[x,y] >= [100,100,100]):
            tmp.append(0)
        else:
            tmp.append(1)
        if all(input2_pixels[x,y] >= [100,100,100]):
            tmp.append(0)
        else:
            tmp.append(1)
        if all(input3_pixels[x,y] >= [100,100,100]):
            tmp.append(0)
        else:
            tmp.append(1)
        # print(tmp[0])
        # print(tmp)
        # 場合分け終了　情報を3桁の配列に格納 白：０、黒：１
        # print(rand[num][0])
        # outputにpixelを埋め込む
        if tmp == [0,0,0]:
            if rand[num][0] == 0 or 1:
                func_1a(output1)
                if rand[num][1] == 0 or 1 or 2:
                    func_2b(output2)
                elif rand[num][1] == 3 or 4 or 5:
                    func_2a(output2)
                elif rand[num][1] == 6 or 7 or 8:
                    func_2d(output2)
                else:
                    func_2c(output2)
            elif rand[num][0] == 2 or 3:
                func_1b(output1)
                if rand[num][1] == 0 or 1 or 2:
                    func_2a(output2)
                elif rand[num][1] == 3 or 4 or 5:
                    func_2b(output2)
                elif rand[num][1] == 6 or 7 or 8:
                    func_2c(output2)
                else:
                    func_2d(output2)
            elif rand[num][0] == 4 or 5:
                func_2a(output1)
                if rand[num][1] == 0 or 1 or 2:
                    func_1a(output2)
                elif rand[num][1] == 3 or 4 or 5:
                    func_1b(output2)
                elif rand[num][1] == 6 or 7 or 8:
                    func_2b(output2)
                else:
                    func_2d(output2)
            elif rand[num][0] == 6 or 7:
                func_2b(output1)
                if rand[num][1] == 0 or 1 or 2:
                    func_1a(output2)
                elif rand[num][1] == 3 or 4 or 5:
                    func_1b(output2)
                elif rand[num][1] == 6 or 7 or 8:
                    func_2c(output2)
                else:
                    func_2a(output2)
            elif rand[num][0] == 8 or 9:
                func_2c(output1)
                if rand[num][1] == 0 or 1 or 2:
                    func_1a(output2)
                elif rand[num][1] == 3 or 4 or 5:
                    func_1b(output2)
                elif rand[num][1] == 6 or 7 or 8:
                    func_2d(output2)
                else:
                    func_2b(output2)
            else:
                func_2d(output1)
                if rand[num][1] == 0 or 1 or 2:
                    func_1a(output2)
                elif rand[num][1] == 3 or 4 or 5:
                    func_1b(output2)
                elif rand[num][1] == 6 or 7 or 8:
                    func_2a(output2)
                else:
                    func_2c(output2)
        elif tmp == [0,0,1]:
            if rand[num][0] == 0 or 1:
                func_1a(output1)
                func_1b(output2)
            elif rand[num][0] == 2 or 3:
                func_1b(output1)
                func_1a(output2)
            elif rand[num][0] == 4 or 5:
                func_2a(output1)
                func_2c(output2)
            elif rand[num][0] == 6 or 7:
                func_2b(output1)
                func_2d(output2)
            elif rand[num][0] == 8 or 9:
                func_2c(output1)
                func_2a(output2)
            else:
                func_2d(output1)
                func_2b(output2)
        elif tmp == [0,1,0]:
            if rand[num][0] == 0 or 1:
                func_1a(output1)
                if rand[num][1] <= 6:
                    func_3a(output2)
                else:
                    func_3c(output2)
            elif rand[num][0] == 2 or 3:
                func_1b(output1)
                if rand[num][1] <= 6:
                    func_3b(output2)
                else:
                    func_3d(output2)
            elif rand[num][0] == 4 or 5:
                func_2a(output1)
                if rand[num][1] <= 6:
                    func_3c(output2)
                else:
                    func_3d(output2)
            elif rand[num][0] == 6 or 7:
                func_2b(output1)
                if rand[num][1] <= 6:
                    func_3d(output2)
                else:
                    func_3a(output2)
            elif rand[num][0] == 8 or 9:
                func_2c(output1)
                if rand[num][1] <= 6:
                    func_3a(output2)
                else:
                    func_3b(output2)
            else:
                func_2d(output1)
                if rand[num][1] <= 6:
                    func_3b(output2)
                else:
                    func_3c(output2)
        elif tmp == [0,1,1]:
            if rand[num][0] == 0 or 1:
                func_1a(output1)
                if rand[num][1] <= 6:
                    func_3b(output2)
                else:
                    func_3d(output2)
            elif rand[num][0] == 2 or 3:
                func_1b(output1)
                if rand[num][1] <= 6:
                    func_3a(output2)
                else:
                    func_3c(output2)
            elif rand[num][0] == 4 or 5:
                func_2a(output1)
                if rand[num][1] <= 6:
                    func_3a(output2)
                else:
                    func_3b(output2)
            elif rand[num][0] == 6 or 7:
                func_2b(output1)
                if rand[num][1] <= 6:
                    func_3b(output2)
                else:
                    func_3c(output2)
            elif rand[num][0] == 8 or 9:
                func_2c(output1)
                if rand[num][1] <= 6:
                    func_3c(output2)
                else:
                    func_3d(output2)
            elif rand[num][0] == 10 or 11:
                func_2d(output1)
                if rand[num][1] <= 6:
                    func_3d(output2)
                else:
                    func_3a(output2)
        elif tmp == [1,0,0]:
            if rand[num][0] <= 2:
                func_3a(output1)
                if rand[num][1] <= 3:
                    func_1a(output2)
                elif rand[num][1] <= 7:
                    func_2b(output2)
                else:
                    func_2c(output2)
            elif rand[num][0] <= 5:
                func_3b(output1)
                if rand[num][1] <= 3:
                    func_1b(output2)
                elif rand[num][1] <= 7:
                    func_2c(output2)
                else:
                    func_2d(output2)
            elif rand[num][0] <= 8:
                func_3c(output1)
                if rand[num][1] <= 3:
                    func_1a(output2)
                elif rand[num][1] <= 7:
                    func_2d(output2)
                else:
                    func_2a(output2)
            else:
                func_3d(output1)
                if rand[num][1] <= 3:
                    func_1b(output2)
                elif rand[num][1] <= 7:
                    func_2a(output2)
                else:
                    func_2b(output2)
        elif tmp == [1,0,1]:
            if rand[num][0] <= 2:
                func_3a(output1)
                if rand[num][1] <= 3:
                    func_1b(output2)
                elif rand[num][1] <= 7:
                    func_2d(output2)
                else:
                    func_2a(output2)
            elif rand[num][0] <= 5:
                func_3b(output1)
                if rand[num][1] <= 3:
                    func_1a(output2)
                elif rand[num][1] <= 7:
                    func_2a(output2)
                else:
                    func_2b(output2)
            elif rand[num][0] <= 8:
                func_3c(output1)
                if rand[num][1] <= 3:
                    func_1b(output2)
                elif rand[num][1] <= 7:
                    func_2b(output2)
                else:
                    func_2c(output2)
            else:
                func_3d(output1)
                if rand[num][1] <= 3:
                    func_1a(output2)
                elif rand[num][1] <= 7:
                    func_2c(output2)
                else:
                    func_2a(output2)
        elif tmp == [1,1,0]:
            if rand[num][0] <= 2:
                func_3a(output1)
                func_3a(output2)
            elif rand[num][0] <= 5:
                func_3b(output1)
                func_3b(output2)
            elif rand[num][0] <= 8:
                func_3c(output1)
                func_3c(output2)
            else:
                func_3d(output1)
                func_3d(output2)
        elif tmp == [1,1,1]:
            if rand[num][0] <= 2:
                func_3a(output1)
                if rand[num][1] <= 3:
                    func_2d(output2)
                elif rand[num][1] <= 7:
                    func_2b(output2)
                else:
                    func_2c(output2)
            elif rand[num][0] <= 5:
                func_3b(output1)
                if rand[num][1] <= 3:
                    func_2a(output2)
                elif rand[num][1] <= 7:
                    func_2c(output2)
                else:
                    func_2d(output2)
            elif rand[num][0] <= 8:
                func_3c(output1)
                if rand[num][1] <= 3:
                    func_2b(output2)
                elif rand[num][1] <= 7:
                    func_2d(output2)
                else:
                    func_2a(output2)
            else:
                func_3d(output1)
                if rand[num][1] <= 3:
                    func_2c(output2)
                elif rand[num][1] <= 7:
                    func_2a(output2)
                else:
                    func_2b(output2)
        else:
            pass
        num+=1

# print(num)

print(output1)
output1.show()
output1.save('output1.bmp')
output2.show()
output2.save('output2.bmp')
