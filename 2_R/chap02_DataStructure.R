# chap02_DataStructure

# 자료 구조의 유형 : 5가지
# 1. 벡터 자료구조
# - 동일한 자료형을 갖는 1차원 배열 구조
# - 벡터 생성 함수 : c(), seq(), rep() 각 형식이 다름

# (1) c()
x <- c(1, 3, 5, 7)
y <- c(3, 5)
length(x)
length(y)

# 집합 관련 함수 base패키지
union(x,y)     #합집합 x+y
setdiff(x,y)   #차집합 x-y
intersect(x,y) #교집합

# 벡터 변수 유형
num <- 1:5 # c(연속정수)
num
num <- c(-10:5) #이렇게도 가능
num
num <- c(1,2,3,"4") #반드시 동일한 자료형만 갖는다
num<- -1:3
num

# 벡터 원소 이름 지정 가능
names <- c("홍길동", "이순신", "강감찬")
names
age <- c(35,45,55)
age
names(age) <- names
age # 벡터 원소에 이름을 붙이게 됐음, 하지만 실제 데이터는 숫자만이고 이름만 붙였을 뿐임
mode(age)
mean(age)
str(age) #특정 객체의 자료구조 제공
#Named num [1:3] 35 45 55                                       : 얘낸 데이터고
#- attr(*, "names")= chr [1:3] "홍길동" "이순신" "강감찬"       : 데이터에 이름을 붙였다

# 2) seq()
help("seq")
num <- seq(1, 10, by=2)
num # 13579

num2 <- seq(10, 1, by = -2)
num2 #10에서 2씩 작아짐

# 3) rep()
?rep # rep(x, ...) : 객체를 집어넣고 이 객체를 몇 번 반복할까 개념
     # rep.int(x, times)
     # rep_len(x, length.out)

rep(1:3, times=3)
#123123123
rep(1:3, each=3)
#111222333
rep(num, times=2)
rep(num, each=2)

# 색인(index) : 저장 위치
#하나의 객체의 여러 원소들이 저장함
#각 원소에 대하여 인덱스를 활용하여 찾아낼 수 있다

a <- 1:50
a # 조회하면 전체 원소가 출력댐 하지만 특정 원소를 보고싶다
a[10] #10번째 원소 조회
a[10:20] #10번부터 20번 까지 조회 , :는 연속을 의미
a[10:20, 30:35] #오류 발생 : incorrect number of dimensions
                # 차원은 콤마로 구분할 수 없다. 콤마는 행과 열(2차원)을 구분하는 용도이기 때문
a[c(10:20,30:35)] # c로 묶어줘야 가능해짐

# 함수 이용
length(a) # 길이 = 원소 개수
a[10:(length(a)-5)] # length(a)-5 = 50-5, 저렇게 가로 안 묶어주면 앞의 10에도 5가 빼짐
a[seq(2, length(a), by=2)]

# 특정 원소 제외(-)
a[-c(20:30)] # 20:30 제외되어 출력
a[-(20:30)]
a[-c(15,25,30:35)]

# 조건식(boolean)
a[a>=10 & a<=30] # & = and
a[a>=10 | a<=30] # | = or
a[!(a>=10)] # ! = not      이 세개를 3대 연산자라 함

# 2. Matrix 자료구조
# - 동일한 자료형을 갖는 2차원 배열구조
# - 생성 함수 : matrix(), rbind(), cbind()
# - 처리함수 : apply()

# (1) Matrix
m1 <- matrix(data=c(1:5))  # 1차원 -> 2차원(행:n, 열:1)
m1
dim(m1) # 5x1
mode(m1) # numeric - 자료형
class(m1) # matrix - 자료구조

m2 <- matrix(data = c(1:9), nrow=3, ncol=3, byrow=T)
m2 
dim(m2) # 3x3

# (2) rbind
x <- 1:5
y <- 6:10
x
y
m3 <- rbind(x, y)
m3
dim(m3) # 2X5=10

# (3) cbind()
m4 <- cbind(x, y)
m4
dim(m4) # 5X2=10

# ADsP 적용
# xy <- rbind(x,y) 다음 보기 중 틀린 건? 
# 1. xy[1,]는 x와 같다.
# 2. xy[,1]는 y와 같다.
# 3. dim(xy)는 2X5이다.
# 4. class(xy)는 matrix이다. 
# 답은 2번
 
# 색인(index) : matrix
# 형식) object[row, column]
m5 <- matrix(data = c(1:9), nrow=3, ncol=3)
m5

# 특정 행, 열 색인
m5[1,]
m5[,1]
m5[2:3,1:2]
m5[1,2:3]
m5[2,3]

