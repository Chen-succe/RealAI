from PIL import Image
import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib as mlb

mlb.use("TkAgg")
# path = r'./20210301002356-2021_83_46_56EF3FE1-6DAA-1850-85F8-7FBBE20CF5B0-124_8839C427-5E67-4223-140C-A19C51B22EBB.jpg'
path = r'./1babecf8-a242-4b00-857b-7a2c64fded1a_0002.jpg'
im = Image.open(path)
im_resize = im.resize((200, 300))
print(im_resize.size)
print(np.array(im_resize).shape)
cv2.imshow('', np.array(im_resize))
cv2.waitKey(0)
print(im)
print(im.size)  # (w, h)
im_array = np.array(im)  # (h, w)
print(im_array.shape)  # (334, 334, 3)
# Image._show(im)
cv2.imshow('', im_array)
cv2.waitKey(0)
# im_new = np.transpose(im_array, (2, 0, 1))
plt.imshow(im_array)
plt.show()

# (h, w, c)
im_cv = cv2.imread(path)
print(im_cv.shape)  # (h, w, c)

im_plt = plt.imread(path)
print(im_plt.shape)
