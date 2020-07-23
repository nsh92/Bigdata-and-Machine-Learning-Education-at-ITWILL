# chap16_1_Classification
library(rpart) # rpart() : 분류모델 생성 
install.packages("rpart.plot")
library(rpart.plot) # prp(), rpart.plot() : rpart 시각화
install.packages('rattle')
library('rattle') # fancyRpartPlot() : node 번호 시각화 


# 단계1. 실습데이터 생성 
data(iris)
set.seed(415)
idx = sample(1:nrow(iris), 0.7*nrow(iris))
train = iris[idx, ]
test = iris[-idx, ]
dim(train) # 105 5
dim(test) # 45  5

table(train$Species)

# 단계2. 분류모델 생성 
# rpart(y변수(범주) ~ x변수(연속), data)
model = rpart(Species~., data=train) # iris의 꽃의 종류(Species) 분류 
model
# 1) root 105 68 setosa (0.35238095 0.31428571 0.33333333)
# root node : 105 전체 데이터 크기, 68 가장 많은 비율 레이블을 뺀 나머지, 각 확률(setosa : 0.35~)

# 2) Petal.Length< 2.45 37  0 setosa (1.00000000 0.00000000 0.00000000) *
# 루트 기준 왼쪽 노드
# P.L < 2.45 : 분류조건 : 37와 0개로, (lable 분류비율), * : 단노드 유무 : 자식이 없다
# 2)와 3)은 똑같은 레벨 : 같은 너비의 들여쓰기

# 3) Petal.Length>=2.45 68 33 virginica (0.00000000 0.48529412 0.51470588)
# 2)와 반대 조건, 68개 : 전체 개수, 33개 : 68중 가장 많은 수인 버지니카, (각 확률), *없으니 자식이 있음

# 6,7)은 3)의 자식마디이고 * 없음


# 분류모델 시각화 - rpart.plot 패키지 제공 
prp(model) # 간단한 시각화   
rpart.plot(model) # rpart 모델 tree 출력
fancyRpartPlot(model) # node 번호 출력(rattle 패키지 제공)

# 단계3. 분류모델 평가  
pred <- predict(model, test) # 비율 예측 

pred <- predict(model, test, type="class") # 분류 예측 class없으면 비율로 예측

# 1) 분류모델로 분류된 y변수 보기 
table(pred)

# 2) 분류모델 성능 평가 
table(pred, test$Species)
# 여기선 행이 예측치로 했음
(13+16+12) / nrow(test)
# 분류정확도 91%



##################################################
# Decision Tree 응용실습 : 암 진단 분류 분석
##################################################
# "wdbc_data.csv" : 유방암 진단결과 데이터 셋 분류

# 1. 데이터셋 가져오기 
wdbc <- read.csv('C:/itwill/2_Rwork/part-iv/wdbc_data.csv', stringsAsFactors = FALSE)
str(wdbc)

# 2. 데이터 탐색 및 전처리 
wdbc <- wdbc[-1] # id 칼럼 제외(이상치) 
head(wdbc)
head(wdbc[, c('diagnosis')], 10) # 진단결과 : B -> '양성', M -> '악성'

# (종속)목표변수(y변수)를 factor형으로 변환 
wdbc$diagnosis <- factor(wdbc$diagnosis, levels = c("B", "M")) # 0, 1로 변환, stringsAsFactors = FALSE설정안하면 아마 팩터로 가져왔음
wdbc$diagnosis[1:10]

summary(wdbc)
# 3. 정규화  : 서로 다른 특징을 갖는 칼럼값 균등하게 적용 
normalize <- function(x){ # 정규화를 위한 함수 정의 
  return ((x - min(x)) / (max(x) - min(x)))
}

# wdbc[2:31] : x변수에 해당한 칼럼 대상 정규화 수행 
wdbc_x <- as.data.frame(lapply(wdbc[2:31], normalize)) # 종속변수는 정규화할 필요 없으니 2:31
wdbc_x
summary(wdbc_x) # 0 ~ 1 사이 정규화 
class(wdbc_x) # [1] "data.frame"
nrow(wdbc_x) # [1] 569

wdbc_df <- data.frame(wdbc$diagnosis, wdbc_x)
dim(wdbc_df) # 569  31
head(wdbc_df)

# 4. 훈련데이터와 검정데이터 생성 : 7 : 3 비율 
idx = sample(nrow(wdbc_df), 0.7*nrow(wdbc_df))
wdbc_train = wdbc_df[idx, ] # 훈련 데이터 
wdbc_test = wdbc_df[-idx, ] # 검정 데이터 
dim(wdbc_train) # 398 31
dim(wdbc_test) # 171 31

# 5. rpart 분류모델 생성 
model <- rpart(wdbc.diagnosis ~ ., data = wdbc_train)
model

rpart.plot(model)

# 6. 분류모델 평가  
y_pred <- predict(model, wdbc_test, type = 'class')
y_pred <- ifelse(y_pred[,1] >= 0.5, 0, 1) # 비율을 더미변수화
y_true <- wdbc_test.diagnosis
table(y_true, y_pred)

acc <- (99+52) / nrow(wdbc_test) # 분류정확도
M <- 52 / (52+14) 
B <- 99 / (99+6)  # 특이도



############################################
### 교차 검정
############################################