# 마이너스 속성
m5[-2,] #2행 제외한다
m5[,-3] #3열 제외한다
m5[,-c(1,3)] # 2개 이상 제외

# 열(컬럼=변수=변인)에 이름 붙이기
colnames(m5) <- c("one", "two", "three")
m5

m5[, 'one'] #열이름으로 물어볼 수 있게 된다.
m5[,'one':'two'] #근대 콜론으로 구분, 범위지정은 안댐 이 작업은 숫자로 해야댐
m5[,1:2]

m5[,"one"]

# broadcast 연산
# - 작원 차원 -> 큰 차원 쪽으로 늘어나서 연산을 수행하는 과정

x <- matrix(1:12, nrow =4, ncol =)
dim(x)
x

# 1) scala(0) vs matrix(2)
# 스칼라는 차원이랑 상관이 없는 걍 상수
0.5 * x

# 2) vactor(1) vs Matrix(2)
y <- 10:12
y + x
x + y

# 3) 동일한 모양
x + x

# 4) 전치행렬 : 행->열, 열->행
x
t(x) #요거임

# 처리 함수 : apply()
help(apply)
#apply(X, MARGIN(1/2), FUN, ...)
x
apply(x, 1, sum) #x를 대상으로 행 마다의 합계를 구하라
apply(x, 2, mean) #x를 대상으로 열 마다의 평균을 구하라
apply(x, 1, var) #분ㅋ산ㅋ
apply(x, 1,sd) #표ㅋ준ㅋ편ㅋ차ㅋ

# 3. Array 자료구조
# - 동일한 자료형을 갖는 3차원 배열구조
# - 생성 함수 : array()
help("array")

#1차원의 데이터를 3차원으로 만드는 과정
arr <- array(data=c(1:12), dim=c(3,2,2))
arr
dim(arr) # 3(행) 2(열) 2(면)

# 어레이에 대한 인덱스(색인) : 좌표가 3개로 표현됨
arr[,,2] # 2면


data()
data("iris3")
iris3
dim(iris3) # 50 4 3 전체 데이터의 수 = 600개
# 꽃 종류 3종에 대한 각 데이터를 나타냄

iris3[,,1] # 꽃의종1
iris3[10:20,1:2,1] #꽃의종1에서 10~20행, 1:2열만 볼래

# 4. data.frame
# - '열 단위 서로다른 자료형'을 갖는 2차원(행렬) 배열구조
# - 생성 함수 : data.frame()
# - 처리 함수 : apply() -> 행렬 처리 

# 1) vector 이용 (길이가 다 같아야함)
no <- 1:3
name <- c("홍길동", "이순신", "유관순")
pay <- c(250,350,200)

emp <- data.frame(NO=no, NAME=name, PAY=pay)
emp
dim(emp) # 3 3
class(emp) # "data.frame"
mode(emp) # "list" 2개 이상의 자료형을 포함하고 있을때 리스트라고 말함

# 자료 참조 : 컬럼 참조 or index 참조
# 형식) object$컬럼
emp$PAY
pay <- emp$PAY #특정 컬럼을 벡터로 뽑뽑
pay
mean(pay)
sd(pay)

 #object[row,column] 원하는 곳을 골라 추출하기도 한다
emp_row <- emp[(1,3),]
emp_row

# 2) csv, text file, db table
setwd("c:/itwill/2_rwork/part-i")
getwd

emp_txt<-read.table("emp.txt", header=T, sep = "") # ""공백으로 구분한다는 설정을 미리 인지시킴킴
emp_txt
class(emp_txt) #데이터프레임
emp_csv<-read.csv("emp.csv") #콤마 구분자로 구분되어있음(기본설정임)
emp_csv
class(emp_csv) #데이터프레임

# [실습]
sid <- 1:3 # 이산형
score <- c(90, 85, 83) # 연속형
gender <- c('M','F','M') #범주형 (남자 여자)

student <- data.frame(SID=sid, Score=score, Gender=gender)

# 자료 구조 보기
str(student) # 문자형 -> 요인형

#'data.frame':	3 obs. of  3 variables: 3개의 관측치 3개의 변수
#  $ SID   : int  1 2 3 : 이산형
# $ Score : num  90 85 83 : 연속형
# $ Gender: Factor w/ 2 levels "F","M": 2 1 2 :

#근대 나는 젠더 저걸 팩터 별로다 하면 젠더 옆에 stringAsFactor=T를 넣는다
#T : 문자형->요인형 변환 여부

# 특정 컬럼 -> 벡터 생성
student$Student

mean(scorr)
sum(score)
sd(score)
sqrt(var(score))

