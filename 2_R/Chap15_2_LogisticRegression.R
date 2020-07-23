# Chap15_2_LogisticRegression

###############################################
# 15_2. 로지스틱 회귀분석(Logistic Regression) 
###############################################

# 목적 : 일반 회귀분석과 동일하게 종속변수와 독립변수 간의 관계를 나타내어 
# 향후 예측 모델을 생성하는데 있다.

# 차이점 : 종속변수가 범주형 데이터를 대상으로 하며 입력 데이터가 주어졌을 때
# 해당 데이터의결과가 특정 분류로 나눠지기 때문에 분류분석 방법으로 분류된다.
# 유형 : 이항형(종속변수가 2개 범주-Yes/No), 다항형(종속변수가 3개 이상 범주-iris 꽃 종류)
# 다항형 로지스틱 회귀분석 : nnet, rpart 패키지 이용 
# a : 0.6,  b:0.3,  c:0.1 -> a 분류 

# 분야 : 의료, 통신, 기타 데이터마이닝

# 선형회귀분석 vs 로지스틱 회귀분석 
# 1. 로지스틱 회귀분석 결과는 0과 1로 나타난다.(이항형)
# 2. 정규분포 대신에 이항분포를 따른다.
# 3. 로직스틱 모형 적용 : 변수[-무한대, +무한대] -> 변수[0,1]사이에 있도록 하는 모형 
#    -> 로짓변환 : 출력범위를 [0,1]로 조정
# 4. 종속변수가 2개 이상인 경우 더미변수(dummy variable)로 변환하여 0과 1를 갖도록한다.
#    예) 혈액형 AB인 경우 -> [1,0,0,0] AB(1) -> A,B,O(0)


# 단계1. 데이터 가져오기
weather = read.csv("C:/itwill/2_Rwork/Part-IV/weather.csv", stringsAsFactors = F) 
# stringsAsFactors = F : 순수한 문자형으로 가져오기
dim(weather)  # 366  15
head(weather)
str(weather)

# chr 칼럼, Date, RainToday 칼럼 제거 
weather_df <- weather[, c(-1, -6, -8, -14)]
str(weather_df) # 11변수

# RainTomorrow 칼럼 -> 로지스틱 회귀분석 결과(0,1)에 맞게 더미변수 생성      
weather_df$RainTomorrow[weather_df$RainTomorrow=='Yes'] <- 1
weather_df$RainTomorrow[weather_df$RainTomorrow=='No'] <- 0
weather_df$RainTomorrow <- as.numeric(weather_df$RainTomorrow)
head(weather_df)

# y 범주 및 빈도수
table(weather_df$RainTomorrow)
prop.table(table(weather_df$RainTomorrow))

#  단계2.  데이터 셈플링
idx <- sample(1:nrow(weather_df), nrow(weather_df)*0.7)
train <- weather_df[idx, ]
test <- weather_df[-idx, ]


#  단계3.  로지스틱  회귀모델 생성 : 학습데이터 
weater_model <- glm(RainTomorrow ~ ., data = train, family = 'binomial')
# family = 'binomial' : y는 이항이다
weater_model 
summary(weater_model) 
# F통계량, 설명력은 없고 유의성 검정 내역만 뜸

# 단계4. 로지스틱  회귀모델 예측치 생성 : 검정데이터 
# newdata=test : 새로운 데이터 셋, type="response" : 0~1 확률값으로 예측 
pred <- predict(weater_model, newdata=test, type="response")  
# type = "response" : 확률로 예측 : y의 범주가 아닌 y가 나올 확률을 보여준다
pred 
range(pred, na.rm=T) # 0.001458894  0.973613764
summary(pred)
str(pred)
# 저 확률값을 근거로 이항분류하는 것은 무의미,  cut off 딱 정해야 함

# cut off = 0.5
cpred <- ifelse(pred >= 0.5, 1, 0)
table(cpred)

y_true <- test$RainTomorrow  # 정답지

# 단계5. 모델 평가
# 교차분할표
table(y_true, cpred)
acc <- (81+8) / nrow(test)
cat('분류정확도는',  acc)

no <- 89/(89+6)
yes <- 8/(8+7)

# 일일히 수정하기 짱나니
tab <- table(y_true, cpred) # 얘는 행렬이니 위치로 지정하여 자동화시키자
acc <- (tab[1,1]+tab[2,2]) / nrow(test)
cat('분류정확도는',  acc)
no <- tab[1,1] / (tab[1,1] + tab[1,2])
yes <- tab[2,2] / (tab[2,1] + tab[2,2])
no_acc <- (tab[1,2] + tab[2,1]) / nrow(test)

# 3) 특이도 : 관측치NO -> no
tab[1,1] / (tab[1,1]+tab[1,2])

# 4) 민감도 = 재현율(recall) : 관측치YES -> YES
recall <- tab[2,2] /(tab[2,1]+tab[2,2])

# 5) 정확률 : 예측치(yes) -> yes
precision <- tab[2,2] / (tab[1,2]+tab[2,2])

# 6) F1_score : 불균형 비율
F1_score = 2 * (recall * precision) / (recall + precision)
# 0.5641026

### ROC Curve를 이용한 모형평가(분류정확도)  ####
# Receiver Operating Characteristic

install.packages("ROCR")
library(ROCR)

# ROCR 패키지 제공 함수 : prediction() -> performance
pr <- prediction(pred, test$RainTomorrow)
prf <- performance(pr, measure = "tpr", x.measure = "fpr")
plot(prf)


###############################################
# 다항형 로지스틱 회귀분석 : nnet
###############################################
install.packages("nnet")
library(nnet)
idx <- sample(nrow(iris), nrow(iris)*0.7)
train <- iris[idx,]
test <- iris[-idx,]

# 활성함수
# 이항 : sigmoid function : 0 ~ 1 확률로 변환
# 다항 : softmax function : 0 ~ 1 확률로 변환 + 전체 합이 1이 되게끔
# y1 = 0.1, y2 = 0.1,  y3 = 0.8 변환 후 y3로 정답으로 나오게끔 유도
names(iris)
model <- multinom(Species ~ ., data = train)
# 신경망을 기반으로 나온 거임, 반복을 통해 개선값을 찾아냄

names(model)
model$fitted.values
range(model$fitted.values) # 1.375521e-36 1.000000e+00
str(model$fitted.values) # matrix임
model$fitted.values[1,] # 얘내 더하면 1임, 예측치
sum(model$fitted.values[1,]) # 1 또는 rowSums
train[1,] # virginica 얘가 정답, 관측치
# 저 정답을 맞추도록 높은 확률이 설정되어 있내

# 예측치 : 범주로 예측
y_pred <- predict(model, test)
y_pred # 범주를 예측했음

y_true <- test$Species

tab <- table(y_true, y_pred)
# 1개 놓짐
44 / 45 # 97%
tab
acc <- (tab[1,1] + tab[2,2] + tab[3,3]) / nrow(test)
cat('분류정확도 =', acc)
