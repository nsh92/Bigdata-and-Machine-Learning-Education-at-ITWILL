#################################
## <제11장 연습문제>
################################# 

#01. descriptive.csv 데이터 셋을 대상으로 다음 조건에 맞게 빈도분석 및 기술통계량 분석을 수행하시오

setwd("C:/ITWILL/2_Rwork/Part-III")
data <- read.csv("descriptive.csv", header=TRUE)
head(data) # 데이터셋 확인

# 조건1) 명목척도 변수인 학교유형(type), 합격여부(pass) 변수에 대해 빈도분석을 수행하고 
# 결과를 막대그래프와 파이차트로 시각화 
type <- data$type
pass <- data$pass

t1 <- table(type)
barplot(t1)
t2 <- table(pass)
barplot(t2)

# 조건2) 비율척도 변수인 나이 변수에 대해 요약치(평균,표준편차)와 비대칭도(왜도와 첨도)
# 통계량을 구하고, 히스토그램으로 비대칭도 설명
age <- data$age
mean(age)
sd(age)
skewness(age)
kurtosis(age)
hist(age)

# 조건3) 나이 변수에 대한 밀도분포곡선과 정규분포 곡선으로 정규분포 검정
hist(age, freq=F)
lines(density(age), col='blue')
range(age)
x <- seq(38,75,0.1)
curve(dnorm(x, mean(age), sd(age)), col='red', add=T)
