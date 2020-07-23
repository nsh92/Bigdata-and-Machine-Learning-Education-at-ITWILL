# chap03_dataIO (input, outout)

# 1. data 불러오기(키보드 입력, 파일 가져오기)
# 1) 키보드 입력
x <- scan() #숫자형이 기본이고 다른 타입은 추가적으로 설정해줘야함)
x[3]
sum(x)
mean(x)

# 문자입력
string <- scan(what = character())

# 2) 파일 읽기
# 2-1) read.table() : 컬럼 구분(공백, 특수문자)
setwd("c:/itwill/2_rwork/part-i")

# 제목없음, 구분자 : 공백인  텍스트 파일 가져오기 txt
read.table("student.txt") # 제목 없음, 공백으로 구분
# 기본 컬럼 제목 : v1~v4

# 컬럼 제목이 있는 경우, 컬럼 구분 : 특수문자(;)
student2 <- read.table("student2.txt", header = TRUE, sep = ";")
student2

# 데이터에 결측치가 있더라
student3 <- read.table("student3.txt", header = TRUE, )
student3
student3$'키' # 현재 문자형태임 : 연산불가능

student3 <- read.table("student3.txt", header = TRUE, na.strings = c("-"))
student3
student3$'키' * 2
mean(student3$'키', na.rm=T)
#만약 다른 결측치 표현 특수문자가 더 있따면 걔내들도 C()안에 들어가야함
str(student3)
class(student3)

# 2-2) read.csv() : 구분자가 콤마
read.csv("student4.txt", na.strings = c("-")) 
#헤더 설정이 기본적으로 트루이기에 표시 없으면 제목이 있는 것으로 간주됨)
student4 <- read.csv("student4.txt", na.strings = c("-"))

# 탐색기 이용 : 파일 선택
excel <- read.csv(file.choose()) # 이상태로 실행시키면 파일탐색기가 뜸
excel

# 2-3) xls/xlsx 엑셀파일 불러오기 : 패키지 설치 요구
install.packages("xlsx") #원래는 rjava도 받아야했는데 이젠 한꺼번에 받아짐
library(rJava) #하지만 메모리엔 올려줘야 함
library(xlsx)

kospi <- read.xlsx("sam_kospi.xlsx", sheetIndex = 1)

# 한글이 포함된 엑셀 파일 읽기
st_excel <- read.xlsx("studentexcel.xlsx", sheetIndex = 1, encoding = 'UTF-8')


# 3) 인터넷 파일 읽기
# 데이터 셋 제공 사이트 
# http://www.public.iastate.edu/~hofmann/data_in_r_sortable.html - Datasets in R packages
# https://vincentarelbundock.github.io/Rdatasets/datasets.html
# https://r-dir.com/reference/datasets.html - Dataset site
# http://www.rdatamining.com/resources/data

titanic <- read.csv("https://vincentarelbundock.github.io/Rdatasets/csv/COUNT/titanic.csv")
str(titanic)
dim(titanic)
head(titanic)

# 저 데이터에서 생존여부 보기
table(titanic$survived) #빈도 수 확인

# 성별 구분
table(titanic$sex)

# class구분
table(titanic$class)

# 성별에 따른 생존여부 : 교차분할표
# 각자 컬럼이었는데 빼와가지고 행렬로 만들어버리기
tab <- table(titanic$survived, titanic$sex)

# 보통 200개 까지 출력시켜주는데 다 보고싶다면
getOption("max.print") # 1000 = 200*5
options(max.print = 999999999)

#막대차트 및 색깔
barplot(tab, col=rainbow(2))

# 2. 데이터 저장(출력)하기
# 1) 화면 출력
x=20
y=30
z=x+y
# 그냥 z실행시키기 = print(z) 근대 굳이 이렇게 지정해줘야할 경우가 있다
cat('z=', z) # 특정한 문자열과 결합시켜서 출력값을 보여줄 수 있음
print('z=',z) # error 문자열과 못 합침
print(z**2) # 수식 표현은 가능

2) 파일 저장(출력)
#read.table -> write.table : 구분자가 공백 특수문자
#read.csv -> write.csv : 구분자가 콤마
#read.xlsx -> write.xlsx : 엑셀(패키지 필요)

# (1) write.table() : 공백
setwd("c:/itwill/2_rwork/output")
write.table(titanic, "titanic.txt", row.name = FALSE)
write.table(titanic, "titanic2.txt", quote=FALSE, row.names = FALSE)

# (2) write.csv() : 콤마
head(titanic)
titanic_df <- titanic[-1]
str(titanic_df) # 변수 하나 없어진 거 확인

write.csv(titanic_df, "titanic_df.csv", row.names=FALSE, quote = FALSE)

# (3) write.xlsx : 엑셀 파일
search() # "package:xlsx"
write.xlsx(titanic, "titanic.xlsx", 
           sheetName = "titanic",
           row.names = F)

더 많은 내용이 있으나 여기서 3장 끗











