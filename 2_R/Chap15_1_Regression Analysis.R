######################################################
# 회귀분석(Regression Analysis)
######################################################
# - 특정 변수(독립변수:설명변수)가 다른 변수(종속변수:반응변수)에 어떠한 영향을 미치는가 분석

###################################
## 1. 단순회귀분석 
###################################
# - 독립변수와 종속변수가 1개인 경우

# 단순선형회귀 모델 생성  
# 형식) lm(formula= y ~ x 변수, data) 
setwd("c:/itwill/2_rwork/part-iv")
product <- read.csv("product.csv", header=TRUE)
head(product) # 친밀도 적절성 만족도(등간척도 - 5점 척도)

str(product) # 'data.frame':  264 obs. of  3 variables:
y = product$'제품_만족도' # 종속변수
x = product$'제품_적절성' # 독립변수
df <- data.frame(x, y)

# 회귀모델 생성 
result.lm <- lm(formula=y ~ x, data=df)
result.lm # 회귀계수 
# Coefficients:
#(Intercept)      x  
# 0.7789       0.7393  
# 방정식 (y) = a*X + b(a기울기 b절편)
#            = 0.7393X + 0.7789

head(df)
X <- 4 # 입력변수
Y <- 3 # 정답
a <- 0.7393 # 기울기기
b <- 0.7789 # 절편

# 회귀방정식 : y를 예측하는 것
y <- a*X + b
cat('y의 예측치 =', y)
# 정답은 아니지만 근사함
err <- y - Y # 모델의 오차
cat('model error = ', err)

names(result.lm) #12개 뜸
# [1] "coefficients" : 회귀계수
# [2] "residuals" : 오차, 잔차
# [5] "fitted.values" : 적합치(예측치)

result.lm$coefficients
# 이렇게 필요한 것만 골라 볼 수 있음

result.lm$residuals # -0.73596305 위에서 계산했던 err와 유사
# 잔차만 쏙
result.lm$fitted.values # 3.735963 위에서 y의 예측치 계산했던 것과 유사
# 모델링 출력값

# 제품 적절성이 만족도에 미치는 인과관계를 보고자했던 것의 초장의 의도임
# 회귀모델 예측 
# predict(모델객체, 넣을변수) -> 예측된 y
predict(result.lm, data.frame(x=5)) 
# 4.475239
range(x)
predict(result.lm, data.frame(x=6))

# (2) 선형회귀 분석 결과 보기
summary(result.lm) 
# 요약통계뿐만 아니라 모델에 대한 통계치를 보여줌
# x -> y 맞는가부터 전반적인 것
# p-value가 0.05보다 작으면 통계적으로 유의하다
# <회귀모델 해석 순서>
# 1. F-statistic: p-value < 0.05
# 2. Adjusted R-squared:  0.5865 : 모델의 설명력(예측력)이 약 0.56 : 1에 가까울 수록 ㅅㅌㅊ
# 3. x의 유의성 검정: Coefficients 표의 t value(1.96사이)와 Pr, 별의 갯수(3개니까 강력한 관계다)

cor(df)
# 0.7668527 높은 상관관계
0.7668527^2 # 0.588 = r-squared

# (3) 단순선형회귀 시각화
# x,y 산점도 그리기 
plot(formula=y ~ x, data=df)
# 회귀분석
result.lm <- lm(formula=y ~ x, data=df)
# 회귀선 (y절편 : 0.77)
abline(result.lm, col='red')
# 그냥 하면 절편이 1위에 있음 : 축의 시작 넘버가 0으로 설정되게끔 해야 함
plot(formula=y ~ x, data=df, xlim = c(0,5), ylim = c(0,5))


result.lm$coefficients
# (Intercept)      x 
# 0.7788583   0.7392762
# 이새끼들은 어떻게 계산된 건가

y <- product$'제품_만족도'
x <- product$'제품_적절성'
# 기울기 = cov(xy)/Sxx
Covxy = mean((x - mean(x)) * (y - mean(y)))
Sxx = mean((x-mean(x))^2)
a <- Covxy / Sxx
# 0.7392

# 절편
b <- mean(y) - (a * mean(x))
# 0.7789


###################################
## 2. 다중회귀분석
###################################
# - 여러 개의 독립변수 -> 종속변수에 미치는 영향 분석
# 가설 : 음료수 제품의 적절성(x1)과 친밀도(x2)는 제품 만족도(y)에 정의 영향을 미친다.

product <- read.csv("product.csv", header=TRUE)
head(product) # 친밀도 적절성 만족도(등간척도 - 5점 척도)

