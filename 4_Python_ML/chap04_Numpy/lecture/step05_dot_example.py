# -*- coding: utf-8 -*-
"""
신경망에서 행렬곱 적용 예
 - 은닉층(h) = [입력(X) * 가중치(w)] + 편향(b)
"""
import numpy as np
# 1. ANN model
# input : image(28x28), hidden node : 32개 -> weight는 [?,?]

# 2. input data 생성(이미지)
x_img = np.random.randint(0,256, size=(28*28))
x_img.shape # (784,) 1차원
x_img.max() # 255

# 정규화 : 0 ~ 1 
x_img = x_img / 255
x_img.max() # 1.0
x_img2d = x_img.reshape(28,28)
x_img2d.shape # (28, 28) 요기에 w를 곱하니 32개의 h가 나와야 함 : w=(28,32)

# 3. weight data
weight = np.random.randn(28,32)
weight
weight.shape # (28, 32)

# 4. hidden layer
hidden = np.dot(x_img2d, weight)
hidden
hidden.shape # h(28, 32) = x(28,28) * w(28,32)
             # h(관측치, 연산값)

































