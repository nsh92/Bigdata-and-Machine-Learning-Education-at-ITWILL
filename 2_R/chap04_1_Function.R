#chap04_2_Function

# 1. 사용자 정의함수

# 형식)
# 함수명 <- function([인수]){
#   실행문
#   실행문
#   [return 값]
# }

# 1) 매개변수없는 함수
f1 <- function(){
  cat('f1 함수')
}
# 함수 정의만 했지 호출하지 않으면 쓰일 일이 없음

f1() # 이렇게 함수를 호출함

# 2) 매개변수 있는 함수
f2 <- function(x){
  x2 <- x^2
  cat('x2=', x2)
}

f2(10) # 실인수를 넣음

# 3) 리턴이 있는 함수
f3 <- function(x,y){
  add <- x+y
  return(add) #계산된 add를 호출하는 기능
}

f3(10,5)

#함수 호출 -> 반환값
add_re<-f3(10,5)

num<-1:10
tot_func <- function(x){
  tot <- sum(x)
  return(tot)
}

tot_re <- tot_func(num)
tot_re

avg <- tot_re/length(num)
avg

# 문) 사칙연산이 가능한 calc함수 정의하기
#100 + 20 = 120
#100 - 20 = 80
#100 * 20 = 2000
# 100 / 20 = 5

x<-100
y<-20

calc <- function(x,y){
  add <- x+y
  sub <- x-y
  mul <- x*y
  div <- x/y
  cat(x, '+', y, '=', add, '\n')
  cat(x, '-', y, '=', sub, '\n')
  cat(x, '*', y, '=', mul, '\n')
  cat(x, '/', y, '=', div, '\n')
  calc_df <- data.frame(add,sub,mul,div)
  #return(add,sub,mul,div) 이렇게 하면 오류 발생
  return(calc_df)
  }  

calc(100,20)

df <- calc(100,20)
df

# 구구단의 단을 인수 받아서 구구단 출력하기
gugu <- function(dan){
  cat('***',dan,'단 ***\n')
  for(i in 1:9){
    cat(dan, '*', i, '=', dan*i, '\n')
  }
}

gugu(8)
gugu(2)


state <- function(fname, data){
  switch(fname,
         SUM = sum(data),
         AVG = mean(data),
         VAR = var(data),
         SD = sd(data)
         )
}
#니가 원하는 함수를 고르면 그거에 맞게 연산시켜주겠다는 함수
data <- 1:10
state("SUM", data)
state("AVG", data)
state("VAR", data)
state("SD", data)

# 결측치(NA) 처리 함수
na<- function(x){
 #1. NA제거
 x1 <- na.omit(x)
 cat('x1 = ', x1, '\n')
 cat('x1 = ', mean(x1), '\n')
  #2. NA -> 평균 취급
 x2 <- ifelse(is.na(x), mean(x, na.rm=T), x)
 cat('x2 = ', x2, '\n')
 cat('x2 = ', mean(x2),'\n')
 #3. NA -> 0
 x3 <- ifelse(is.na(x), 0, x)
 cat('x3 = ', x3, '\n')
 cat('x3 = ', mean(x3))
}

x <- c(10,5,4,NA,2,6,3,NA,7,5,8,10)
length(x)
mean(x, na.rm=T)
na(x)


###################################
### 몬테카를로 시뮬레이션 
###################################
# 현실적으로 불가능한 문제의 해답을 얻기 위해서 난수의 확률분포를 이용하여 
# 모의시험으로 근사적 해를 구하는 기법

# 동전 앞/뒤 난수 확률분포 함수 
coin <- function(n){
  r <- runif(n, min=0, max=1)
  #print(r) # n번 시행 
  
  result <- numeric()
  for (i in 1:n){
    if (r[i] <= 0.5)
      result[i] <- 0 # 앞면 
    else 
      result[i] <- 1 # 뒷면
  }
  return(result)
}


# 몬테카를로 시뮬레이션 
montaCoin <- function(n){
  cnt <- 0
  for(i in 1:n){
    cnt <- cnt + coin(1) # 동전 함수 호출 
  }
  result <- cnt / n
  return(result)
}

