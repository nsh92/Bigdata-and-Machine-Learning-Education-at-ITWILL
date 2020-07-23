##################################################
# chap14. 상관관계 분석(Correlation Analysis)
##################################################
# - 변수 간 관련성 분석 방법 
# - 관련함수 : cor(), cov(), cov2cor() 

product <- read.csv("C:/itwill/2_rwork/Part-III/product.csv", header=TRUE)
head(product) # 친밀도 적절성 만족도(등간척도 - 5점 척도)

# 기술통계량
summary(product) # 요약통계량

sd(product$제품_친밀도); sd(product$제품_적절성); sd(product$제품_만족도)
# 변수 간의 상관관계 분석 
# 형식) cor(x,y, method) # x변수, y변수, method(pearson): 방법

# 1) 상관계수(coefficient of correlation) : 두 변량 X,Y 사이의 상관관계 정도를 나타내는 수치(계수)
cor(product$제품_친밀도, product$제품_적절성) # 0.4992086 -> 다소 높은 양의 상관관계
# 앞놈이 엑스, 뒷놈이 와이 뒤엔 method("pearson") 생략댐
cor(product$제품_친밀도, product$제품_만족도) # 0.467145 -> 다소 높은 양의 상관관계

# 전체 변수 간 상관계수 보기
cor(product, method="pearson") # 피어슨 상관계수 - default
# 이 와꾸를 상관계수 행렬이라 함
# 대각선을 두고 자기 상관계수라 함
# 대각선을 제외하고 가장 큰 놈이 제일 유의미 : 적절성+만족도


# 방향성 있는 색생으로 표현 - 동일 색상으로 그룹화 표시 및 색의 농도 
install.packages("corrgram")   
library(corrgram)
corrgram(product) # 색상 적용 - 동일 색상으로 그룹화 표시
corrgram(product, upper.panel=panel.conf) # 수치(상관계수) 추가(위쪽)
corrgram(product, lower.panel=panel.conf) # 수치(상관계수) 추가(아래쪽)

# 차트에 곡선과 별표 추가
install.packages("PerformanceAnalytics") 
library(PerformanceAnalytics) 

# 상관성,p값(*),정규분포 시각화 - 모수 검정 조건 
chart.Correlation(product, histogram=, pch="+") 

# spearman : 서열척도 대상 상관계수

# 2) 공분산(covariance) : 두 변량 X,Y의 관계를 나타내는 양
cor(product)
cov(product)
# 얘도 대각선은 무시

cov2cor(cov(product)) # 공분산 행렬 -> 상관계수 행렬 변환

# 상관계수 vs 공분산
# 공통점 : 두 확률변수의 관계를 나타내는 값이다
# 상관계수 : 크기(양)와 방향(- +)을 제공한다
# 공분산 : 크기(양) 제공한다, 방향은 ㄴㄴ함
# 결국 공분산을 쓰더라도 방향까지 보려면 상관계수로 또 돌려야함

x <- product$제품_적절성
y <- product$제품_만족도

Cov_xy <- mean((x - mean(x)) * (y - mean(y)))
# 위 cov(product) 값과 다르지 않음

r = Cov_xy / (sd(x)*sd(y))
# 위 cor(product) 값과 다르지 않음

# 공분산 : 크기 영향을 매우 많이 받는다.
score_iq <- read.csv(file.choose())
str(score_iq)
# iq가 다른 변수들과 상관이 있는가
cor(score_iq[-1])
# score와 academy와 높은 상관성
cov(score_iq[-1])
# cor에 비해서 academy가 확실히 작은 값이 나옴
# 이래서 상관분석 사용이 더 선호됨