# 단계 1: K겹 교차검정을 위한 샘플링
install.packages("cvTools")
library(cvTools)
?cvFolds
# cvFolds(n, K = 5, R = 1,
#   type = c("random", "consecutive", "interleaved"))
# n = 데이터셋의 전체 길이, k = 나누는 횟수, 나눠진 거 안에서 세트 수
# c(추출방식)   

cross <- cvFolds(n=nrow(iris), K = 3, R = 1, type = "random")
#1번으로 테스트 2번에 검증, 1+2 테스트 3번에 검증 이런식 50개씩 나눠짐
# 또는 2,3 번으로 훈련하고 1번으로 검증하고
cross # Fold : dataset, Index : row
str(cross) # subsets은 또 2차원임

# set1
d1 <- cross$subsets[cross$which == 1, 1] # 첫번째 데이터셋을 호출함
# set2
d2 <- cross$subsets[cross$which == 2, 1]
d3 <- cross$subsets[cross$which == 3, 1] # [k, r] 이를 이용하여 논리적 for문으로 들어가게함

length(d1)
length(d2)
length(d3)
# 50개씩
# iris에서 꺼내 올 행 숫자를 뽑은 거임

K <- 1:3
R <- 1

for(r in R){ # R은 set : 열 index
  for(k in K){ # k겹 : 행 index
    idx <- cross$subsets[cross$which == k, r]
    cat('k=', k, '\n')
    print(idx)
  }
}

# 세바퀴 확인 : 1회전 * 3회전

###############################################
cross <- cvFolds(n=nrow(iris), K = 3, R = 2, type = "random")
K <- 1:3
R <- 1:2

for(r in R){ # R은 set : 열 index
  cat('R=', r, '\n')
  for(k in K){ # k겹 : 행 index
    idx <- cross$subsets[cross$which == k, r]
    cat('k=', k, '\n')
    print(idx)
  }
}

# 여섯바퀴 확인 : 2회전 * 3회전

##############################################
ACC <- numeric()

for(r in R){ # R은 set : 열 index
  cat('R=', r, '\n')
  for(k in K){ # k겹 : 행 index
    idx <- cross$subsets[cross$which == k, r]
    #cat('k=', k, '\n')
    #print(idx)
    test <- iris[idx,] # 검정용 : 50개
    train <- iris[-idx,] # 훈련 : 100개
    model <- rpart(Species ~., data = train)
    pred <- predict(model, test, type = 'class')
    tab <- table(test$Species, pred)
    ACC[k] <- (tab[1,1]+tab[2,2]+tab[3,3]) / sum(tab)
  }
}

ACC
# 보통 요놈을 산술평균한 걸 분류정확도로 침
mean(ACC)

######################################################
ACC <- numeric()
CNT <- 1

for(r in R){ # R은 set : 열 index
  cat('R=', r, '\n')
  for(k in K){ # k겹 : 행 index
    idx <- cross$subsets[cross$which == k, r]
    #cat('k=', k, '\n')
    #print(idx)
    test <- iris[idx,] # 검정용 : 50개
    train <- iris[-idx,] # 훈련 : 100개
    model <- rpart(Species ~., data = train)
    pred <- predict(model, test, type = 'class')
    tab <- table(test$Species, pred)
    ACC[k] <- (tab[1,1]+tab[2,2]+tab[3,3]) / sum(tab)
    cnt <- cnt + 1
  }
}

ACC
mean(ACC)
# 이게 FM이긴 한데, 결과는 같음
#####################################################
# titanic3.csv 변수 설명
#'data.frame': 1309 obs. of 14 variables:
#1.pclass : 1, 2, 3등석 정보를 각각 1, 2, 3으로 저장
#2.survived : 생존 여부. survived(생존=1), dead(사망=0)
#3.name : 이름(제외)
#4.sex : 성별. female(여성), male(남성)
#5.age : 나이
#6.sibsp : 함께 탑승한 형제 또는 배우자의 수
#7.parch : 함께 탑승한 부모 또는 자녀의 수
#8.ticket : 티켓 번호(제외)
#9.fare : 티켓 요금
#10.cabin : 선실 번호(제외)
#11.embarked : 탑승한 곳. C(Cherbourg), Q(Queenstown), S(Southampton)
#12.boat     : (제외)Factor w/ 28 levels "","1","10","11",..: 13 4 1 1 1 14 3 1 28 1 ...
#13.body     : (제외)int  NA NA NA 135 NA NA NA NA NA 22 ...
#14.home.dest: (제외)

titanic<-read.csv(file.choose())
# 위 타이타닉 분류모형 ㄱㄱ
# 생존률에 결정적인 변수를 알아보자
# 변수로 못씀 : 3, 8,10,12~14
# <조건1> 6개 변수 제외한 서브셋 생성
# <조건2>

titanic_df <- titanic[, -c(3,8,10,12:14)]
titanic_df$survived <- factor(titanic_df$survived)
str(titanic_df)

idx <- sample(nrow(titanic_df), nrow(titanic_df)*0.7)
train <- titanic_df[idx,]
test <- titanic_df[-idx,]

model <- rpart(survived ~., data = train)
model # 가장 중요 변수 : sex > age
rpart.plot(model)


y_pred <- predict(model, test, type = "class")
y_true <- test$survived

# model 평가
tab <- table(y_true, y_pred)

acc <- (tab[1,1]+tab[2,2]) / sum(tab)
cat('accuracy =', acc)





