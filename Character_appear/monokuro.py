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
# print(input1_pixels[70,70])


for y in range(height):
    for x in range(width):
        # print(input1_pixels[x][y])
        if all(input1_pixels[x,y] == [0, 0, 0]):
            # 0
            if all(input2_pixels[x,y] == [0, 0, 0]):
                # 0
                if all(input3_pixels[x,y] == [0, 0, 0]):
                    # [0,0,0]
                    output1.putpixel((x*2,y*2), (0,0,0))
                    output1.putpixel((x*2+1,y*2), (0,0,0))
                    output1.putpixel((x*2,y*2+1), (255,255,255))
                    output1.putpixel((x*2+1,y*2+1), (255,255,255))

                    output2.putpixel((x*2,y*2), (0,0,0))
                    output2.putpixel((x*2+1,y*2), (255,255,255))
                    output2.putpixel((x*2,y*2+1), (0,0,0))
                    output2.putpixel((x*2+1,y*2+1), (255,255,255))
                else:
                    # [0,0,1]
                    output1.putpixel((x*2,y*2), (0,0,0))
                    output1.putpixel((x*2+1,y*2), (0,0,0))
                    output1.putpixel((x*2,y*2+1), (255,255,255))
                    output1.putpixel((x*2+1,y*2+1), (255,255,255))

                    output2.putpixel((x*2,y*2), (255,255,255))
                    output2.putpixel((x*2+1,y*2), (255,255,255))
                    output2.putpixel((x*2,y*2+1), (0,0,0))
                    output2.putpixel((x*2+1,y*2+1), (0,0,0))
            else:
                # [0,1,0]
                if all(input3_pixels[x,y] == [0, 0, 0]):
                    output1.putpixel((x*2,y*2), (0,0,0))
                    output1.putpixel((x*2+1,y*2), (0,0,0))
                    output1.putpixel((x*2,y*2+1), (255,255,255))
                    output1.putpixel((x*2+1,y*2+1), (255,255,255))

                    output2.putpixel((x*2,y*2), (0,0,0))
                    output2.putpixel((x*2+1,y*2), (255,255,255))
                    output2.putpixel((x*2,y*2+1), (255,255,255))
                    output2.putpixel((x*2+1,y*2+1), (255,255,255))
                    # [0,1,1]
                else:
                    output1.putpixel((x*2,y*2), (0,0,0))
                    output1.putpixel((x*2+1,y*2), (0,0,0))
                    output1.putpixel((x*2,y*2+1), (255,255,255))
                    output1.putpixel((x*2+1,y*2+1), (255,255,255))

                    output2.putpixel((x*2,y*2), (255,255,255))
                    output2.putpixel((x*2+1,y*2), (255,255,255))
                    output2.putpixel((x*2,y*2+1), (0,0,0))
                    output2.putpixel((x*2+1,y*2+1), (255,255,255))
        else:
            # 0
            if all(input2_pixels[x,y] == [0, 0, 0]):
                # 0
                if all(input3_pixels[x,y] == [0, 0, 0]):
                    # [1,0,0]
                    output1.putpixel((x*2,y*2), (0,0,0))
                    output1.putpixel((x*2+1,y*2), (255,255,255))
                    output1.putpixel((x*2,y*2+1), (255,255,255))
                    output1.putpixel((x*2+1,y*2+1), (255,255,255))

                    output2.putpixel((x*2,y*2), (0,0,0))
                    output2.putpixel((x*2+1,y*2), (255,255,255))
                    output2.putpixel((x*2,y*2+1), (0,0,0))
                    output2.putpixel((x*2+1,y*2+1), (255,255,255))
                else:
                    # [1,0,1]
                    output1.putpixel((x*2,y*2), (0,0,0))
                    output1.putpixel((x*2+1,y*2), (255,255,255))
                    output1.putpixel((x*2,y*2+1), (255,255,255))
                    output1.putpixel((x*2+1,y*2+1), (255,255,255))

                    output2.putpixel((x*2,y*2), (255,255,255))
                    output2.putpixel((x*2+1,y*2), (255,255,255))
                    output2.putpixel((x*2,y*2+1), (0,0,0))
                    output2.putpixel((x*2+1,y*2+1), (0,0,0))
            else:
                # [1,1,0]
                if all(input3_pixels[x,y] == [0, 0, 0]):
                    output1.putpixel((x*2,y*2), (0,0,0))
                    output1.putpixel((x*2+1,y*2), (255,255,255))
                    output1.putpixel((x*2,y*2+1), (255,255,255))
                    output1.putpixel((x*2+1,y*2+1), (255,255,255))

                    output2.putpixel((x*2,y*2), (0,0,0))
                    output2.putpixel((x*2+1,y*2), (255,255,255))
                    output2.putpixel((x*2,y*2+1), (255,255,255))
                    output2.putpixel((x*2+1,y*2+1), (255,255,255))
                    # [1,1,1]
                else:
                    output1.putpixel((x*2,y*2), (0,0,0))
                    output1.putpixel((x*2+1,y*2), (255,255,255))
                    output1.putpixel((x*2,y*2+1), (255,255,255))
                    output1.putpixel((x*2+1,y*2+1), (255,255,255))

                    output2.putpixel((x*2,y*2), (255,255,255))
                    output2.putpixel((x*2+1,y*2), (255,255,255))
                    output2.putpixel((x*2,y*2+1), (0,0,0))
                    output2.putpixel((x*2+1,y*2+1), (255,255,255))

output1.show()
output1.save('output1.bmp')
output2.show()
output2.save('output2.bmp')

# 以下img_pixelsからデータを受け取る 仕様↓
# img_pixels[width][height]
# => array([r,g,b])

# ピクセルのセット
# img2.putpixel((width, height), (r,g,b))

# 画像の表示
# img2.show()


# 画像の保存
# img2.save('gazoumei.jpg')

# pixelの取得
# (heightは上から)
# img.getpixel((width,height))
