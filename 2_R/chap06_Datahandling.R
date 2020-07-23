#chap06_Datahandling

# 1. dplyr 패키지
install.packages("dplyr")
library(dplyr)
library(help="dplyr")

# 1) 파이프 연산자 : %>%
# 형식) df%>%func1()%>%func2()

iris %>% head()
head(iris)

iris %>% head() %>% filter(Sepal.Length >= 5.0)
# 150개 > 6 > 3개 관측치만 뽑아냄

install.packages("hflights")
library(hflights)
str(hflights)

# 2) tbl_df() : 콘솔 크기만큼 자료를 구성
hflights_df <- tbl_df(hflights)
# ... with 227,486 more rows, and 14 more variables: 지금 보여준 거 말고 이만큼 더있다

# 3) filter 함수 : 행단위 추출
# 형식) df %>% filter(조건식)
names(iris) # 컬럼구성이 뭐엿더라
iris %>% filter(Species == 'setosa') %>% head()
iris %>% filter(Sepal.Width > 3) %>% head()
iris_df <- iris %>% filter(Sepal.Width > 3)
str(iris_df) #서브셋을 더 편하게 만들어주는거다

hflights_df
# 필터의 원래 형식 filter(대상, 조건식)
filter(iris, Sepal.Width > 3)
filter(hflights_df, Month == 1 & DayofMonth == 1)
filter(hflights_df, Month == 1 | Month == 2)

# 4) arrange() : 정렬 함수
# 형식) df %>% arrange(컬럼명)
iris %>% arrange(Sepal.Width) %>% head() #오름차순이 기본값
iris %>% arrange(desc(Sepal.Width)) %>% head() #내림차순

# 형식) arrange(df, 컬럼명) : 월 도착시간 정렬순서
arrange(hflights_df, Month, ArrTime)

arrange(hflights_df, desc(Month), ArrTime)


# 5) select() : 열 추출
# 형식) df %>% select()
names(iris)
iris%>%select(Sepal.Length, Petal.Length, Species) %>% head()

# 형식) select(df, col1, col2, ...)
select(hflights_df, DepTime, ArrTime, TailNum, AirTime)

select(hflights_df, Year : DayOfWeek)

# 문) Month 기준으로 내림차순 정렬하고 Year, Month, AirTime 칼럼 선택하기
head(hflights_df)

select(arrange(hflights_df, desc(Month)), Year, Month, AirTime)

# 6) mutate() : 파생변수 : 기준의 변수를 가지고 새로운 변수를 만든다
# 형식) df %>% mutate(변수=함수or수식)
iris %>% mutate(diff = Sepal.Length - Sepal.Width) %>% head()

# 형식2) 직접활용 mutate(df, 변수 = 함수 or 수식)
select(mutate(hflights_df, 
       diff_delay = ArrDelay - DepDelay),
       ArrDelay, DepDelay, diff_delay
       )

# 7) summarise() 통계 출력
# 형식) df %>% summarise(변수 = 통계함수()) / 저 변수 파생변수 형태임
iris %>% summarise(col1_avg = mean(Sepal.Length), 
                   col2_sd = sd(Sepal.Width))

# ) 서머라이즈 단독 사용 summarise(df, 변수 = 통계함수())
summarise(hflights_df, 
          delay_avg = mean(DepDelay, na.rm=T),
          delay_tot = sum(DepDelay, na.rm=T)
          )
# 출발지연시간 평균/ 합계를 구했음

str(hflights)

hflights_df


# 8) group_by(dataset, 집단변수)
# 형식) df %>% group_by(집단변수)
names(iris)
table(iris$Species) 
grp<-iris%>%group_by(Species) # Groups:   Species [3] 스피시스로는 집단이 3개다

summarise(grp, mean(Sepal.Length)) # 요약통계 및 더 편리한 집계
# 1 setosa                     5.01
# 2 versicolor                 5.94
# 3 virginica                  6.59

summarise(grp, sd(Sepal.Length))

# group_by 실습
install.packages("ggplot2")
library(ggplot2)

data("mtcars") # 자동차 연비
head(mtcars)
str(mtcars) # 저새끼들 다 집단변수임
table(mtcars$cyl) # 각 변수 안에서 또 집단이 나뉨
table(mtcars$gear)

# group : cyl
grp<-group_by(mtcars, cyl)

# 각 cyl 집단별 연비 평균
summarise(grp, mpg_avg = mean(mpg),
               mpg_sd = sd(mpg))
## 실린더 적을수록 연비가 좋은듯하구만

# 각 gear 집단별 무게(wt) 평균 표준편차
grp<-group_by(mtcars, gear)
summarise(grp, wt_avg = mean(wt),
          wt_sd = sd(wt))
