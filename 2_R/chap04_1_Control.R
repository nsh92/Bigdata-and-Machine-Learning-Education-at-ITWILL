# chap04_1_Control (4-2도있음)

# <실습> 산술연산자 
num1 <- 100 # 피연산자1
num2 <- 20  # 피연산자2
result <- num1 + num2 # 덧셈
result # 120
result <- num1 - num2 # 뺄셈
result # 80
result <- num1 * num2 # 곱셈
result # 2000
result <- num1 / num2 # 나눗셈
result # 5

result <- num1 %% num2 # 나머지 계산
result # 0

result <- num1^2 # 제곱 계산(num1 ** 2)
result # 10000
result <- num1^num2 # 100의 20승
result # 1e+40 -> 1 * 10의 40승과 동일한 결과


# <실습> 관계연산자 
# (1) 동등비교 
boolean <- num1 == num2 # 두 변수의 값이 같은지 비교
boolean # FALSE
boolean <- num1 != num2 # 두 변수의 값이 다른지 비교
boolean # TRUE

# (2) 크기비교 
boolean <- num1 > num2 # num1값이 큰지 비교
boolean # TRUE
boolean <- num1 >= num2 # num1값이 크거나 같은지 비교 
boolean # TRUE
boolean <- num1 < num2 # num2 이 큰지 비교
boolean # FALSE
boolean <- num1 <= num2 # num2 이 크거나 같은지 비교
boolean # FALSE

# <실습> 논리연산자(and, or, not, xor)
logical <- num1 >= 50 & num2 <=10 # 두 관계식이 같은지 판단 
logical # FALSE
logical <- num1 >= 50 | num2 <=10 # 두 관계식 중 하나라도 같은지 판단
logical # TRUE

logical <- num1 >= 50 # 관계식 판단
logical # TRUE
logical <- !(num1 >= 50) # 괄호 안의 관계식 판단 결과에 대한 부정 : 50보다 큰 것이 아닌지?
logical # FALSE

x <- TRUE; y <- FALSE
xor(x,y) # [1] TRUE 서로 다르다
x <- TRUE; y <- TRUE
xor(x,y) # FALSE 서로 같다


##########################################
### 1. 조건문
##########################################

# 1) if(조건식) - 조건식 : 산술, 관계, 논리연산자
x<-10
y<-5
z<-x*y
if(z>=200){
  cat('z는 20보다 크다.') #실행문
}

# 형식) if(조건식){참}else{거짓}
if(z>=20){cat('z는20보다큼')}else{cat('z는20보다작음')}

# 형식2) if(조건식1){참}else if(조건식2){참}else{거짓}
score<-scan() #0~100전제
score
# score -> grade(A, B, C, D, F)
grade <- ""
if(score>=90){grade <- "A"
}else if(score>=80){grade <- "B"
}else if(score>=70){grade <- "C"
}else if(score>=60){grade <- "D"
}else{grade<-"F"}
grade
cat('점수는', score, '이고. 등급은', grade)

#문) 키보드로 임의 숫자를 입력받아서 짝홀 판별하기
num <- scan()#여기서 입력
jjakhol<-""
if(num%%2==0){cat('짝수이다')}else{cat(홀수이다)}
#시발

#문)주민번호를 이용하여 성별 판별하기
library(stringr)
jumin <- "123456-8234567"
# 성별추출 : str_sub(8,8)
# 1 or 3 : 남자
# 2 or 4 : 여자
# other : 번호가 틀렸다
gender <- str_sub(jumin,8,8)
if(gender == 1|gender == 3){cat('남자입니다')
}else if(gender == 2|gender == 4){cat('여자입니다')
}else{cat('번호가틀렷다이새끼야')}

# 2) ifelse : if + else
# 형식) ifelse(조건식, 참, 거짓) = 3항연산자
# vector 입력 -> 처리 -> vector 출력

score <- c(78,85,95,45,65)
grade <= #합격 #실패
ifelse(score >= 60, "합격", "실패")

excel <- read.csv(file.choose()) 
q5<-excel$q5
table(q5)
q5_re <- ifelse(q5 >=3, "큰값", "작은값")
table(q5_re)
# 5점 척도 데이터를 범주형 변수로 바꿨다

# 조건넣으려는데 결측치가 있다 : 평균으로 대체하라
x <- c(75,85,42,NA,85)
ifelse(is.na(x), mean(x, na.rm = T), x) #NA값이 있으면 평균으로 바꿔주고 아님 그대로 나오면대고
ifelse(is.na(x), 0, x) # 이렇게도 활용가능

# ifelse 안에 또 ifelse 또 들어가는 것도 가능

