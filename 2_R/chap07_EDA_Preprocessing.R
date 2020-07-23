chap07_EDA_Preprocessing
# 1. 탐색적 데이터 조회

# 실습 데이터 읽어오기
setwd("C:/ITWILL/2_rwork/Part-II")
dataset <- read.csv("dataset.csv", header=TRUE) # 헤더가 있는 경우
# dataset.csv - 칼럼과 척도 관계 


# 1) 데이터 조회
# - 탐색적 데이터 분석을 위한 데이터 조회 

# (1) 데이터 셋 구조
names(dataset) # 변수명(컬럼)
attributes(dataset) # names(), class, row.names
str(dataset) # 데이터 구조보기
dim(dataset) # 차원보기 : 300 7
nrow(dataset) # 관측치 수 : 300
length(dataset) # 칼럼수 : 7 
length(dataset$resident) # 300

# (2) 데이터 셋 조회
# 전체 데이터 보기
dataset # print(dataset) 
View(dataset) # 뷰어창 출력

# 칼럼명 포함 간단 보기 
head(dataset)
head(dataset, 10) 
tail(dataset) 

# (3) 칼럼 조회 
# 형식) dataframe$칼럼명   
dataset$resident
length(dataset$age) # data 수-300개 

# $ vs index
res <- dataset$resident #달러로 지정
res2 <- dataset['resident'] #인덱스로 형태
str(res) # int [1:300] 벡터형 변수
str(res2) # 'data.frame' 데이터프레임
dim(res) # 얘는 벡터
dim(res2) # 얘는 행렬 벡터아님

# 형식) dataframe["칼럼명"] 
dataset["gender"] # = dataset[2]
dataset["price"] # = dataset[]

# 형식) dataframe[색인] : 색인(index)으로 원소 위치 지정 
dataset[2] # 두번째 컬럼
dataset[6] # 여섯번째 컬럼
dataset[3,] # 3번째 관찰치(행) 전체 -> 벡터형태 : dataset$job
dataset[,3] # 3번째 변수(열) 전체 -> 데이터프레임 : dataset['job']

# dataset에서 2개 이상 칼럼 조회
dataset[c("job", "price")]
dataset[c("job":"price")] # error 연속적으로 추출하려는 건 안댄다
dataset[c(3:6)] # 이렇게 해야 연속 추출댄다
dataset[c(2,6)]

dataset[c(1,2,3)] 
dataset[c(1:3)] 
dataset[c(2,4:6,3,1)] 
dataset[-c(2)] # dataset[c(1,3:7)] 



# 2. 결측치(NA) 발견과 처리
# 9999999 - NA

# 결측치 확인
summary(dataset$price) # NA확인
table(is.na(dataset$price)) # 이렇게도 확인가능

table(is.na(dataset)) # 전체 컬럼

# 1) 결측치 제거
price2 <- na.omit(dataset$price) # 특정 컬럼 결측치 제거
length(price2) # 제거하고 난 수 , 벡터

dataset2<- na.omit(dataset) # 전체 컬럼 결측치 제거
dim(dataset2) # 행렬

## 얘내들은 NA잡느라 옆에있는 애들까지 족친 상태
## 그래서 원래 300개였는데 209개 됐음

# 특정 컬럼 기준 결측치 제거 -> subset 생성
# 날리기 보단 제외하여 뽑자
stock <- read.csv(file.choose()) #파트1의 stock.csv
str(stock)

# Market.Cap : 시가총액 변수
library(dplyr)
stock_df <- stock%>%filter(!is.na(Market.Cap))
dim(stock_df) # 69는 그대로

stock_df <- subset(stock, !is.na(Market.Cap))
dim(stock_df) # 위와 동일

# 2) 결측치 처리(0으로 대체)
# 날리지 말고 대체값을 넣어놓자
x<-dataset$price
dataset$price2 <- ifelse(is.na(x),0,x)

# 3) 결측치 처리(평균으로 대체)
dataset$price3<-ifelse(is.na(x), mean(x, na.rm=T), x)
dataset
dim(dataset) # 원래 7개였는데 9개로 바뀜
head(dataset[c('price','price2','price3')], 30)

