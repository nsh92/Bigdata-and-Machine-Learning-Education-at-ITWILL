# xgboost vs randomForest
# - xgboost : boosting 방식 
# - randomForest : bagging 방식 

# 1. package install
install.packages("xgboost")
library(xgboost)
#library(help="xgboost")

# 2. dataset load/search
data(agaricus.train)
data(agaricus.test)

train <- agaricus.train
test <- agaricus.test

str(train)
train$data@Dim # x변수의 차원구조를 담고있음
# $ data : x변수 : [6513, 126] 2차원 Matrix
# $ label : y변수 : num [1:6513] 1차원의 벡터
train$data # 너무 많아서 ...이 보임
train$label
table(train$label) # 0과 1이 적당히 균등


str(test)
# 6513개 : 1611개 훈련 검정 배분


# 3. xgboost matrix 생성 : 객체 정보 확인  
# xgb.DMatrix(data = x, label = y)
dtrain <- xgb.DMatrix(data = train$data, label = train$label) # x:data, y:label
dtrain 
# dim: 6513 x 126 와꾸의 매트릭스가 만들어졌다 말고는 딱히 의미가 없음
# xgboost를 위한 객체만들기 용도

?xgboost
#We will train decision tree model using the following parameters:
# •objective = "binary:logistic": we will train a binary classification model ;
# "binary:logistic" : y변수 이항 
# •max_depth = 2: the trees won't be deep, because our case is very simple ;
# tree 구조가 간단한 경우 : 2
# •nthread = 2: the number of cpu threads we are going to use;
# cpu 사용 수 : 2
# •nrounds = 2: there will be two passes on the data, the second one will enhance the model by further reducing the difference between ground truth and prediction.
# 실제값과 예측값의 차이를 줄이기 위한 반복학습 횟수 
# •eta = 1 : eta control the learning rate  # 1에 가까울수록 빠르게
# 학습률을 제어하는 변수(Default: 0.3) 
# 숫자가 낮을 수록 모델의 복잡도가 높아지고, 컴퓨팅 파워가 더많이 소요
# 부스팅 과정을보다 일반화하여 오버 피팅을 방지하는 데 사용
# •verbose = 0 : no message
# 0이면 no message, 1이면 성능에 대한 정보 인쇄, 2이면 몇 가지 추가 정보 인쇄

# 4. model 생성 : xgboost matrix 객체 이용  
xgb_model <- xgboost(data = dtrain, max_depth = 2, eta = 1, nthread = 2, nrounds = 2, objective = "binary:logistic", verbose = 0)

# 5.  학습된 model의 변수(feature) 중요도/영향력 보기 
import <- xgb.importance(colnames(train$data), model = xgb_model)
import
# 가장 중요한 변수 top4개가 뜸 얘내 말고 다른 애들은 딱히 영향이 없더라
# Gain : 지니 계수

xgb.plot.importance(importance_matrix = import)

# 6. 예측치
pred <- predict(xgb_model, test$data)
range(pred) # 범주로 예측했나 확률로 예측했나 : 확률로 : 근대 y(label)는 범주지
y_pred <- ifelse(pred >= 0.5, 1, 0) # y에 맞는 범주로 넣어주기
y_true <- test$label

# 7. 모델 평가
# 7-1) 분류정확도
table(y_true) # 0과 1 비슷
tab <- table(y_true, y_pred)
acc <- (tab[1,1]+tab[2,2]) / length(y_true) # 97.8%
cat('분류정확도 =', acc)

# 7-2) 평균 오차
# T/F논리식을 숫자형으로 변환(1,0)
mean_arr <- mean(as.numeric(pred >= 0.5) != y_true) # != 같지 않다 # == 로 바꾸면 정확도로 바뀌지
cat('평균오차 =', mean_arr)
mean_arr1 <- mean(as.numeric(pred >= 0.5) == y_true)

# 8. model save & load
# 모델 ㅅㅌㅊ내
# 다음 번에도 쓰고 싶구만

# 8-1) model file save
setwd("c:/itwill/2_rwork/output")
xgb.save(xgb_model, 'xgboost.model') # (저장할 오브젝트, 파일명)
# TRUE 뜨면 저장댔음

rm(list = ls()) # 메모리(객체들) 날리기

# 8-2) model load : 메모리에 올린다
xgb_model2 <- xgb.load('xgboost.model')

pred2 <- predict(xgb_model2, test$data)
range(pred2)


######################################################
## iris로 해보기 : y이항분류
######################################################
iris_df <- iris

# 1. y 범주를 이항으로 변경하기
iris_df$Species <- ifelse(iris_df$Species == 'setosa', 0, 1)
str(iris_df) # Species 숫자로 바뀜 원래 3가지 팩터형이었음
table(iris_df$Species) # 그래서 50개 100개로 나뉨

# 2. dataset 생성
idx <- sample(nrow(iris_df), nrow(iris_df)*0.7)
train <- iris_df[idx, ]
test <- iris_df[-idx, ]

