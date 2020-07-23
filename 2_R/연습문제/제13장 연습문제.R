# chap13_Ttest_Anova(연습문제)

#############################################
# 추론통계분석 - 1-1. 단일집단 비율차이 검정
#############################################

# 01. 중소기업에서 생산한 HDTV 판매율을 높이기 위해서 프로모션을 진행한 결과 
# 기존 구매비율 15% 보다 향상되었는지를 각 단계별로 분석을 수행하여 검정하시오.


#연구가설(H1) : 기존 구매비율과 차이가 있다.
#귀무가설(H0) : 기존 구매비율과 차이가 없다.

#조건) 구매여부 변수 : buy (1: 구매하지 않음, 2: 구매)

#(1) 데이터셋 가져오기
setwd("C:/ITWILL/2_Rwork/Part-III")
hdtv <- read.csv("hdtv.csv", header=TRUE)

# (2) 빈도수와 비율 계산
buy <- hdtv$buy
table(buy)
prop.table(table(buy))

# (3)가설검정
binom.test(x=10, n=50, p=0.15, alternative = 'two.sided', conf.level=0.95)
# p-value = 0.321 > 0.05 # 귀무가설 채택
# 95 percent confidence interval:
#   0.1003022 ~ 0.3371831
# probability of success : 0.2 -> 실제성공확률
# 구매비율은 15%를 넘지 못한다

#################################################
# 추론통계학 분석 - 1-2. 단일집단 평균차이 검정
#################################################

# 02. 우리나라 전체 중학교 2학년 여학생 평균 키가 148.5cm로 알려져 있는 상태에서 
# A중학교 2학년 전체 500명을 대상으로 10%인 50명을 표본으로 선정된 데이터 셋을 이용하여
# 모집단의 평균과 차이가 있는지를 각 단계별로 분석을 수행하여 검정하시오.

#(1) 데이터셋 가져오기
sheight<- read.csv("student_height.csv", header=TRUE)

# (2) 기술통계량 평균 계산
height <- sheight$height
length(sheight$height)
mean(sheight$height)
hist(height) # 이것만 봐도 정규성이 아닌 티가 남

# (3) 정규성 검정
shapiro.test(height)
# ㄴㄴ 정규분포아님

# (4) 가설검정 
wilcox.test(height, mu=148.5)
# V = 826, p-value = 0.067 > 0.05 귀무가설 채택
# 중학교 2학년 여학생 평균 키는 모평균148.5cm와 차이가 없다고 볼 수 있다

#################################################
# 추론통계학 분석 - 2-1. 두집단 비율 차이 검정
#################################################

# 03. 대학에 진학한 남학생과 여학생을 대상으로 진학한 대학에 
# 대해서 만족도에 차이가 있는가를 검정하시오.

# 힌트) 두 집단 비율 차이 검정
#  조건) 파일명 : two_sample.csv, 변수명 : gender(1,2), survey(0,1)
# gender : 남학생(1), 여학생(2)
# survey : 불만(0), 만족(1)
# prop.test('성공횟수', '시행횟수')

two <- read.csv("two_sample.csv")
str(two)

boy <- subset(two, gender == 1)
girl <- subset(two, gender == 2)

sur_boy <- boy$survey
sur_girl <- girl$survey
length(sur_boy)
length(sur_girl)

var.test(sur_boy, sur_girl)
wilcox.test(sur_boy, sur_girl)
# p-value = 0.2163 이므로 0.05보다 작음
# 성별에 따른 만족도에 유의미한 차이가 있음

##################################################
# 추론통계학 분석 - 2-2. 두집단 평균 차이 검정
##################################################

# 04. 교육방법에 따라 시험성적에 차이가 있는지 검정하시오.

#힌트) 두 집단 평균 차이 검정
#조건1) 파일 : twomethod.csv
#조건2) 변수 : method : 교육방법, score : 시험성적
#조건3) 모델 : 교육방법(명목)  ->  시험성적(비율)
#조건4) 전처리 : 결측치 제거 : 평균으로 대체 


two1 <- read.csv("twomethod.csv")
str(two1)

meth1 <- subset(two1, method == 1)
meth2 <- subset(two1, method == 2)
score1 <- meth1$score
score2 <- meth2$score

var.test(score1, score2)
# p-value =0.8494 > 0.05
t.test(score1, score2)
# p-value = 1.303e-06 < 0.05 이므로 교육방법에 따른 시험성적에 유의미한 차이가 없다능


# 05. iris 데이터셋을 이용하여 다음과 같이 분산분석(aov)을 수행하시오.
# 독립변수 : Species(집단변수)
# 종속변수 : 1번 컬럼 ~ 4번 컬럼 중에서 전제조건을 만족하는 변수 선택
# 분산분석 수행 -> 사후검정 해석
str(iris)

bartlett.test(iris$Sepal.Length, iris$Species)
bartlett.test(iris$Sepal.Width, iris$Species) # p-value = 0.3515 : 전제조건 만족
bartlett.test(iris$Petal.Length, iris$Species)
bartlett.test(iris$Petal.Width, iris$Species)

# p-value = 0.3515 : 전제조건 만족
# 이래야 anova를 할만한 동질성 검증을 만족하는 것임

x <- iris$Sepal.Width
y <- iris$Species

result <- aov(Sepal.Width ~ Species, data = iris)
summary(result)
# 매우 유의미한 수준에서 적어도 한 집단의 평균 차이가 있다

TukeyHSD(result)
# 95% 신뢰수준에서 3집단 모두 평균의 차이를 보인다.
# 꽃잎의 넓이 변수는 versicolor와 setosa 집단에서 가장 큰 평균 차이를 보인다

plot(TukeyHSD(result))

# method(plot)
# 이거 치면 plot으로 뭘 볼 수 있나 리스트가 뜨는데
# TukeyHSD도 저 리스트에 있어서 볼 수 있음

library(dplyr) # df %>% function()
# 이 파이프 메쏘드로 평균차이검정을 해볼까

iris %>% group_by(Species) %>% summarise(age = mean(Sepal.Width))
2.77 - 3.43 = -0.66 # Tukey에서의 diff값과 일치
2.97 - 3.43 = -0.46
