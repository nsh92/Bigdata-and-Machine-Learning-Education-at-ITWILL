'''
분류용 dataset 정리 site
https://datascienceschool.net/view-notebook/577a01e24d4f456bb5060da6e47054e1/

sklearn dataset
'''
from sklearn import datasets # dataset 제공 library
import pandas as pd
import numpy as np
import seaborn as sn
import matplotlib.pyplot as plt

######################################
# 분류분석에 적합한 데이터셋
######################################

# 1. wine 
'''
와인의 화학 조성을 사용하여 와인의 종류를 예측하기 위한 데이터

•타겟 변수
◦와인의 종류 : 0, 1, 2 세가지 값 

•특징 변수 
◦알콜(Alcohol)
◦말산(Malic acid)
◦회분(Ash)
◦회분의 알칼리도(Alcalinity of ash) 
◦마그네슘(Magnesium)
◦총 폴리페놀(Total phenols)
◦플라보노이드 폴리페놀(Flavanoids)
◦비 플라보노이드 폴리페놀(Nonflavanoid phenols)
◦프로안토시아닌(Proanthocyanins)
◦색상의 강도(Color intensity)
◦색상(Hue)
◦희석 와인의 OD280/OD315 비율 (OD280/OD315 of diluted wines)
◦프롤린(Proline)
'''
from sklearn.datasets import load_wine
wine = load_wine()
print(list(wine.target_names)) # ['class_0', 'class_1', 'class_2']

wine_x, wine_y = load_wine(return_X_y=True)
print(type(wine_x)) # <class 'numpy.ndarray'>
print(np.shape(wine_x)) # (178, 13) : matrix
print(np.shape(wine_y)) # (178,) : vector

# numpy -> DataFrame 
wine_df = pd.DataFrame(wine_x, columns=wine.feature_names)
tg = pd.Series(wine_y, dtype="category")
tg = tg.cat.rename_categories(wine.target_names)
wine_df['class'] = tg
wine_df.tail()

# class별 주요변수 간 산점도 
sn.pairplot(vars=["alcohol", "alcalinity_of_ash", "total_phenols", "flavanoids"], 
             hue="class", data=wine_df)
plt.show()


# 2. breast cancer 데이터셋
'''
유방암(breast cancer) 진단 데이터 

•타겟 변수 
 - 종양이 양성(benign)인지 악성(malignant)인지를 판별
•특징 변수(30개) 
 - 유방암 진단 사진으로부터 측정한 종양(tumar)의 특징값
'''
cancer = datasets.load_breast_cancer()
print(cancer)
print(cancer.DESCR)

cancer_x = cancer.data
cancer_y = cancer.target
print(np.shape(cancer_x)) # (569, 30) : matrix
print(np.shape(cancer_y)) # (569,) : vector

cencar_df = pd.DataFrame(cancer_x, columns=cancer.feature_names)
tg = pd.Series(cancer_y, dtype="category")
tg = tg.cat.rename_categories(cancer.target_names)
cencar_df['class'] = tg
cencar_df.tail()

# 타겟 변수 기준 주요변수 간 산점도 
sn.pairplot(vars=["worst radius", "worst texture", "worst perimeter", "worst area"], 
             hue="class", data=cencar_df)
plt.show()


# 3. digits 데이터셋 - 숫자 예측(0~9)
'''
숫자 필기 이미지 데이터

•타겟 변수 
 - 0 ~ 9 : 10진수 정수 
•특징 변수(64픽셀 이미지 8*8) 
 -0부터 9까지의 숫자를 손으로 쓴 이미지 데이터
 -각 이미지는 0부터 15까지의 16개 명암을 가지는 8x8=64픽셀 해상도의 흑백 이미지
'''
digits = datasets.load_digits()
print(digits.DESCR)
'''
:Number of Instances: 5620
:Number of Attributes: 64
:Attribute Information: 8x8 image of integer pixels in the range 0..16.
'''
print(digits.data.shape)
print(digits.target.shape)
'''
(1797, 64)
(1797,)
'''
print(digits)
# 8x8 image of integer pixels in the range 0..16