# x : matrix, y : verctor # DMatrix 생성을 위하여
train_x <- as.matrix(train[, -5])
train_y <- train$Species
dim(train_x)
str(train_y)

# 3. DMatrix 생성
# dtrain <- xgb.DMatrix(data = train$data, label = train$label) # 아까 했던 거
  dtrain <- xgb.DMatrix(data = train_x, label = train_y)
  dtrain # 105 4

# 4. xgboost model 생성
xgb_iris_model <- xgboost(data = dtrain, max_depth = 2, eta = 1, nthread = 2, nrounds = 2, objective = "binary:logistic", verbose = 0)
xgb_iris_model

# 5. 학습된 model의 변수 중요도 영향력 보기
import <- xgb.importance(colnames(train_x), model = xgb_iris_model)
import

# 6. 예측치
test_x <- as.matrix(test[, -5])
test_y <- test$Species

pred <- predict(xgb_iris_model, test_x)
range(pred) # 0.06508537 0.94941592
y_pred <- ifelse(pred >= 0.5, 1, 0)

tab <- table(test_y, y_pred)
acc <- (tab[1,1] + tab[2,2]) / length(test_y)
cat('분류정확도 =', acc*100)



######################################################
## iris로 해보기 : 다항분류
######################################################

?xgboost
# objective 속성
# objective = 'reg:squarederror' : 연속형(default)
# objective = 'binary:logistic' : y이항분류 
# objective = 'multi:softmax : y다항분류
## 주의사항 : class 시작 번호가 0이어야 함(+넘버타입) 3클래스 : 0 1 2
##            num_class = n 클래스 개수 알려줘야 함

#위에서 그대로 복사하고 수정
iris_df <- iris
table(iris_df)
# 1. y 범주를 다항으로 변경하기
iris_df$Species <- ifelse(iris_df$Species == 'setosa', 0, ifelse(iris_df$Species == 'versicolor', 1, 2))
str(iris_df) # Species 0,1,2 num으로 바뀜 원래 3가지 팩터형이었음
table(iris_df$Species) # 그래서 50개 50개 50개로 나뉨

# 2. data set 생성
idx <- sample(nrow(iris_df), nrow(iris_df)*0.8)
train <- iris_df[idx,]
test <- iris_df[-idx,]

# 3. xgb.DMatrix 생성

train_x <- as.matrix(train[-5]) # 매트릭스
train_y <- train$Species        # 벡터

dmtrix <- xgb.DMatrix(data = train_x, label = train_y)

# 4. xgboost model 생성
xgb_iris_model2 <- xgboost(data = dmtrix, max_depth = 2, eta = 1, 
                           nthread = 2, nrounds = 2, 
                           objective = "multi:softmax", num_class = 3,    # num_class로 몇개인지 지정해줘야함
                           verbose = 0)
xgb_iris_model2

# 5. 예측치 prediction
test_x <- as.matrix(test[,-5])
test_y <- test$Species

pred <- predict(xgb_iris_model2, test_x)
range(pred)  # 0 ~ 2 : 다항분류라서 바로 범주 예측함 : cut off 안필요
tab <- table(test_y, pred) 
acc <- (tab[1,1]+tab[2,2]+tab[3,3])/sum(tab)
cat('분류정확도 =', acc*100, '%')  
  
import <- xgb.importance(colnames(train), model = xgb_iris_model2)
import
xgb.plot.importance(importance_matrix = import)

# 6. 추가적으로 평균 오차 검토
mean_err <- mean(pred != test_y)
cat('평균 오차 =', mean_err, '%')


######################################################
## iris로 해보기 : y가 연속형 : 회귀트리
######################################################
# objective = 'reg:squarederror' : 연속형(default)

iris_df <- iris

# 2. dataset 생성
idx <- sample(nrow(iris_df), nrow(iris_df)*0.7)
train <- iris_df[idx, ]
test <- iris_df[-idx, ]

# 2. xgboost model 생성
# y : 1번 칼럼
# x : 2~4번 칼럼

train_x <- as.matrix(train[, c(2:4)])
train_y <- train$Sepal.Length
dim(train_x)
str(train_y)

# 3. DMatrix 생성
# dtrain <- xgb.DMatrix(data = train$data, label = train$label) # 아까 했던 거
dtrain <- xgb.DMatrix(data = train_x, label = train_y)
dtrain # 105 4

# 4. xgboost model 생성
xgb_iris_model <- xgboost(data = dtrain, max_depth = 2, eta = 1, nthread =2, nrounds = 3, verbose = 0)
                          
xgb_iris_model

# 5. 학습된 model의 변수 중요도 영향력 보기
import <- xgb.importance(colnames(train_x), model = xgb_iris_model)
import

# 6. 예측치
test_x <- as.matrix(test[, 2:4])
test_y <- test$Sepal.Length

pred <- predict(xgb_iris_model, test_x)
range(pred) # 4.781450 7.652664 : 숫자 예측

mse <- mean( (test_y - pred)^2)
cat('MSE =', mse)