#(1) 변수선택 : 적절성 + 친밀도 -> 만족도  
y = product$'제품_만족도' # 종속변수
x1 = product$'제품_친밀도' # 독립변수1
x2 = product$'제품_적절성' # 독립변수2

df <- data.frame(x1, x2, y)

result.lm <- lm(formula = y ~ x1 + x2, data=df)
#result.lm <- lm(formula=y ~ ., data=df)
# ~ . 점 : 'y빼고 다' 독립변수다
result.lm <- lm(formula = y ~ ., data=df)

# 계수 확인 
result.lm # 같은 값 나오는 거 확인
# y절편하나, 기울기 두개 출력
# (Intercept)     x1           x2  
# 0.66731      0.09593      0.68522 
b <- 0.66731
a1 <- 0.09593
a2 <- 0.68522
head(df)
x1 <- 3
x2 <- 4
# 이래놓고 y가 3 나오는지 확인해보자
# 다중회귀방정식
y = (a1 * x1 + a2 * x2) + b
# 3.69598
Y = 3
err = Y - y
abs(err) # 절대값
# 0.69정도의 오차가 있다

# 분석 결과 확인
summary(result.lm)
# 1. F-statistic: p-value: < 2.2e-16 : 모델은 통계적으로 유의하다
# 2. Adjusted R-squared:  0.5945 설명력은 이정도다
# 3. x의 유의성 검정
# x1  2.478   0.0138 *      -> 친밀도
# x2  15.684  < 2e-16 ***   -> 적절성
# 둘 다 유의미한데 친밀도보다 적절성이 더 많은 영향을 미친다

install.packages('car') # 다중공선성 문제 확인
library(car)

Prestige # 직업군 102개 평판
str(Prestige)
# $ education: 교육수준(x1)
# $ income   : 수입(y)
# $ women    : 여성비율(x2)
# $ prestige : 평판(x3)
# $ census   : 직업수
# $ type     : Factor w/ 3 levels "bc","prof","wc": 2 2 2 2 2 2 2 2 2 2 ...

row.names(Prestige) # 행이름 : 직업군의 이름 확인

df <- Prestige[, c(1:4)]
str(df)
model <- lm(income ~ ., data = df)
model

summary(model)
# Coefficients:
#            Estimate Std. Error  t value  Pr(>|t|)    
# (Intercept) -253.850   1086.157  -0.234    0.816       
# education    177.199    187.632   0.944    0.347      (상관없음)
# women        -50.896      8.556  -5.948 4.19e-08 ***  (음의상관)
# prestige     141.435     29.910   4.729 7.58e-06 ***  (양의상관)

res <- model$residuals #잔차(오차) = 정답 - 예측치
summary(res)
length(res) 

# 잔차 표준화
res_scale <- scale(res) # 0과 1로 정규화작업
shapiro.test(res)
summary(res_scale)

# MSE mean square error
# 표준화
mse <- mean(res_scale^2) # 평균제곱오차
cat('MSE =', mse) # MSE = 6369159 # 표준화하기에 적절한 데이터가 아니었내
# 표준화 후 MSE = 0.99
# 0에 가까울수록 좋지
# 제곱 : 부호 절대값, 패널티
# 평균 : 전체 오차에 대한 평균

###################################
## 3. x 변수 선택
###################################

new_data <- Prestige[, c(1:5)]
dim(new_data) # 102   5
library(MASS)

model2 <- lm(income ~., data = new_data)

step <- stepAIC(model2, direction = 'both')
# 여러 모델링이 제시되는데, AIC가 작을수록 좋음
# 가장 작은 거 해보자
model3<-lm(income ~ women + prestige, data = new_data)
summary(model3)
# 개선된 R-squared 값 확인
# 맹신하진 마라


###################################
# 4. 다중공선성(Multicolinearity)
###################################
# - 독립변수 간의 강한 상관관계로 인해서 회귀분석의 결과를 신뢰할 수 없는 현상
# - 생년월일과 나이를 독립변수로 갖는 경우
# - 해결방안 : 강한 상관관계를 갖는 독립변수 제거

# (1) 다중공선성 문제 확인
library(car)
fit <- lm(formula=Sepal.Length ~ Sepal.Width+Petal.Length+Petal.Width, data=iris)
vif(fit) # 분산팽창요인 정보 제공 : 독립변수끼리의 상관성
 
sqrt(vif(fit))>2 # root(VIF)가 2 이상인 것은 다중공선성 문제 의심 
# Petal.Length  Petal.Width 임마들이 값이 월등히 크다 : 문제내 : 다중공선성 문제가 의심스럽다

