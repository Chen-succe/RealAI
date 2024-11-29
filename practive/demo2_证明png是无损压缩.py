import cv2

path = '1babecf8-a242-4b00-857b-7a2c64fded1a_0002.jpg'
im = cv2.imread(path)
cv2.imwrite('11.png', im, [cv2.IMWRITE_PNG_COMPRESSION,1])
cv2.imwrite('12.png', im, [cv2.IMWRITE_PNG_COMPRESSION,2])
cv2.imwrite('13.png', im, [cv2.IMWRITE_PNG_COMPRESSION,3])
cv2.imwrite('14.png', im, [cv2.IMWRITE_PNG_COMPRESSION,4])
cv2.imwrite('15.png', im, [cv2.IMWRITE_PNG_COMPRESSION,5])
cv2.imwrite('16.png', im, [cv2.IMWRITE_PNG_COMPRESSION,6])