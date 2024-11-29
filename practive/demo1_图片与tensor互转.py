import cv2
# from PIL import Image
import PIL.Image as Image
import numpy as np
import torch.nn as nn
import torch
import torchvision.transforms as transforms
crop = transforms.Compose([
    transforms.CenterCrop((80, 80)),
    # transforms.ToTensor()
])
tensor_  = transforms.Compose([
    transforms.CenterCrop((40, 40)),
    transforms.ToTensor(),
    transforms.ToPILImage()
])


im_path = '1babecf8-a242-4b00-857b-7a2c64fded1a_0002.jpg'
im_PIL = Image.open(im_path)
print(im_PIL.size)
print(type(im_PIL))
crop_im = crop(im_PIL)
print(crop_im.convert('RGB').load()[0,0])
print(type(crop_im))
tensor_im = tensor_(im_PIL)
print(tensor_im.load()[0, 0])
data = np.random.randint(0, 255, size=27) 

# data = data/ 255.0
print(data[0])
img = data.reshape(3,3,3)
img =  img.astype(np.float32)
print(img)
# img = img/ 255.0

imgPIL = transforms.ToPILImage()(img)
print(imgPIL.load()[0,0])
"""(383, 480)
<class 'PIL.JpegImagePlugin.JpegImageFile'>
<class 'PIL.Image.Image'>
没有ToTensor，还是PIL类型"""
exit()

im = cv2.imread(im_path)
print(im.shape)
print(type(im))

#PIL转数组
im_cv = np.array(im_PIL)
print(im_cv.shape)
# cv2.imshow('', cv2.cvtColor(im_cv, cv2.COLOR_RGB2BGR))
# cv2.waitKey(0)


# 数组转PIL
im_cv = im
im_PIL = Image.fromarray(cv2.cvtColor(im_cv, cv2.COLOR_BGR2RGB))
# im_PIL.show()

# tensor 转 PIL. 会自动转换c w h 顺序
tensor_a = torch.randn((3,40,40))
print(',',tensor_a.shape)
a = transforms.ToPILImage()
a_PIL = a(tensor_a)
print(a_PIL.size)
print(type(a_PIL))
# a_PIL.show()


#tensor 转 数组， 不会转换cwh顺序
a_arr = tensor_a.numpy()
print(type(a_arr), a_arr.shape)
a_arr = np.transpose(a_arr, (1,2,0))
print(a_arr.shape)
# cv2.imshow('', a_arr[:,:,::-1])  # 这样仅仅是翻转最后一个维度。类似rgb转bgr操作
# cv2.imshow('', a_arr)
# cv2.waitKey(0)

# tensor转数组，使用PIL做中转
tensor_b = tensor_a
a = transforms.ToPILImage()
a_PIL = a(tensor_a)
a_arr = np.array(a_PIL)
# cv2.imshow('', cv2.cvtColor(a_arr, cv2.COLOR_RGB2BGR))
# cv2.waitKey(0)

# cv2转tensor， 再转PIL
im = cv2.imread(im_path)
im_chw = np.transpose(im, (2, 0, 1))
print(im_chw.shape)
im_chw = im_chw[::-1, :, :].copy()
im_tensor = torch.from_numpy(im_chw)
print(im_tensor.shape)
a = transforms.ToPILImage()
im_PIL = a(im_tensor)
print(im_PIL.size)
# im_PIL.show()
'''注意点：numpy和tensor互转时，没有自动转换顺序，需要手动来改变顺序。而且PIL和cv之间注意rgb通道顺序 '''


print("----"*50)


### str、bytes、BytesIO、Image的相互转换
import base64
from io import BytesIO

# Image 转 str
img_PIL = Image.open(im_path)

# 创建一个字节流管道
imgByteArr = BytesIO()

# 将图片数据存入字节流管道，format可以按照具体文件格式填写  
img_PIL.save(imgByteArr, format='png') 

# 从字节流管道中获取二进制
img_bytes = imgByteArr.getvalue()
print(img_bytes[-4:]) # b'\xaeB`\x82'

# bytes 转str
string = base64.b64encode(img_bytes).decode('utf8')  # QmCC
print(string[-4:])  # 打印结果为一些字母和数字组成的二进制文件。
print(base64.b64encode(img_bytes)[-4:])  # b'QmCC'  与上一行的区别就是多了一个b
print(base64.b64decode(string)[-4:])
# img_PIL.save('a_pIL_75.jpg')

'''
Base64是一种编码方法，用于将二进制数据转换成由64个可打印字符组成的文本字符串。这种编码通常用于在不支持二进制数据的系统间传输数据，例如在电子邮件、网页、XML和JSON中嵌入图像或其他二进制文件。

Base64编码的工作原理是将每3个字节的二进制数据（24位）转换成4个6位的组，每个6位组对应于Base64编码表中的一个字符。如果原始数据的字节数不是3的倍数，会用一个或两个=字符来填充结果，以确保输出是4的倍数。

Base64编码表通常包含字母A-Z、a-z、数字0-9，以及两个符号+和/。在某些情况下，特别是在URL和文件名中，+可能被-替换，/可能被_替换，以避免混淆。

例如，ASCII字符串"Man"的Base64编码如下：

将"Man"转换为二进制：0100 1101 0110 1001
将二进制数据分成每组6位：0100 110 10110 1001
填充最后一组以使其成为6位：0100 110 10110 1001 (在最后添加两个0使其成为0100 110 101101 001)
将每组6位转换为对应的Base64字符：TWFu
因此，"Man"的Base64编码是"TWFu"。

Base64编码不是用于数据压缩的，实际上，由于它将3个字节的数据转换成4个字符，编码后的数据通常比原始数据更大。它主要用于确保数据在各种系统和网络中安全传输，而不改变数据的内容。
'''
