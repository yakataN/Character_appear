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
def func_1a(self):
    self.putpixel((x*2,y*2),(0,0,0))
    self.putpixel((x*2+1,y*2),(255,255,255))
    self.putpixel((x*2,y*2+1),(255,255,255))
    self.putpixel((x*2+1,y*2+1),(0,0,0))

def func_1b(output):
    output.putpixel((x*2,y*2),(255,255,255))
    output.putpixel((x*2+1,y*2),(0,0,0))
    output.putpixel((x*2,y*2+1),(0,0,0))
    output.putpixel((x*2+1,y*2+1),(255,255,255))

def func_2a(output):
    output.putpixel((x*2,y*2),(255,255,255))
    output.putpixel((x*2+1,y*2),(255,255,255))
    output.putpixel((x*2,y*2+1),(0,0,0))
    output.putpixel((x*2+1,y*2+1),(0,0,0))

def func_2b(output):
    output.putpixel((x*2,y*2),(0,0,0))
    output.putpixel((x*2,y*2+1),(255,255,255))
    output.putpixel((x*2+1,y*2),(0,0,0))
    output.putpixel((x*2+1,y*2+1),(255,255,255))

def func_2c(output):
    output.putpixel((x*2,y*2),(0,0,0))
    output.putpixel((x*2,y*2+1),(0,0,0))
    output.putpixel((x*2+1,y*2),(255,255,255))
    output.putpixel((x*2+1,y*2+1),(255,255,255))

def func_2d(output):
    output.putpixel((x*2,y*2),(255,255,255))
    output.putpixel((x*2,y*2+1),(0,0,0))
    output.putpixel((x*2+1,y*2),(255,255,255))
    output.putpixel((x*2+1,y*2+1),(0,0,0))

def func_3a(output):
    output.putpixel((x*2+1,y*2),(0,0,0))
    output.putpixel((x*2,y*2+1),(255,255,255))
    output.putpixel((x*2,y*2),(255,255,255))
    output.putpixel((x*2+1,y*2+1),(255,255,255))

def func_2b(output):
    output.putpixel((x*2,y*2),(255,255,255))
    output.putpixel((x*2,y*2+1),(0,0,0))
    output.putpixel((x*2+1,y*2),(255,255,255))
    output.putpixel((x*2+1,y*2+1),(255,255,255))

def func_2c(output):
    output.putpixel((x*2,y*2),(255,255,255))
    output.putpixel((x*2,y*2+1),(255,255,255))
    output.putpixel((x*2+1,y*2),(255,255,255))
    output.putpixel((x*2+1,y*2+1),(0,0,0))

def func_2d(output):
    output.putpixel((x*2,y*2),(255,255,255))
    output.putpixel((x*2,y*2+1),(255,255,255))
    output.putpixel((x*2+1,y*2),(0,0,0))
    output.putpixel((x*2+1,y*2+1),(255,255,255))