# 학년이라던가 나이라던가의 변수에서의 결측치는 0이나 평균넣는게 적절치 않다
# 4) 통계적 방법의 결측치 처리 ( 해당 그룹에서의 평균으로 대체 )
age <- round(runif(n=12, min = 20, max = 25))
grade <- rep(1:4, 3)
age[5]<-NA
age[8]<-NA
DF <- data.frame(age, grade)
DF
# 저 결측치 자리에 그 학년 평균 나이를 넣도록 해라 age2에

n <- nrow(DF)
g1=0;g2=0;g3=0;g4=0
for(i in 1:n){
  if(DF$grade[i] == 1 & !is.na(DF$age[i])){
    g1 = g1 + DF$age[i]
  }else if(DF$grade[i] == 2 & !is.na(DF$age[i])){
    g2 = g2 + DF$age[i]
    }else if(DF$grade[i] ==3 & !is.na(DF$age[i])){
    g3 = g3 + DF$age[i]
    }else if(DF$grade[i] ==4 & !is.na(DF$age[i]))
      g4 = g4 + DF$age[i]
    
}
n

# 각 학년별 나이 합계
g1;g2;g3;g4
tab<-table(DF$grade)
age2 <- age
for(i in 1:n){
  if(is.na(DF$age[i]) & DF$grade[i]==1) age2[i] <- g1/2
  if(is.na(DF$age[i]) & DF$grade[i]==2) age2[i] <- g2/2
  if(is.na(DF$age[i]) & DF$grade[i]==3) age2[i] <- g3/2
  if(is.na(DF$age[i]) & DF$grade[i]==4) age2[i] <- g4/2
}

age2
DF$age2 <- round(age2)
DF


str(dataset)


# 3. 이상치(outlier) 발견과 정제
# - 정상 범주에서 크게 벗어난 값

# 1) 범주형(집단) 변수 대상 이상치 발견 및 정제
gender <- dataset$gender # 젠더 벡터 생성
gender

# 범주형에서 이상치는 보통 빈도(table)나 차트에서 발견됨 
table(gender)
# 0   1   2   5 
# 2 173 124   1 
# 0,5은 정상적인 데이터일리 없다
pie(table(gender))


# 저새끼를 정제하자 : 없앰
dataset<-subset(dataset, gender==1|gender==2)
pie(table(dataset$gender))

# 2) 연속형 변수
price<-dataset$price
length(price)
plot(price) #그림을 통해 이상치 확인
summary(price) # 요약통계를 통해 이상치 확인

# 물론 바로 족치기보단 정말 족쳐야대는지 확인하고 족쳐야한다
# 2~10만원 이 사이를 정상 범주로 가정하겠다
dataset2 <- subset(dataset, price >= 2 & price <= 10)
dim(dataset2) # 297에서 248개로
plot(dataset2$price)
boxplot(dataset2$price)
# 평균은 5.5만원쯤, 75%까지는 6만원대 밑에서 거래하더라

# dataset2 : age(20~69) 정상범주 가정
dataset3 <- subset(dataset, age >=20 & age <=69)
plot(dataset3$age)
boxplot(dataset3$age)

# 3) 이상치 발견이 어려운 경우
boxplot(dataset$price)$stats
# $stats를 붙임으로써 통계상의 정상범주를 볼 수 있음
# 그러하니 저 범위로 정상범주를 가정할 수도 있다
subset(dataset, price >=2.1 & price <=7.9) # 정상범주에에서 상하위 0.3% 거름
boxplot(subset(dataset, price >=2.1 & price <=7.9)$price)

# [실습]
library(ggplot2)
str(mpg)
hwy <- mpg$hwy
length(hwy) #234

boxplot(hwy)$stats #0.3%상에서 상위에 두 개의 이상치 발견
#정상 범주를 봤으니 정제하자

# 정제 방법1) 제거
subset(mpg, hwy >=12 & hwy <=37)
boxplot(subset(mpg, hwy >=12 & hwy <=37)$hwy)
# 두 이상치가 정제됨

# 정제 방법2) NA처리
hwy_tmp <- ifelse(mpg$hwy < 12 | mpg$hwy > 37, NA, mpg$hwy)
# 저 범위에 들어가면 na로, 아님 그대로
mpg$hwy2 <- hwy_tmp
mpg_df <- as.data.frame(mpg)
mpg_df[c('hwy', 'hwy2')]
  