np.random.seed(0)
N = 4 # 4행
M = 10 # 10열 
fig = plt.figure(figsize=(10, 5))
plt.subplots_adjust(top=1, bottom=0, hspace=0, wspace=0.05)
for i in range(N): # 4
    for j in range(M): # 10
        k = i*M+j
        ax = fig.add_subplot(N, M, k+1)
        ax.imshow(digits.images[k], cmap=plt.cm.bone, interpolation="none")
        ax.grid(False)
        ax.xaxis.set_ticks([])
        ax.yaxis.set_ticks([])
        plt.title(digits.target_names[digits.target[k]])
plt.tight_layout()
plt.show()

img2d = digits.data[0].reshape(8,8)
plt.imshow(img2d)
digits.target[0]


# 4. Covertype
'''
대표 수종 데이터

•타겟 변수 
 - 미국 삼림을 30×30m 영역으로 나누어 각 영역의 특징으로부터 대표적인 나무의 종(species)을 기록한 데이터
•특징 변수(30개) 
 - 특징 데이터가 54종류, 표본 데이터의 갯수가 581,012개

'''
from sklearn.datasets import fetch_covtype
import pandas as pd

covtype = fetch_covtype()
print(covtype.DESCR)
'''
=================   ============
Classes                        7
Samples total             581012
Dimensionality                54
Features                     int
=================   ============
'''

covtype_x = covtype.data 
covtype_y = covtype.target 

covtype_x.shape #  (581012, 54)
covtype_y.shape # (581012,)
covtype_x[0] # 1row 

# DataFrame의 특징 변수 지정 
covtype.data.shape[1] # 54
# x{:02d} : 숫자 오른쪽 기준(:)으로 2자리, 1자리이면 0으로 채움 : x01 ~ x54
columns=["x{:02d}".format(i + 1) for i in range(covtype.data.shape[1])]
columns

# X변수 칼럼명 지정 : x01 ~ x54
df = pd.DataFrame(covtype.data, 
                  columns=["x{:02d}".format(i + 1) for i in range(covtype.data.shape[1])],
                  dtype=float) 
# raw 자료형 2.596e+03 -> 자료형 정수 변환(2596) -> 실수형 변환(2596.0) 
df.head()

# Y변수 DataFrame에 추가 
cy = pd.Series(covtype.target, dtype="category")
df['Cover_Type'] = cy
df.head()
df.tail()
'''
           x01    x02   x03   x04   x05  ...  x51  x52  x53  x54  Cover_Type
581007  2396.0  153.0  20.0  85.0  17.0  ...  0.0  0.0  0.0  0.0           3
581008  2391.0  152.0  19.0  67.0  12.0  ...  0.0  0.0  0.0  0.0           3
581009  2386.0  159.0  17.0  60.0   7.0  ...  0.0  0.0  0.0  0.0           3
581010  2384.0  170.0  15.0  60.0   5.0  ...  0.0  0.0  0.0  0.0           3
581011  2383.0  165.0  13.0  60.0   4.0  ...  0.0  0.0  0.0  0.0           3
'''
df.info()

# raw data file save
df.to_csv('D:/MegaIT/Python_ML/chap05_Regression/data/covtype.csv', 
                    index=None, na_rep='NaN', encoding='utf-8')

df = pd.read_csv('D:/MegaIT/Python_ML/chap05_Regression/data/covtype.csv')
df.info()

# 특징 변수(1~10) + 타겟 변수 file save
col_names = list(df.columns)
cols = col_names[:10]
cols.append(col_names[-1])

# 타겟변수 : 1~3
covtype_df = df[cols]
covtype_df = covtype_df[covtype_df['Cover_Type']<= 3]
covtype_df.info()
covtype_df.to_csv('D:/MegaIT/Python_ML/chap05_Regression/data/covtype1to10_1to3.csv', 
                    index=None, na_rep='NaN', encoding='utf-8')

'''
각 특징 데이터가 가지는 값의 종류를 보면 1번부터 10번 특징은 실수값이고 
11번부터 54번 특징은 이진 카테고리값이라는 것을 알 수 있다.
'''
df.head()
# nunique() : 유일값 빈도수 
pd.DataFrame(df.nunique()).T
'''
    x01  x02  x03  x04  x05   x06  ...  x50  x51  x52  x53  x54  Cover_Type
0  1978  361   67  551  700  5785  ...    2    2    2    2    2           7
'''
df['x54'].value_counts() # 0.0, 1.0
df['x54'].unique()
df['x01'].nunique() # 1978