# (2) iris 변수 간의 상관계수 구하기
cor(iris[,-5]) # 변수간의 상관계수 보기(Species 제외) 
#x변수 들끼 계수값이 높을 수도 있다. -> 해당 변수 제거(모형 수정) <- Petal.Width
# 점마들 0.96임 거의 1
# 그러니 점마들을 나란히 쓰면 안되는 것임 : 하나를 빼던가하셈

# (3) 학습데이터와 검정데이터 분류
x <- sample(1:nrow(iris), 0.7*nrow(iris)) # 전체중 70%만 추출 # 행의 인덱스를 추출하는 것
train <- iris[x, ] # 학습데이터 추출
test <- iris[-x, ] # 검정데이터 추출

# (4) Petal.Width 변수를 제거한 후 회귀분석 : 모델 생성
iris_model <- lm(formula=Sepal.Length ~ Sepal.Width + Petal.Length, data=train)
iris_model
summary(iris_model)
# 랜덤하게 샘플을 추출하기에 실행할 때마다 값은 달라짐

# (5) model 예측치 : test_set(x) -> prediction(y)
y_pred <- predict(iris_model, test)
y_pred

# (6) 모델 평가 
# MSE(표준화된 경우에 사용 가능)
# 정답을 미리 만듦
y_true <- test$Sepal.Length # 모델에서의 종속변수 컬럼

Error <- y_true - y_pred
mse <- mean(Error^2)
cat('MSE =', mse) # 0에 가까울수록 좋음

# 상관계수 r : 표준화가 안 된 경우
r <- cor(y_true, y_pred)
cat('r =', r) # 1에 가까울수록 좋음

y_pred[1:10]
y_true[1:10]
# 나란히 비교해보자

# 시각화 평가
plot(y_true, col='blue', type = 'l', label = 'y true')
points(y_pred, col='red', type = 'l', label = 'y pred')
# 범례 추가
legend("topleft", legend = c('y true', 'y pred'),
       col=c('blue', 'red'), pch = '-')
# 어디서 잔차가 많이 발생하나 시각적으로 확인 가능

##########################################
##  5. 선형회귀분석 잔차검정과 모형진단
##########################################

# 1. 변수 모델링  : x, y 선정
# 2. 회귀모델 생성 : lm()
# 3. 모형의 잔차검정 
#   1) 잔차의 등분산성 검정 : 균등한 분포
#   2) 잔차의 정규성 검정 : 평균을 중심으로의 분포
#   3) 잔차의 독립성(자기상관) 검정 
# 4. 다중공선성 검사 
# 5. 회귀모델 생성/ 평가 

# 위 절차를 모두 충족하는 건 드물다

names(iris)

# 1. 변수 모델링 : y:Sepal.Length <- x:Sepal.Width,Petal.Length,Petal.Width
formula = Sepal.Length ~ Sepal.Width + Petal.Length + Petal.Width
# 이렇게 미리 함수를 지정해도 되는구먼

# 2. 회귀모델 생성 
model <- lm(formula = formula,  data=iris)
model
names(model)


# 3. 모형의 잔차검정
plot(model)
#Hit <Return> to see next plot: 잔차 vs 적합값 -> 패턴없이 무작위 분포(포물선 분포 좋지않은 적합)
  # 등분산성 검정 : 잔차 0을 기준으로 상하좌우 골고루 분포되어있는가

#Hit <Return> to see next plot: Normal Q-Q -> 정규분포 : 대각선이면 잔차의 정규성 
  # 정규분포 : 점선에 대하여 점들이 비등하게 겹쳐있는가

#Hit <Return> to see next plot: 척도 vs 위치 -> 중심을 기준으로 고루 분포 
#Hit <Return> to see next plot: 잔차 vs 지렛대값 -> 중심을 기준으로 고루 분포 
  ## 독립성
  ## 3 4번은 참고용이고 1 2번이 중요함함

# (1) 등분산성 검정 
plot(model, which =  1) # 이렇게 which로 지정하면 보고싶은 페이지만 봄
methods('plot') # plot()에서 제공되는 객체 보기 

# (2) 잔차 정규성 검정
attributes(model) # coefficients(계수), residuals(잔차), fitted.values(적합값)
res <- residuals(model) # 잔차 추출 
res <- model$residuals # 똑같음
shapiro.test(res) # 정규성 검정 - p-value = 0.9349 >= 0.05
# 귀무가설 : 정규성과 차이가 없다.

# 정규성 시각화  
hist(res, freq = F) 
qqnorm(res)

# (3) 잔차의 독립성(자기상관 검정 : Durbin-Watson) DW테스트
install.packages('lmtest')
library(lmtest) # 자기상관 진단 패키지 설치 
dwtest(model) # 더빈 왓슨 값
# DW = 2 ~ 4 : 채택력 해당, p-value 0.05
# 잔차들이 상관성이 있는가를 판단

