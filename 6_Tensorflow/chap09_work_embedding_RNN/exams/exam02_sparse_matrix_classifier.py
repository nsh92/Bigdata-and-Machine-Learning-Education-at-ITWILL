"""
 문) newsgroups 데이터셋을 대상으로 5개 뉴스 그룹만 선택하여 희소행렬을 
     생성한 후 DNN model을 생성하시오.
     조건1> 전체 단어 중 40,000개를 선택하여 x_train을 대상으로 
            tfidf 방식의 희소행렬 만들기(x_test는 작성되었음) 
     조건2> DNN layer
        hidden layer1 : [4000, 126]
        hidden layer2 : [126, 64] 
        hidden layer3 : [64, 32] 
        output layer : [32, 5]
     조건3> 과적합(overfitting)을 고려한 Dropout 적용 
     조건4> model compile : optimizer='rmsprop'
     조건5> model training : epochs=10,  batch_size=400
     조건6> model validation : score, accuracy 적용  
"""
from sklearn.datasets import fetch_20newsgroups # news 데이터셋 
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Embedding, LSTM, Dropout
import time

start_time = time.time() 

# 1. hyper parameters
num_words = 40000 


# 2. news dataset 가져오기 
newsgroups = fetch_20newsgroups(subset='all') # train/test load 
#print(newsgroups.target_names)
#print(len(newsgroups.target_names)) # 20개 뉴스 그룹 

# 1) train set : 5개 뉴스 그룹 선택   
cats = list(newsgroups.target_names)[:5]
news_train = fetch_20newsgroups(subset='train',categories=cats)
x_train = news_train.data # texts
y_train = news_train.target # 0 ~ 3
len(x_train) # 뉴스 text : 2823
y_train # [4, 2, 3, ..., 4, 1, 2] - integer

# <조건1> train set sparse matrix 생성 
tokenizer = Tokenizer(num_words = num_words)
tokenizer.fit_on_texts(x_train)
token = tokenizer.word_index
print("전체 단어 수 = ", len(token))
x_data = tokenizer.texts_to_matrix(x_train, mode='tfidf')
x_data.shape

# 2) test set dataset 5개 뉴스그룹 대상 : 희소행렬
news_test = fetch_20newsgroups(subset='test', categories=cats)
x_val = news_test.data # texts
x_val = text_prepro(x_val)
y_val = news_test.target # 0 ~ 4

# test set sparse matrix 생성
sparse_test = tokenizer.texts_to_matrix(texts=x_val, mode='tfidf')
print(sparse_test.shape) # (1879, 40000)



# 드랍아웃은 대충 차원이 높을수록 높이는 것이 권장됨
# 3. <조건2><조건3> model layer 
input_shape = (40000, )
model = Sequential()
model.add(Dense(126, input_shape = input_shape, activation="relu"))
Dropout(0.3)
model.add(Dense(64, activation="relu"))
Dropout(0.2)
model.add(Dense(32, activation="relu"))
Dropout(0.1)
model.add(Dense(5, activation="softmax"))

model.summary()

# 4. <조건4><조건5> model 생성과 평가 
model.compile(optimizer = 'rmsprop', loss = 'sparse_categorical_crossentropy', metrics = ['sparse_categorical_accuracy']) 
model.fit(x_data, y_train, batch_size = 400, epochs = 10, validation_data = (sparse_test, y_val))

# 5. <조건6>> model 평가 
loss, score = model.evaluate(sparse_test, y_val)
# loss: 0.4110 - sparse_categorical_accuracy: 0.8233