for y in range(height):
    for x in range(width):
        # output1用とoutput2用の乱数の生成
        rand = np.random.randint(0,12,2)
        # 場合分け
        tmp = []
        if all(input1_pixels[x,y] == [0,0,0]):
            tmp.append(0)
        else:
            tmp.append(1)
        if all(input2_pixels[x,y] == [0,0,0]):
            tmp.append(0)
        else:
            tmp.append(1)
        if all(input3_pixels[x,y] == [0,0,0]):
            tmp.append(0)
        else:
            tmp.append(1)
        # 場合分け終了　情報を3桁の配列に格納
        # outputにpixelを埋め込む
        if all(tmp) == [0,0,0]:
            if rand[0] == 0 or 1:
                output1.func_1a()
                if rand[1] == 0 or 1 or 2:
                    func_2a(output2)
                elif rand[1] == 3 or 4 or 5:
                    func_2b(output2)
                elif rand[1] == 6 or 7 or 8:
                    func_2c(output2)
                elif rand[1] == 9 or 10 or 11:
                    func_2d(output2)
            elif rand[0] == 2 or 3:
                func_1b(output1)
                if rand[1] == 0 or 1 or 2:
                    func_2a(output2)
                elif rand[1] == 3 or 4 or 5:
                    func_2b(output2)
                elif rand[1] == 6 or 7 or 8:
                    func_2c(output2)
                elif rand[1] == 9 or 10 or 11:
                    func_2d(output2)
            elif rand[0] == 4 or 5:
                func_2a(output1)
                if rand[1] == 0 or 1 or 2:
                    output2.func_1a
                elif rand[1] == 3 or 4 or 5:
                    func_1b(output2)
                elif rand[1] == 6 or 7 or 8:
                    func_2b(output2)
                elif rand[1] == 9 or 10 or 11:
                    func_2d(output2)
            elif rand[0] == 6 or 7:
                func_2b(output1)
                if rand[1] == 0 or 1 or 2:
                    output2.func_1a
                elif rand[1] == 3 or 4 or 5:
                    func_1b(output2)
                elif rand[1] == 6 or 7 or 8:
                    func_2c(output2)
                elif rand[1] == 9 or 10 or 11:
                    func_2a(output2)
            elif rand[0] == 8 or 9:
                func_2c(output1)
                if rand[1] == 0 or 1 or 2:
                    output2.func_1a
                elif rand[1] == 3 or 4 or 5:
                    func_1b(output2)
                elif rand[1] == 6 or 7 or 8:
                    func_2d(output2)
                elif rand[1] == 9 or 10 or 11:
                    func_2b(output2)
            elif rand[0] == 10 or 11:
                func_2d(output1)
                if rand[1] == 0 or 1 or 2:
                    output2.func_1a
                elif rand[1] == 3 or 4 or 5:
                    func_1b(output2)
                elif rand[1] == 6 or 7 or 8:
                    func_2a(output2)
                elif rand[1] == 9 or 10 or 11:
                    func_2c(output2)

        if all(tmp) == [0,0,1]:
            if rand[0] == 0 or 1:
                output1.func_1a
                func_1b(output2)
            elif rand[0] == 2 or 3:
                func_1b(output1)
                output2.func_1a
            elif rand[0] == 4 or 5:
                func_2a(output1)
                func_2c(output2)
            elif rand[0] == 6 or 7:
                func_2b(output1)
                func_2d(output2)
            elif rand[0] == 8 or 9:
                func_2c(output1)
                func_2a(output2)
            elif rand[0] == 10 or 11:
                func_2d(output1)
                func_2b(output2)

        if all(tmp) == [0,1,0]:
            if rand[0] == 0 or 1:
                output1.func_1a
                if rand[1] <= 6:
                    func_3a
                else:
                    func_3c
            elif rand[0] == 2 or 3:
                func_1b(output1)
                if rand[1] <= 6:
                    func_3b
                else:
                    func_3d
            elif rand[0] == 4 or 5:
                func_2a(output1)
                if rand[1] <= 6:
                    func_3c
                else:
                    func_3d
            elif rand[0] == 6 or 7:
                func_2b(output1)
                if rand[1] <= 6:
                    func_3d
                else:
                    func_3a
            elif rand[0] == 8 or 9:
                func_2c(output1)
                if rand[1] <= 6:
                    func_3a
                else:
                    func_3b
            elif rand[0] == 10 or 11:
                func_2d(output1)
                if rand[1] <= 6:
                    func_3b
                else:
                    func_3c

        if all(tmp) == [0,1,1]:
            if rand[0] == 0 or 1:
                output1.func_1a
                if rand[1] <= 6:
                    func_3b
                else:
                    func_3d
            elif rand[0] == 2 or 3:
                func_1b(output1)
                if rand[1] <= 6:
                    func_3a
                else:
                    func_3c
            elif rand[0] == 4 or 5:
                func_2a(output1)
                if rand[1] <= 6:
                    func_3a
                else:
                    func_3b
            elif rand[0] == 6 or 7:
                func_2b(output1)
                if rand[1] <= 6:
                    func_3b
                else:
                    func_3c
            elif rand[0] == 8 or 9:
                func_2c(output1)
                if rand[1] <= 6:
                    func_3c
                else:
                    func_3d
            elif rand[0] == 10 or 11:
                func_2d(output1)
                if rand[1] <= 6:
                    func_3d
                else:
                    func_3a

        if all(tmp) == [1,0,0]:
            if rand[0] <= 2:
                func_3a(output1)
                if rand[1] <= 3:
                    func_1a
                elif rand[1] <= 7:
                    func_2b
                else:
                    func_2c
            elif rand[0] <= 5:
                func_3b(output1)
                if rand[1] <= 3:
                    func_1b
                elif rand[1] <= 7:
                    func_2c
                else:
                    func_2d
            elif rand[0] <= 8:
                func_3c(output1)
                if rand[1] <= 3:
                    func_1a
                elif rand[1] <= 7:
                    func_2d
                else:
                    func_2a
            elif rand[0] <= 11:
                func_3d(output1)
                if rand[1] <= 3:
                    func_1b
                elif rand[1] <= 7:
                    func_2a
                else:
                    func_2b

        if all(tmp) == [1,0,1]:
            if rand[0] <= 2:
                func_3a(output1)
                if rand[1] <= 3:
                    func_1b
                elif rand[1] <= 7:
                    func_2d
                else:
                    func_2a
            elif rand[0] <= 5:
                func_3b(output1)
                if rand[1] <= 3:
                    func_1a
                elif rand[1] <= 7:
                    func_2a
                else:
                    func_2b
            elif rand[0] <= 8:
                func_3c(output1)
                if rand[1] <= 3:
                    func_1b
                elif rand[1] <= 7:
                    func_2b
                else:
                    func_2c
            elif rand[0] <= 11:
                func_3d(output1)
                if rand[1] <= 3:
                    func_1a
                elif rand[1] <= 7:
                    func_2c
                else:
                    func_2a

        if all(tmp) == [1,1,0]:
            if rand[0] <= 2:
                func_3a(output1)
                func_3a(output2)
            elif rand[0] <= 5:
                func_3b(output1)
                func_3b(output2)
            elif rand[0] <= 8:
                func_3c(output1)
                func_3c(output2)
            elif rand[0] <= 11:
                func_3d(output1)
                func_3d(output2)

        if all(tmp) == [1,1,1]:
            if rand[0] <= 2:
                func_3a(output1)
                if rand[1] <= 3:
                    func_2d
                elif rand[1] <= 7:
                    func_2b
                else:
                    func_2c
            elif rand[0] <= 5:
                func_3b(output1)
                if rand[1] <= 3:
                    func_2a
                elif rand[1] <= 7:
                    func_2c
                else:
                    func_2d
            elif rand[0] <= 8:
                func_3c(output1)
                if rand[1] <= 3:
                    func_2b
                elif rand[1] <= 7:
                    func_2d
                else:
                    func_2a
            elif rand[0] <= 11:
                func_3d(output1)
                if rand[1] <= 3:
                    func_2c
                elif rand[1] <= 7:
                    func_2a
                else:
                    func_2b

print(output1)
output1.show()
output1.save('output1.bmp')
output2.show()
output2.save('output2.bmp')
