# -*- coding: utf-8 -*-
"""
reshape vs resize
 - reshape : 모양 변경
 - resize : 크기 변경
   ex) 다양한 크기의 images -> 120*150 규격화 -> 모델에 집어넣기 전에 필수적 전처리
"""
import numpy as np
from glob import glob # 파일을 검색해주는 모듈(문자열 경로, *.jpg)
from PIL import Image # 이미지 파일 읽기 파이썬 이미지 라이브러리
import matplotlib.pyplot as plt

# 1개 이미지 열기 (먼저 workspace를 현재 경로로 설정)
path = "./chap04_Numpy"
file = path +  "/images/test1.jpg"
img = Image.open(file)
type(img) # PIL.JpegImagePlugin.JpegImageFile
img.shape # 오류 : 넘파이 객체가 아니니 행렬도 아니지 그러니 이를 바꿔야지

np.shape(img) # (360, 540, 3) 이러니까 되내
# 이 걸 120 150 3 으로 변경하고싶다 : resize
plt.imshow(img)

# PIL의 멤버 : 값은 튜플로 넣어야 : 원래 그림은 (h, w, c)인데, resize는 (w, h, c)로 인식함
img_re = img.resize((150, 120))
np.shape(img_re) # (120, 150, 3)
plt.imshow(img_re)

# PIL -> 넘파이
type(img) # PIL객체
img_arr = np.asarray(img)
type(img_arr) # numpy.ndarray
img_arr.shape # (360, 540, 3)

# 어떤 디렉토리에 다수의 이미지가 있을 때 이를 일정하게 업로드하는 방법
def imageResize():
    img_h = 120 # 세로픽셀
    img_w = 150 # 가로픽셀
    image_resize  = [] # 규격화된 이미지 적재

    # glob : file 패턴
    for file in glob(path + '/images/' + '*.jpg'):
        # test1.jpg -> test2.jpg, ...
        img = Image.open(file) # image file read
        print(np.shape(img)) # resize 전 확인
        
        # PIL -> resize
        img = img.resize((img_w, img_h))
        # PIL -> numpy
        img_data = np.asarray(img)
        
        # resize image save
        image_resize.append(img_data)
        print(file, ':', img_data.shape)

    return np.array(image_resize) # 리스트를 어레이로


image_resize = imageResize()
image_resize.shape
image_resize[0].shape
image_resize[1].shape

plt.imshow(image_resize[0])
plt.imshow(image_resize[1])
















