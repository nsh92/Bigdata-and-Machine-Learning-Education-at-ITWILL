
# 차트 데이터 생성
chart_data <- c(305,450, 320, 460, 330, 480, 380, 520) 
names(chart_data) <- c("2016 1분기","2017 1분기","2016 2분기","2017 2분기","2016 3분기","2017 3분기","2016 4분기","2017 4분기")
str(chart_data)
chart_data
max(chart_data)

# 1.이산변수 시각화
# (1) 막대차트
?barplot
barplot(chart_data, ylim=c(0,600), 
        main="2016년 vs 2017년 판매현황",
        col=rainbow(8))
# 가로막대
barplot(chart_data, xlim=c(0,600), horiz=T,
        main="2016년 vs 2017년 판매현황",
        col=rainbow(8))

# 1행 2열 구조 한 화면에 차트 두개
par(mfrow=c(1,2)) # 1행 2열 그래프 보기
VADeaths
str(VADeaths)
row_names <- row.names(VADeaths)
row_names
col_names<- colnames(VADeaths)
col_names
max(VADeaths) 
min(VADeaths)

#beside=false horiz=false
barplot(VADeaths, beside = F, 
        horiz = F,
        main = "버지니아 사망비율",
        col = rainbow(4))

#beside=true horiz=false
barplot(VADeaths, beside = T, 
        horiz = F,
        main = "버지니아 사망비율",
        col = rainbow(4))

par(mfrow=c(1,1)) # 이래하면 다시 한개만 보기

# 범례추가
legend(x=4, y=200, legend = row_names, fill=rainbow(5))

# (2) 점차트
dotchart(chart_data, color=c("green","red"), lcolor="black",
         pch=1:2, labels=names(chart_data), xlab="매출액",
         main="분기별 판매현황 점 차트 시각화", cex=1.2)

# (3) 원차트 파이차트
pie(chart_data, labels = names(chart_data),
    border='blue', col=rainbow(8), cex=1.2)

# 차트에 제목을 추가하는 별도의 함수
title("2014~2015년도 분기별 매출현황")

table(iris$Species)
pie(table(iris$Species),
    col = rainbow(3),
    main = "아이리스 꽃의 종")

# 2. 연속변수 시각화
# - 시간, 길이 등의 연속성을 갖는 변수
# 1) 상자 그래프 시각화
summary(VADeaths)
boxplot(VADeaths)
quantile(VADeaths) #사분위 나누기

range(iris$Sepal.Width) # 2.0 ~ 4.4

# 2) 히스토그램 시각화
hist(iris$Sepal.Width, 
     xlab="iris$Sepal.Width",
     col="mistyrose",
     main="iris 꽃받침 넓이 histogram",
     xlim=c(2.0, 4.5))


par(mfrow=c(1,2))

hist(iris$Sepal.Width, 
     xlab="iris$Sepal.Width",
     col="green",
     main="iris 꽃받침 넓이 histogram", 
     xlim=c(2.0, 4.5))

hist(iris$Sepal.Width, 
     xlab="iris$Sepal.Width",
     col="mistyrose",
     freq = F,
     main="iris 꽃받침 넓이 histogram", 
     xlim=c(2.0, 4.5))

par(mfrow=c(1,1))

hist(iris$Sepal.Width, 
     xlab="iris$Sepal.Width",
     col="mistyrose",
     freq = F,
     main="iris 꽃받침 넓이 histogram", 
     xlim=c(2.0, 4.5))

# 밀도 분포곡선도 추가하고싶다
lines(density(iris$Sepal.Width), col="red")

# 정규분포 만들어보기
n <- 10000
x <- rnorm(n,mean = 0, sd = 1)
hist(x, freq = F)
lines(density(x), col="red")

# 3) 산점도 시각화
x<-runif(n=15,min=1,max=100)
y<-runif(n=15,min=5,max=120)
plot(x)
plot(x,y) #(y~x)
plot(y,x)

#col 속성
head(iris,10)
plot(iris$Sepal.Length, iris$Petal.Length,
     col = iris$Species)
#색깔이 범주인 산점도가 만들어짐


par(mfrow=c(2,2)) # 2행 2열 차트 그리기
price <- rnorm(10)
plot(price, type="l") # 유형 : 실선
plot(price, type="o") # 유형 : 원형과 실선(원형 통과)
plot(price, type="h") # 직선
plot(price, type="s") # 꺾은선

plot(price, type="o", pch=5) # 빈 사각형
plot(price, type="o", pch=15)# 채워진 마름모
plot(price, type="o", pch=20, col="blue") #color 지정
plot(price, type="o", pch=20, col="orange", cex=1.5) #character expension(확대)

# 만능차트
methods(plot) # 저 기능들이 plot에 있다

# plot.ts : 시계열자료
WWWusage
plot(WWWusage)

#plot.lm : 회귀
install.packages("UsingR")
library(UsingR)
library(help="UsingR")
data(galton)
str(galton)
# 유전학자 갈톤이 만든 데이터셋 : 회귀란 말을 제안함
model <- lm(child ~ parent, data=galton)
plot(model)

# 4) 산점도 행렬 : 변수 간의 비교
pairs(iris[-5])

# 5) 차트 파일 저장
setwd("C:/itwill/2_Rwork/output") # 폴더 지정

jpeg("iris.jpg", width=720, height=480) # 픽셀 지정 가능
plot(iris$Sepal.Length, iris$Petal.Length, col=iris$Species)
title(main="iris 데이터 테이블 산포도 차트")
dev.off() # 장치 종료

# 꽃의 종별 산점도 행렬
table(iris$Species)
pairs(iris[iris$Species=='setosa',1:4])
pairs(iris[iris$Species=='virginica',1:4])

#########################
### 3차원 산점도 
#########################
install.packages('scatterplot3d')
library(scatterplot3d)

# 꽃의 종류별 분류 
iris_setosa = iris[iris$Species == 'setosa',]
iris_versicolor = iris[iris$Species == 'versicolor',]
iris_virginica = iris[iris$Species == 'virginica',]

# scatterplot3d(밑변, 오른쪽변, 왼쪽변, type='n') # type='n' : 기본 산점도 제외 
d3 <- scatterplot3d(iris$Petal.Length, iris$Sepal.Length, iris$Sepal.Width, type='n')

d3$points3d(iris_setosa$Petal.Length, iris_setosa$Sepal.Length,
            iris_setosa$Sepal.Width, bg='orange', pch=21)

d3$points3d(iris_versicolor$Petal.Length, iris_versicolor$Sepal.Length,
            iris_versicolor$Sepal.Width, bg='blue', pch=23)

d3$points3d(iris_virginica$Petal.Length, iris_virginica$Sepal.Length,
            iris_virginica$Sepal.Width, bg='green', pch=25)
