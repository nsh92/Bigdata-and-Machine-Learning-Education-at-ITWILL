#################################
## <제15장 연습문제>
################################# 

###################################
## 선형 회귀분석 연습문제 
###################################

# 01. ggplot2패키지에서 제공하는 diamonds 데이터 셋을 대상으로 
# carat, table, depth 변수 중 다이아몬드의 가격(price)에 영향을 
# 미치는 관계를 다음과 같은 단계로 다중회귀분석을 수행하시오.

library(ggplot2)
data(diamonds)
str(diamonds)

# 단계1 : 다이아몬드 가격 결정에 가장 큰 영향을 미치는 변수는?
y = diamonds$price
x1 = diamonds$carat
x2 = diamonds$table
x3 = diamonds$depth
df = data.frame(x1,x2,x3,y)
result.lm1 <- lm(formula = y ~ ., data = df)
result.lm1
summary(result.lm1)
# x1, carat이 가장 큰 영향을 미치는 변수다

# 단계2 : 다중회귀 분석 결과를 정(+)과 부(-) 관계로 해설
# 기울기에 근거하여, carat은 price에 대하여 정의 관계, table과 depth는 부의 관계로 파악된다

# 02. mtcars 데이터셋을 이용하여 다음과 같은 단계로 다중회귀분석을 수행하시오.

library(datasets)
str(mtcars) # 연비 효율 data set 

# 단계1 : 연비(mpg)는 마력(hp), 무게(wt) 변수와 어떤 상관관계를 갖는가? 
y2 = mtcars$mpg
x4 = mtcars$hp
x5 = mtcars$wt
df1 = data.frame(x4,x5,y2)
cor(df1)
# 연비는 마력과 무게에 대하여 음의 상관관계를 가진다

# 단계2 : 마력(hp)과 무게(wt)는 연비(mpg)에 어떤 영향을 미치는가? 
result.lm2 <- lm(formula = y2 ~ ., data = df1)
result.lm2
summary(result.lm2)
# 마력과 무게는 연비에 대하여 음의 영향을 미친다

# 단계3 : hp = 90, wt = 2.5t일 때 회귀모델의 예측치는?
x_data <- data.frame(x4=90, x5=2.5) # 모델 생성시 동일한 변수의 이름을 사용해야 함
answer <- predict(result.lm2, data.frame(x_data))
cat('회귀모델 예측치는', answer) # 24.67339

# 03. product.csv 파일의 데이터를 이용하여 다음과 같은 단계로 다중회귀분석을 수행하시오.
setwd("C:/ITWILL/2_Rwork/Part-IV")
product <- read.csv("product.csv", header=TRUE)

#  단계1 : 학습데이터(train),검정데이터(test)를 7 : 3 비율로 샘플링
x1 <- sample(1:nrow(product), 0.7*nrow(product))
train1 <- product[x1,]
test1 <- product[-x1,]
str(product)
#  단계2 : 학습데이터 이용 회귀모델 생성 
#        변수 모델링) y변수 : 제품_만족도, x변수 : 제품_적절성, 제품_친밀도
lm_product <- lm(제품_만족도 ~ ., data = train1)
summary(lm_product)

#  단계3 : 검정데이터 이용 모델 예측치 생성 
y1_pred <- predict(lm_product, test1)
y1_pred
#  단계4 : 모델 평가 : MSE, cor()함수 둘 다 이용  
y1_true <- test1$제품_만족도
error1 <- y1_pred - y1_true
mse1 <- mean(error1^2)
cat('mse =', mse1 )

r1 <- cor(y1_pred, y1_true)
cat('r =', r1)

###################################
## 로지스틱 회귀분석 연습문제 
###################################
# 04.  admit 객체를 대상으로 다음과 같이 로지스틱 회귀분석을 수행하시오.
# <조건1> 변수 모델링 : y변수 : admit, x변수 : gre, gpa, rank 
# <조건2> 7:3비율로 데이터셋을 구성하여 모델과 예측치 생성 
# <조건3> 분류 정확도 구하기 

# 파일 불러오기
admit <- read.csv('admit.csv')
str(admit) # 'data.frame':	400 obs. of  4 variables:
#$ admit: 입학여부 - int  0 1 1 1 0 1 1 0 1 0 ...
#$ gre  : 시험점수 - int  380 660 800 640 520 760 560 400 540 700 ...
#$ gpa  : 시험점수 - num  3.61 3.67 4 3.19 2.93 3 2.98 3.08 3.39 3.92 ...
#$ rank : 학교등급 - int  3 3 1 4 4 2 1 2 3 2 ...

# 1. data set 구성 
idx <- sample(1:nrow(admit), nrow(admit)*0.7)
train_admit <- admit[idx, ]
test_admin <- admit[-idx, ]

# 2. model 생성 
model <- glm(admit ~ ., data = train_admit)
summary(model)
# 3. predict 생성 
pred <- predict(model, newdata = test_admin, type = "response")

# 4. 모델 평가(분류정확도) : 혼돈 matrix 이용/ROC Curve 이용
cpred <- ifelse(pred > 0.5, 1, 0)
true <- test_admin$admit
tab <- table(true, cpred)
library(ROCR)
pr <- prediction(pred, test_admin$admit)
prf <- performance(pr, measure = "tpr", x.measure = "fpr")
plot(prf)

acc <- (tab[1,1] + tab[2,2]) / sum(tab)
cat('분류정확도 =', acc )
recall <- tab[2,2] / (tab[2,1] + tab[2,2])
precision <- tab[2,2] / (tab[1,2] + tab[2,2])
F1 <- 2*((recall * precision) / (recall + precision))
cat('조화평균 =', F1)
