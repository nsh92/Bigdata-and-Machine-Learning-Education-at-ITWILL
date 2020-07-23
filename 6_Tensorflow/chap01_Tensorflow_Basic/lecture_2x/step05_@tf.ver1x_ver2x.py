# -*- coding: utf-8 -*-
'''lecture_x1_step08 -> ver2
1. 즉시 실행 모드
2. 세션 대신 함수
3. @tf.function 함수 장식자'''

import tensorflow as tf
import pandas as pd
from sklearn.model_selection import train_test_split

iris = pd.read_csv("C:/ITWILL/6_Tensorflow/data/iris.csv")
iris.info()

cols = list(iris.columns)
x_data = iris[cols[:4]]
y_data = iris[cols[-1]]
x_data.shape
y_data.shape





