# 4. 다중공선성 검사 
library(car)
sqrt(vif(model)) > 2 # TRUE 

formula = Sepal.Length ~ Sepal.Width + Petal.Length 
model <- lm(formula = formula,  data=iris)
summary(model) # 모델 평가


##########################################
##  6. 범주형 변수 사용
##########################################
# 범주형 = 카테고리형
# - 범주형 변수(gender 간주) -> 더미변수 변환(남자0 여자1로, 정확히 기준을 0, 나머지 1)
# - 범주형 변수는 기울기에 영향이 없음(절편에만 영향)
# - 범주형 범주의 수 가 n개 가정
# - 더미변수의 수는 n-1개
# ex) 혈액형 (AB, A, B, O형) <- 3개 변수 필요
##       x1 x2 x3
##   A형 1  0  0
##   B형 0  1  0
##   O형 0  0  1
##   AB  0  0  0  <- base라 함(기준)

# Factor란 것이 저런 범주형 변수를 더미 변수로 만들어주는 것
# 따라서 자료형이 Factor로 되어있다면 이미 더미 변수로 설정되어있다는 것임

# 의료비 예측
insurance <- read.csv(file.choose())
str(insurance)
# 'data.frame':	1338 obs. of  7 variables:
# $ age     : 나이 : int  19 18 28 33 32 31 46 37 37 60 ...
# $ sex     : 성별 : Factor w/ 2 levels "female","male": 1 2 2 2 2 1 1 1 2 1 ...
# $ bmi     : 비만도지수 : num  27.9 33.8 33 22.7 28.9 ...
# $ children: 자녀수 : int  0 1 3 0 0 0 1 3 2 0 ...
# $ smoker  : 흡연 : Factor w/ 2 levels "no","yes": 2 1 1 1 1 1 1 1 1 1 ...
# $ region  : 지역 : Factor w/ 4 levels "northeast","northwest",..: 4 3 3 2 2 3 3 2 1 2 ...
# $ charges : 의료비 : num  16885 1726 4449 21984 3867 ...

# 범주형 변수 : sex(2), smoker(2), region(4)
# 기준(base) : level1(base) = 0, level2(나머지) = 1

# 회귀모델 생성
insurance2 <- insurance[, -c(5:6)]
head(insurance2)
ins_model <- lm(charges ~ ., data = insurance2)
ins_model # Intercept = -7460.0, sexmale = 1321.7

# female = 0, male = 1
# [해석] 이 숫자만 본다면 여성에 비해서 남성의 의료비가 증가한다
# y = a.x + b
y_male = 1321.7 * 1 + (-7460)
y_female = 1321.7 * 0 + (-7460) 
# 남성은 구해도 여성은 구하지 못함 변수가 걍 0이기 때문
# 그래서 남성은 증가하는 거로 보이는 거임
# 이래서 기울기는 의미없음 항상 같고 절편만 유의미함 
# 근대 여성에 대한 기울기가 궁금하다면 레벨을 바꾸면 댐
x <- c('male', 'female')
insurance2$sex <- factor(insurance2$sex, levels = x)
str(insurance2)
ins_model <- lm(charges ~ ., data = insurance2)
ins_model # Intercept = -6138.2, sexfemale = -1321.7
# [해석] 여성이 남성에 비해서 의료비 절감 -1321.7만큼

male <- subset(insurance2, sex == 'male')
female <- subset(insurance2, sex == 'female')
mean(male$charges) # 13956.75
mean(female$charges) # 12569.58 이렇게 통계적으로도 확인 가능

# 절편의 영향을 보자
## dummy 변수 vs 절편
insurance3 <- insurance[, -6]
head(insurance3)
ins_model2 <- lm(charges ~ smoker, data = insurance3)
ins_model2 # 절편8434, 기울기 23616
# base : smokerno( = 0)
# [해석] 흡연하면 비흡연자에 비해 23616만큼 비싸진다

no <- subset(insurance3, smoker == 'no')
mean(no$charges) # 이 값이 그대로 절편이 된 것을 확인
yes <- subset(insurance3, smoker == 'yes')
mean(yes$charges)

# 즉 절편은 base일 때의 평균치와 같다

table(insurance$region)
# n개의 범주, n-1개의 더미변수
insurance4 <- insurance
ins_model3 <- lm(charges ~ region, data = insurance4)
# 절편 = 13406.4, 기울기들 = -988.8, 1329.0, -1059.4
# northeast가 베이스