# 산포도 : 분산, 표준편차
# 모집단에 대한 분산, 표준편차
# 모집단에 대한 분산 = sum((x-산술평균)^2)/N, 표준편차는 저기다 루트
# 표본에 대한 분산 = sum((x-산술평균)^2)/(N-1)
# 표본에 대한 분산, 표준편차 - R 함수 : 이러하여서 알을 써서 약간 다른 값이 나올수있따

avg <- mean(score)# 스칼라
diff <- ((score - avg)^2) #(vector에서 스칼라로 변신)
VAR <- ((score - avg)^2)/ (length(score)-1)
SD <- sqrt(VAR)

# 5. List
# - key와 value 한 쌍으로 자료가 저장된다.
# - key를 통해서 값(value)을 참조한다.
# - 다양한 자료형, 자료구조를 갖는 자료구조이다.
# - 키는 중복 불가, 값은 중복 가능

# 1) key를 생략했을 때 < 보통 원소는 이래야 함 [key1=value, key2=value] >
# 입력["홍길동", "이순신"] -> [key="홍길동", key="이순신"] 이렇게 한 것으로 간주한다.
lst <- list('lee', '이순신', 35, 'hong', '홍길동', 30) #리스트니까 벡터가 아님
lst #[[1]]저게 key임 자동으로 만들어진
# lst의 첫번째 원소 : key+value 형태로 한 쌍의 형태
# [[1]] -> 사용자가 생략했던 기본키 : default key
# [1] "lee" -> 값(value)

# [[2]] -> 기본키(default key)
# [1] "이순신" -> 값2(value)

lst[1] #첫번째 원소를 보기 위한 인덱스 한 쌍의 형태이므로 쌍이 출력됨
lst[6]

# key를 통해 value를 참조한다.
lst[[5]] #홍길동 [[숫자]]저것들은 정확히 인덱스는 아니고 키의 모양이다.

# 2) key 노생략
lst2 <- list(first=1:5, second=6:10)
lst2 # 직접 만든 키에 $가 붙음 키 별로 value가 지정한대로 붙어있음

# key를 통해 value 참조
lst2$first #값이 반환됨
lst2$second

# data.frame의 $ vs list의 $
# data.frame$컬럼명
# list$키명

# 키를 딱 지명하여 값을 가져왔을 때, 그 수준에서는 벡터형태로 봄이 맞음
lst2$second[2:4] # 7 8 9

# 3) 다양한 자료형(숫자형 문자형 논리형)
lst3 <- list(name=c("홍길동","유관순"),
             age=c(35,25),
             gender=c('M', 'F')) #이 원소들이 하나의 원소에 들어간 셈
lst3
mean(lst3$age)

# 4) 다양한 자료구조 (vector, matrix, array)
lst4 <- list(one=c('one','two','three'),
             two=matrix(1:9, nrow=3),
             three = array(1:12,c(2,3,2)))
lst4
#1차원
#2차원
#3차원
#다양한 자료 구조를 하나의 객체로 넣어버렸음

# 5) list 형변환
multi_list <- list(r1 = list(1,2,3),
                   r2 = list(10,20,30),
                   r3 = list(100,200,300))
multi_list # key안에 또다른 key가 만들어짐 : 중첩리스트

#do.call(func, object)
mat <- do.call(rbind, multi_list)
mat

# 6) list 처리 함수
x <- list(1:10) # 키 생략 -> [[n]]
x

# list -> vector
v <- unlist(x) # 키 제거
v

a <-list(1:5)
b <-list(6:10)
a;b

# list 객체에 함수 적용 : lapply
lapply(c(a,b), max)# 리스트에 막 어케 해서 함수를 적용하고 리스트로 반환함
sapply(c(a,b), max)# 값만 딱 벡터로 보여줌

# 6. 서브셋(subset)
# - 특정 행 또는 열 선택 -> 새로운 dataset 생성
x <- 1:5
y <- 6:10
z <- letters[1:5]

df<-data.frame(x,y,z)
df

help("subset")
# subset(x, subset, select, drop = FALSE, ...)
#1) 조건식으로 서브셋 생성
df2<- subset(df, x >= 2)
df2 <- 조건에 맞는 애들만 출력댐

#2) select 이용 : 필요한 곳을 직접 고르겠따 : 컬럼으로 정함
df3 <- subset(df, select = c(x,z)) #x와 z만 쓰겠다
df3

# 3) 조건식 셀렉트 다 이용
df4 <- subset(df, x>=2 &x<=4, select=c(x,z))
df4

class(df2)
class(df3)
class(df4)
# 다 데이터프레임이네

# 행 단위로도 적용할 수 있다. 특정 칼럼의 특정 값으로 서브셋
df5<-subset(df,z %in% c('a','c','e')) # z컬럼 중에서 a c e 안에서 골라라
df5