montaCoin(5)

montaCoin(1000)
montaCoin(10000)


# 중심극한정리 : 시행횟수가 많아질수록 근사해진다


# 2. R의 주요 내장 함수

# 2-1) 기술통계함수 

vec <- 1:10          
min(vec)                   # 최소값
max(vec)                   # 최대값
range(vec)                  # 범위
mean(vec)                   # 평균
median(vec)                # 중위수
sum(vec)                   # 합계
prod(vec)                  # 데이터의 곱
#1*2*3*4*5*6*7*8*9*10
summary(vec)               # 요약통계량 

rnorm(10) # 평균은 0, 표준편차1에 수렴하도록 난수 생성
sd(rnorm(10))      # 표준편차 구하기
factorial(5) # 팩토리얼=120
sqrt(49) # 루트

install.packages('RSADBE')
library(RSADBE)
library(help='RSADBE')
data(Bug_Metrics_Software)
str(Bug_Metrics_Software)
# 자료구조 : num [1:5, 1:5, 1:2] 행 열 면 3차원
Bug_Metrics_Software[,,1] # 1면 열어라
Bug_Metrics_Software[,,2] # 2면 열어라
#이런 걸 가져다 행단위, 열단위 계산을 하고싶더라

rowSums(Bug_Metrics_Software[,,1]) #행단위 합계 : 소프트웨어별 버그수 합계
colSums(Bug_Metrics_Software[,,1]) #열단위 합계 : 버그별 소프트웨어 합계
rowMeans(Bug_Metrics_Software[,,1]) # 행 평균
colMeans(Bug_Metrics_Software[,,1]) # 열 평균

# 저 3차원 다루는 거에서 새로운 면을 만들어 넣고싶다
bug<-Bug_Metrics_Software
bug.new <- array(bug,dim=c(5,5,3)) # 기존의 구조와 다르지 않음
dim(bug.new)
bug.new[,,3] = bug[,,1]-bug[,,2]
bug.new

# 2-2) 반올림 관련 함수 
x <- c(1.5, 2.5, -1.3, 2.5)
round(mean(x)) # 1.3 -> 1
ceiling(mean(x)) # x보다 큰 정수 
floor(mean(x)) # 1보다 작은 정수 


# 3. 난수 생성과 확률분포
# 3-1) 정규분포를 따르는 난수 - 연속확률분포(실수형)
# 형식) rnorm(n, mean=0, sd=1) 0과 1은 기본설정 바꾸려면 바꾸면댐
n<-1000
r<-rnorm(n, mean=0,sd=1)
mean(r)
sd(r)
hist(r) #대칭성

# 3-2) 균등분포를 따르는 난수 - 연속확률분포
# 형식) runif(n,min=,max=) 생략하면 0, 1
r2 <- runif(n, min = 0, max=1)
r2
hist(r2) # 비슷비슷하게끔 생성됨

# 3-3) 이항분포를 따르는 난수 - 이산확률분포 - 정수형데이터
set.seed(123)
n<-10
r3<-rbinom(n,size=1,0.5)
r3
#셋 시드를 미리 설정하면 같은 항상 결과가 나옴

r3<-rbinom(n,size=1,0.25)
r3
 
# 3-4) sample
sample(10:20,5)
sample(c(10:20, 50:100), 10)

# train(70%)/test(30%) 데이터셋
dim(iris)
idx<-sample(nrow(iris), nrow(iris)*0.7)
idx # 행번호를 추출한셈
range(idx)
length(idx)
train<-iris[idx,] #학습데이터
test<-iris[-idx,] #검증데이터

dim(train)
dim(test)
#이런 것을 홀드아웃 방식이라 함

# 4. 행렬연산 내장함수

x<-matrix(1:9, nrow=3, byrow=T)
x # 3행 3열
y<-matrix(1:3, nrow=3)
y # 3향 1열

# x %*% y : 행렬곱
x;y
z <- x %*% y
z
# 행렬곱 전제조건
# 1. x아 y가 모두 행렬이어야함
# 2. x(열)=y(행)이어야함 : 수일치