## 특징 변수 : 집단변수 변환(문자열 변수 -> 더미변수) 

# [0,1] -> 카테고리 형태로 변환 
df.iloc[:, 10:54] = df.iloc[:, 10:54].astype('category')
df.info()
# x54           581012 non-null category


# 피벗테이블 : 행(타겟변수), 열(x14), 셀(빈도수) 
df_count = df.pivot_table(index="Cover_Type", columns="x14", aggfunc="size")
df_count
'''
x14              0.0      1.0
Cover_Type                   
1           211840.0      NaN
2           280275.0   3026.0
3            14300.0  21454.0
4                NaN   2747.0
5             9493.0      NaN
6             7626.0   9741.0
7            20510.0      NaN
'''


'''
[해설]
타겟변수와 x14 변수의 교차분할표
 - x14변수의 category(0, 1)에 의해서 
    0번 : 1, 5, 7번 클래스 분류
    1번 : 4번 클래스 분류
'''

# 히트맵 시각화 
sn.heatmap(df_count, cmap=sn.light_palette("gray", as_cmap=True), annot=True, fmt="0")
plt.show()


# 5. news group 
'''
- 20개의 뉴스 그룹 문서 데이터(문서 분류 모델 예문으로 사용)

•타겟 변수 
◦문서가 속한 뉴스 그룹 : 20개 

•특징 변수 
◦문서 텍스트 : 18,846
'''

from sklearn.datasets import fetch_20newsgroups
newsgroups = fetch_20newsgroups(subset='all') # 'train', 'test'
# Downloading 20news dataset.

print(newsgroups.DESCR)
'''
**Data Set Characteristics:**

    =================   ==========
    Classes                     20
    Samples total            18846
    Dimensionality               1
    Features                  text
    =================   ==========
'''

# data vs target
newsgroups.data # text
len(newsgroups.data) # 18846

newsgroups.target # array([10,  3, 17, ...,  3,  1,  7])
len(newsgroups.target) # 18846

# 뉴스 그룹 : 20개 이름 
newsgroups.target_names # ['alt.atheism', ... 'talk.religion.misc']

# 1,2번째 뉴스 보기 
print(newsgroups.data[0])
print("=" * 50)
idx = newsgroups.target[0]
print(newsgroups.target_names[idx])
'''
==================================================
rec.sport.hockey
'''
print(newsgroups.data[1])
print("=" * 50)
idx = newsgroups.target[1]
print(newsgroups.target_names[idx]) # rec.sport.hockey
'''
==================================================
comp.sys.ibm.pc.hardware
'''

### 텍스트 벡터 변환 ###
'''
 텍스트 데이터로 예측모델 또는 군집 모델을 생성하기 위해서 먼저 텍스트를 
 적절한 숫자 값의 벡터로 만든다. 
'''
# train dataset 4개 뉴스그룹 대상 : 희소행렬  
from sklearn.feature_extraction.text import TfidfVectorizer
cats = ['alt.atheism', 'talk.religion.misc','comp.graphics', 'sci.space']
newsgroups_train = fetch_20newsgroups(subset='train',categories=cats)
vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform(newsgroups_train.data)
vectors.shape # (2034, 34118)


from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics

# NB 모델 생성 
clf = MultinomialNB(alpha=.01)
clf.fit(vectors, newsgroups_train.target) # 훈련셋 적용 


# test dataset 4개 뉴스그룹 대상 : 희소행렬
newsgroups_test = fetch_20newsgroups(subset='test', categories=cats)
vectors_test = vectorizer.transform(newsgroups_test.data)
vectors_test.shape # (1353, 34118)

# 모델 예측치
pred = clf.predict(vectors_test)

# 모델 평가 : average=[None, 'micro', 'macro', 'weighted'].
metrics.f1_score(newsgroups_test.target, pred, average='micro') 
# 0.893569844789357

# real value vs predict
newsgroups_test.target[:20]
pred[:20]
'''
array([2, 1, 1, 1, 1, 1, 2, 2, 0, 2, 1, 1, 1, 2, 1, 0, 0, 0, 1, 2]
array([2, 1, 2, 1, 1, 1, 2, 2, 0, 2, 1, 1, 1, 2, 1, 0, 0, 2, 1, 2]
'''



