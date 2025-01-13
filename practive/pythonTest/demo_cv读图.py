import cv2
import numpy as np
im_bgr = cv2.imread('1.jpg')
# print(im.shape)
im_rgb = cv2.cvtColor(im_bgr, cv2.COLOR_BGR2RGB)
img = cv2.cvtColor(im_rgb, cv2.COLOR_BGR2RGB)
# print(np.equal(im_bgr, img))
assert np.array_equal(im_bgr, img), 'the imagea are not equal'
assert np.equal(im_bgr, img).any(), 'the imagea are not equal'
cv2.imshow('', img)
cv2.waitKey(0)