## 기어가 적은 애들이 무거운듯

# 두 집단변수 -> 그룹화
grp2 <- group_by(mtcars, cyl, gear) # cyl로 1차 그루핑, 기어로 2차)
summarise(grp2, mpg_avg = mean(mpg), mpg_sd = sd(mpg))


# 형식) group_by(dataset, 집단변수)

# 예제) 각 항공기별 비행편수가 40편 이상이고,
# 평균 비행거리가 2000마일 이상인 경우의 평균도착지연시간을 확인하시오
  #1) 항공기별 그룹화
  str(hflights)
  planes <- group_by(hflights, TailNum)
  planes
  
  #2) 항공기별 요약통계 : 1차적으로 비행편수 그담에 평균 비행거리, 평균 도착지연시간
  planes_state <- summarise(planes, count = n(),
                  Dist_avg = mean(Distance, na.rm = T),
                  Delay_avg = mean(ArrDelay, na.rm = T))
  
  planes_state
  ## 컬럼명을 보면서 내가 의도했던 순서가 맞는지 확인
  ## 문제를 다시 보고 더 필요한 조건을 찾기
  
  #3) 항공기별 요약 통계 조건에 맞게 필터링
  filter(planes_state, count >= 40 & Dist_avg >= 2000)
  


# 2. reshape2
  install.packages("reshape2")
  library(reshape2)

# 1) dcast() : long -> wide

data <- read.csv(file.choose())
# Date : 구매일자
# ID : 고객 구분자
# Buy : 구매수량

# 형식 ) dcast(dataset, row ~ col(행과 열의 갯수를 지정), func)
wide <- dcast(data, Customer_ID ~ Date, sum)
wide

library(ggplot2)
data(mpg) # 자동차 연비
str(mpg)

mpg_df <- as.data.frame(mpg)
mpg_df
str(mpg_df)

# 집단화 가능한 애들을 뽑아야
mpg_df <- select(mpg_df, c(cyl, drv, hwy))
head(mpg_df)
# 교차셀에 hwy 합계
tab <- dcast(mpg_df, cyl~drv, sum)
tab

# 교차셀에 hwy 출현 건수
tab2 <- dcast(mpg_df, cyl~drv, length)
tab2

# 교차분할표
table(행집단변수, 열집단변수)
table(mpg_df$cyl, mpg_df$drv)
## dcast로 건수 구하는거나 이거나 같은 결과다

unique(mpg_df$cyl) # 범주가 무엇인가 확인
unique(mpg_df$drv) # 즉 무슨 집단이 있는가


# 2) melt() : wide -> long (dcast와 반대)
long <- melt(wide, id="Customer_ID") # 아까 옆으로 폈던 데이터를 아래로 폈음
long
# Customer_ID : 기준 칼럼
# variable : 열이름
# value : 교차셀의 값

names(long) <- c("User_ID", "Date, Buy")
long

# example
data("smiths")

# wide -> long
long <- melt(smiths, id = 'subject')
long

long2 <- melt(smiths, id = 1:2)
long2

# long -> wide
wide <- dcast(long, subject ~ ... )
wide

# 3. acast(dataset, 행~열~면)
data("airquality")
str(airquality)

table(airquality$Month)
# 5~9월 동안의 자료구만
table(airquality$Day)
dim(airquality)

# wide -> long
air_melt <- melt(airquality, id = c("Month", "Day"), na.rm=T)
air_melt
dim(air_melt)
table(air_melt$variable)

# [일,월, variable] -> [행 열 면]
# acast(dataset, Day ~ Month ~ variable)
air_arr3d  <- acast(air_melt, Day ~ Month ~ variable)
dim(air_arr3d) # 31 5 4

# 오존 data
air_arr3d[,,1]

# 태양열 data
air_arr3d[,,2]

###### 추가내용 ######
# 4. URL 만들기
## 1) base URL
   baseUrl <- "http://www.sbus.or.kr/2018/lost/lost_02.htm?"

## 2) page query 추가
# http://www.sbus.or.kr/2018/lost/lost_02.htm?Page=1
no <- 1:5
library(stringr)
page <- str_c('page=', no)
page

# outer(x(1), y(n), func) 1:다 결합시켜주는 함수
page_url <- outer(baseUrl, page, str_c)
page_url
dim(page_url)
                       
# reshape : 2d -> 1d
page_url <- sort(as.vector(page_url))
page_url

# 3) sear query 추가
# http://www.sbus.or.kr/2018/lost/lost_02.htm?Page=2&search=&selectstate=&bus_no=&sear=2
no <- 1:3
sear <- str_c("&sear=", no)
final <- outer(page_url, sear, str_c)
final <- sort(as.vector(final))
final