# [실습] iris dataset 이용 subset 생선
iris
str(iris) #str : 스트럭처, 자료 구조 보기
# data.frame':	150 obs. of  5 variables:       행(관측치) 150개 변수(열) 5개
#  $ Sepal.Length: num  5.1 4.9 4.7 4.6 5 5.4 4.6 5 4.4 4.9 ...
#  $ Sepal.Width : num  3.5 3 3.2 3.1 3.6 3.9 3.4 3.4 2.9 3.1 ...
#  $ Petal.Length: num  1.4 1.4 1.3 1.5 1.4 1.7 1.4 1.5 1.4 1.5 ...
#  $ Petal.Width : num  0.2 0.2 0.2 0.2 0.2 0.4 0.3 0.2 0.2 0.1 ...
#  $ Species     : Factor w/ 3 levels "setosa","versicolor",..

iris_df = subset(iris, Sepal.Length >=mean(Sepal.Length), 
                 select = c(Sepal.Length, Petal.Length, Species ))
iris_df
str(iris_df)
# 'data.frame':	70 obs. of  3 variables


# 7. 문자열 처리와 정규표현식
install.packages("stringr")
library(stringr)

string="hong35lee45kang55,유관순25이사도시45"
# 메타문자 : 패턴지정 특수 기호
# 1. str_extract_all
# 1) 반복관련 메타문자 : [x] = x 1개,{n} = n개 연속
str_extract_all(string, "[a-z]{3}") #영소문자 아무거나 연속으로 세번나오는걸 추출하라
# 추출 = [[1]]
#         [1] "hon" "lee" "kan"

str_extract_all(string, "[a-z]{3,}") #세번 이상 연속
# 추출 = [[1]]
#         [1] "hong" "lee"  "kang"

name <- str_extract_all(string, "[가-힣]{3,}") #한글 세 자 이상 : "유관순"   "이사도시"
unlist(name)
name

name<-str_extract_all(string, "[가-힣]{3,5}") # 3~5자 사이
name

# 숫자 추출
ages<-str_extract_all(string, "[0-9]{2,}")
unlist(ages) #문자열로 추출됨

num_ages <- as.numeric(unlist(ages))
cat('나이 평균=', mean(num_ages)) # 숫자를 추출하고 숫자형으로 바꿔주고 계산을 함


# 2) 단어와 숫자 관련 메타문자
# 단어 : ||w
# 숫자 : ||d

jumin <- "123456-4234567"
str_extract_all(jumin, "[0-9]{6}-[1-4]{6}")
# character(0) : 담아낼 문자열이 업다

email <- "kp1234@naver.com"
str_extract_all(email, "[a-z]{3,}@[a-z]{3,}.[a-z]{2,}") #character(0)

str_extract_all(email, "[a-z]||w{3,}@[a-z]{3,}.[a-z]{2,}")

email2 <- "kp1@234@naver.com"
str_extract_all(email2, "[a-z]||w{3,}@[a-z]{3}.[a-z]{2,}")

# (3) 접두어(^), 접미어($) 메타문자
email3 <- "1kp1234@naer.com"
str_extract_all(email3,"[a-z]||w{3,}@[a-z]{3}.[a-z]{2,}") # 이러한 패턴으로는 제대로 감지하기 모자르다

str_extract_all(email3,"^[a-z]||w{3,}@[a-z]{3,}.[a-z]{2,}")
str_extract_all(email3,"^[a-z]||w{3,}@[a-z]{3,}.com$")

# (4) 특정 문자 제외 메타문자
string
result <- str_extract_all(string,"[^0-9]{3,}")
result # [[1]] : 기본키
name <- str_extract_all(result[[1]], "[가-힣]{3,}") #1차적으로 숫자 제거, 2차적으로 영문자, 특수문자
unlist(name)

# 2. str_length_all : 문자열 길이 반환
length(string) # 1
str_length(string) # 29

# 3. str_locate / str_locate_all
str_locate(string, 'g') # 앞에있는 g만 찾아짐
str_locate_all(string,'g') #모든 g 찾아냄

# 4. str_replace / str_replace_all #특정한 문자를 찾아 바꿈
str_replace_all(string, "[0-9]{2}", "") # 숫자제거

# 5. str_sub : 부분 문자열 추출
str_sub(string, start = 3, end = 5)

# 6. str_split : 문자열 분리(토큰)
string2 <- "홍길동, 이순신, 강감찬, 유관순"
result<-str_split(string2, ",")
name <- unlist(result)

# 7. 문자열 결합(join) : 기본함수
paste(name, collapse = ",") #콤마를 사이에 껴서 결합시켜라






