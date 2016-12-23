import matplotlib.pyplot as plt
from matplotlib.image import imread

img = imread('test.jpg')
# imreadはmatplotlib.imageモジュールのimread()
plt.imshow(img)
# imshow()はpyplotモジュールのメソッド
plt.show()