# 4. 코딩 변경
# 데이터의 가독성, 척도 변경, 최초 코딩 내용 변경을 목적으로 수행 

# 1) 데이터 가독성(1,2)
# 1, 2로 끝내기보단 저게 뭘 설명하는 것인지 표시하는 게 좋을 수 있다 : 가독성
# 형식) dataset$새칼럼[조건식] <- "값"
dataset$gender2[dataset$gender==1] <- "남자"
dataset$gender2[dataset$gender==2] <- "여자"
head(dataset,10)
head(dataset2)

dataset2$resident2[dataset2$resident==1] <- "1. 서울"
dataset2$resident2[dataset2$resident==2] <- "2. 인천"
dataset2$resident2[dataset2$resident==3] <- "3. 대전"
dataset2$resident2[dataset2$resident==4] <- "4. 대구"
dataset2$resident2[dataset2$resident==5] <- "5. 시구군"
head(dataset2)

# 2) 척도 변경 : 연속 -> 범주
# 분석에 따라 범주형만 가능할 수도 있음
range(dataset2$resident)
# 20~30 : 청년층, 31~55 : 중년층, 56~ : 장년층
dataset2$age2[dataset2$age <= 30] <-"청년층"
dataset2$age2[dataset2$age > 30 & dataset2$age <= 55] <-"중년층"
dataset2$age2[dataset2$age > 55] <-"장년층"
head(dataset2)

# 3) 역코딩 : 1번으로 집계된 것은 5번으로, 5번을 1번으로
table(dataset2$survey) # 빈도수 확인
surver <- dataset2$survey
csurver <- 6 - surver # 역코딩
dataset2$survey <-csurver
table(dataset2$survey) # 빈도수 뒤집어짐


# 5. 탐색적 분석을 위한 시각화
# - 변수 간의 관계 분석

setwd("C:/ITWILL/2_rwork/Part-II")
new_data <- read.csv("new_data.csv")
dim(new_data) # 231 15
str(new_data)

# 1) 범주형(명목 / 서열) vs 범주형(명목 / 서열)
# - 방법 : 교차테이블, barplot

# 거주지역(5집단) vs 성별(2집단)
tab1 <- table(new_data$resident2, new_data$gender2)
tab1

barplot(tab1, beside = T, horiz = T, col = rainbow(5),
        main = "성별에 다른 거주지역 분포 현황",
        legend = row.names(tab1))

tab2 <- table(new_data$gender2, new_data$resident2)
tab2

barplot(tab2, beside = T, horiz = T, col = rainbow(2),
        main = "거주지역에 따른 성별 분포 현황",
        legend = row.names(tab2))

mosaicplot(tab1, col = rainbow(5),
           main = "성별에 다른 거주지역 분포 현황")
# 면적에 따른 비교가 가능, 정사각형 기준

library(ggplot2) 
# 고오급 시각화 도구 : 직업유형(범주형) vs 나이(범주형으로 바꾼 거)

# 미적 객체 생성
obj =ggplot(data = new_data, aes(x=job2, fill = age2))
# 막대차트 추가
obj + geom_bar() #기본와꾸

# 막대차트 추가
obj + geom_bar(position = "fill") # 밀도 1 기준으로 한 비율

table(new_data$job2, new_data$age2, useNA = "ifany")

# 2) 숫자형(비율) vs 범주형(명목이나 서열)
# - 방법 : boxplot, 카테고리별 통계
install.packages("lattice")
library(lattice)

# 나이(비율척도) vs 직업유형(명목)
densityplot( ~ age, groups = job2, data = new_data, auto.key = T)

# groups = 집단변수 : 각 격자 내에 그룹 효과
# auto.key = T : 범례 추가

# 3) 숫자형(비율) vs 범주형(명목) vs 범주형(명목)
# (1) 구매금액을 성별과 직급으로 분류
densityplot(~ price | factor(gender2),
            groups = position2, data = new_data,
            auto.key = T)

# factor(집단변수) : 범주의 수 만큼 격자 생성
# groups = 집단변수 : 각 격자 내의 그룹 효과

# (2) 구매금액을 직급과 성별로 분류
densityplot(~ price | factor(position2),
            groups = gender2, data = new_data,
            auto.key = T)

