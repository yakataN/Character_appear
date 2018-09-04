from PIL import Image
import numpy as np

img = Image.open('original.jpg')
width, height = img.size
filter_size = 20
img2 = Image.new('RGB', (width - filter_size, height - filter_size))
img_pixels = np.array([[img.getpixel((x,y)) for x in range(width)] for y in range(height)])

filter_size = 20

for y in range(height - filter_size):
  for x in range(width - filter_size):
    # 位置(x,y)を起点に縦横フィルターサイズの小さい画像をオリジナル画像から切り取る
    partial_img = img_pixels[y:y + filter_size, x:x + filter_size]
    # 小さい画像の各ピクセルの値を一列に並べる
    color_array = partial_img.reshape((filter_size+1) ** 2, 3)
    # 各R,G,Bそれぞれの平均を求めて加工後画像の位置(x,y)のピクセルの値にセットする
    mean_r, mean_g, mean_b = color_array.mean(axis = 0)
    img2.putpixel((x,y), (int(mean_r), int(mean_g), int(mean_b)))

img2.show()
img2.save('bokashi.jpg')