# 3) switch 문 : 다중선택
# 형식)  switch(비교 구문, 실행구문1, 실행구문2, 실행구문3) 
switch("pwd", "name", age=105, name="홍길동", id="hong", pwd="1234") 
switch("name", age=105, name="홍길동", id="hong", pwd="1234") 

# 4) which문
# 조건식에 만족하는 위치 반환

name <- c("kim","lee","choi","park")
which(name=="choi") # [1] 3번째에 있다

library(MASS)
data("Boston")
str(Boston)#506관측치 14변수
name <- names(Boston) #변수만 가져옴
length(name) #컬럼의 14개다

# x(독립) y(종속) 변수 선택
# 저 보스턴 데이터에서 어떤 것들이 주택 가격(중앙값medv)에 영향을 미치는지 알아보자
which(name=="medv") # 14번째다
y_col <- which(name=="medv")
y_col

Y <- Boston[y_col]
head(Y)

X <- Boston[-y_col] #y_col빼고 다 : 마이너스표시
head(X)

# 문) iris 데이터셋을 대상으로 x변수(1~4컬럼), y변수(5컬럼) 지정해봐라
str(iris)
name<-names(iris)
iy_col<-which(name=="Species")
y<-iris[iy_col]
x<-iris[-iy_col]
head(y)
head(x)


##########################################
### 2. 반복문
##########################################

# 1) for(변수 in 열거행객체){실행문}
num <- 1:10 # 이 모양을 열거행객체라 함

for(i in num){ # i에 하나씩 차례로 넣음, 10회 반복하는 셈
  cat('i=', i, '\n') #실행문
  print(i*2) # 줄바꿈
  }

#홀짝 구분 
for(i in num){
  if(i %% 2 !=0){
    cat('i=',i,'\n')
  }
}

for(i in num){
  if(i %% 2 == 0){
    cat('i=',i,'\n')
  }else{
  next  
  }
}

# 문) 키보드로 5개 정수를 입력받아서 짝/홀 구분하기
num <- scan()
for(i in num){
  if(i %% 2 ==0){
    cat('짝수다\n')
    }else{
      cat('홀수다\n')
    }
  }

# 문)1~100까지 홀수의 합과 짝수의 합 출력하기
even <- 0 #짝수합
odd <- 0 #홀수합
cnt <- 0 #카운터 변수

num <- 1:100

for(i in num){
  cnt = cnt + 1            #1씩만 증가하는 카운터 변수
  if(i %% 2 == 0){
    even = even + i        # 짝수에 대한 누적 변수
  }else{
    odd = odd + i          # 홀수에 대한 누적 변수
  }
}
cat('짝수의합=', even, '홀수의합=', odd)
cat('카운터변수=', cnt)
even
odd
cnt

kospi<-read.csv(file.choose())
str(kospi)

# 칼럼 = 컬럼-컬럼
kospi$diff <- kospi$High - kospi$Low
str(kospi)

row <- nrow(kospi) #행의 길이 반환
# diff 평균 이상 '평균 이상', 아니면 '평균 미만'
diff_result = "" # 변수 초기화
for(i in 1:row){
  if (kospi$diff[i] >= mean(kospi$diff)){
    diff_result[i] = '평균 이상'
  }else{
    diff_result[i] = '평균 미만'
  }
}
diff_result
kospi$diff_result = diff_result
table(kospi$diff_result)


# 이중 for문
for(변수 in 열거형){
 for(변수 in 열거형){
   실행문
 }
}

for(i in 2:9){
  cat('***', i,'단***\n')
  for(j in 1:9){
    cat(i, '*', j, '=', (i*j), '\n')
  }
  cat('\n')
  }
# 구구단이 출력됨


# 이중 for문 파일 저장하기
for(i in 2:9){
  cat('***', i,'단***\n',
      file="c:/itwill/2_rwork/output/gugu.txt",
      append = TRUE)
  
  for(j in 1:9){
    cat(i, '*', j, '=', (i*j), '\n',
        file="c:/itwill/2_rwork/output/gugu.txt",
        append = TRUE)
  }
  cat('\n',
      file="c:/itwill/2_rwork/output/gugu.txt",
      append = TRUE)
}

# text file 읽기
gugu.tet<-readLines("c:/itwill/2_rwork/output/gugu.txt")
gugu.tet

# 2) while(조건식){실행문}
i=0 #초기화
while(i < 5){
  cat('i = ', i, '\n')
  i=1+i
}

x <- c(2,5,8,6,9)
#각 변량에 제곱을 취해보자
n <- length(x)
i<-0 #index역할
while(i < n){
  i<-1+i
  y[i] <- x[i]^2
}

y


