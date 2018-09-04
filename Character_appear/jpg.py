# coding: utf-
from PIL import Image
import numpy as np

# 元となる画像の読み込み
input1 = Image.open('original1.jpg')
input2 = Image.open('original2.jpg')
#オリジナル画像の幅と高さを取得
width, height = img.size
# オリジナル画像と同じサイズのImageオブジェクトを作成する
output = Image.new('RGB', (width, height))
# 画像を配列に変換
img_pixels = []
for y in range(height):
  for x in range(width):
    # getpixel((x,y))で左からx番目,上からy番目のピクセルの色を取得し、img_pixelsに追加する
    img_pixels.append(img.getpixel((x,y)))
# あとで計算しやすいようにnumpyのarrayに変換しておく
img_pixels = np.array(img_pixels)
# 終了

# 以下img_pixelsからデータを受け取る 仕様↓
# img_pixels[width][height]
# => array([r,g,b])

# 画像の表示
# img2.show()

# ピクセルのセット
# img2.putpixel((width, height), (r,g,b))

# 画像の保存
# img2.save('gazoumei.jpg')

# pixelの取得
# (heightは上から)
# img.getpixel((width,height))