# 4) 숫자 vs 숫자 | 숫자 vs 숫자 vs 범주
# - 방법 : 상관계수, 산점도, 산점도 행렬

# 4-1) 숫자형(age) vs 숫자형(price)
cor(new_data$age, new_data$price) # 연산 대상에 NA가 있으면 연산이 안대지롱
# na.rm이 자동으로 뜨지 않으면 이 펑션에서는 자체적으로 가능하지 않다는 거임

new_data2 <- na.omit(new_data)
cor(new_data2$age, new_data2$price)
#매우 작은 값이 나옴 : 상관성 그닥
#0.3보다는 커야 보통 상관성이 있다고 한다
plot(new_data2$age, new_data2$price)
#그림으로 그려보아도 저래 보임

# 4-2) 숫자형 vs 숫자형 vs 범주형
# xyplot(y~x) y축 x축 순서 
xyplot(price ~ age | factor(gender2),
       data = new_data)
# 남자는 평평한 분포, 여자는 우상향 분포가 대충 보인다


# 6. 파생변수 생성
# - 기존 변수를 이용하여 새로운 변수를 만든다
 # 1. 사칙연산 
 # 2. 1:1방식 : 기존 칼럼으로 새로운 칼롬을 만든다(1개씩)
 # 3. 1:n방식 : 기준변수를 토대로 새로운 변수를 만든다.(1개에 대하여 여러개)

#고객정보 테이블
user_data <- read.csv("user_data.csv")
str(user_data)

# 1) 1:1방식 : 기존 칼럼으로 새로운 칼롬을 만든다(1개씩)
# 더미변수 : 1,2 -> 1 | 3,4 ->2
tmp <- ifelse(user_data$house_type==1 | user_data$house_type ==2, 1, 2)
user_data$house_type2 <- tmp
table(user_data$house_type2) #원래 1부터 4까지인데 2까지의 더미변수로 뜸

# 2) 1:n방식 : 기준변수를 토대로 새로운 변수를 만든다.(1개에 대하여 여러개)
# 지불정보 테이블
pay_data <- read.csv("pay_data.csv")
str(pay_data)
names(pay_data)
# user_id : 오라클에서의 외래키 느낌
# product_type, pay_method, price(얘는 계산이 가능한 비율척도)(나머지는 범주)

library(reshape2)
# dcast(데이터셋, 행 집단변수~열 집단변수, 함수)
# 이 함수 자체가 n개로 뿔려주는 기능을 하는 거임 long->wide
# 어떤 고객이 어떤 물건을 얼마만큼 산 건지를 보여줌 
# 고객별 상품 유형에 따른 구매금액 합계
product_price <- dcast(pay_data, user_id ~ product_type, sum)
# Using price as value column: use value.var to override
# 이 메시지는 오류가 아니라 저렇게 만들었다는 걍 설명임
product_price
# 1001고객은 1번 상품을 153000원 어치 구매함 2~4 상품에 대하여 구매안함
# 가독성을 증진시키기 위하여 상품유형을 바꾸자
dim(product_price) # 303 6      97명은 암 것도 안 샀구나
names(product_price) <- c("user_id", "식료품(1)", "생필품(2)", "의료(3)", "잡화(4)", "기타(5)")
head(product_price) # 확인요

product_price <- dcast(pay_data, (user_id : pay_method) ~ product_type, sum)
                      


#고객새끼의 정보를 더 연계시키고 싶다

# 3) 파생 변수 추가(join)
library(dplyr)
# 형식) left_join(데이터프레임1, 조인대상 데이터프레임2, by = '조인대상 칼럼')
user_pay_data <- left_join(user_data, product_price, by = 'user_id')
dim(user_pay_data)
head(user_pay_data)

# 4) 사칙연산
# 3번 고객의 경우 물건을 여러가지를 샀내 총합계도 추가하고 싶다
names(user_pay_data)
user_pay_data$tot_price <- user_pay_data[,7] + user_pay_data[,8] + user_pay_data[,9] + user_pay_data[,10] + user_pay_data[,11]
head(user_pay_data[7:12])
#저게 번거롭다면 #user_pay_data[,7] -> user_pay_data$'식료품(1)'