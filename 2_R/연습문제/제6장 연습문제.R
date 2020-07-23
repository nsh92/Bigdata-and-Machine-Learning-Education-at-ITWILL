#################################
## <제6장 연습문제>
################################# 

# <dplyr 패키지 관련 연습문제> 
library(dplyr)
data(iris)

# 01. iris의 꽃잎의 길이(Petal.Length) 칼럼을 대상으로 1.5 이상의 값만 필터링하시오.
filter(iris, iris$Petal.Length >= 1.5)
dim(filter(iris, iris$Petal.Length >= 1.5))
## 답 : dim 했을 때 126,5

# 02. 01번 결과에서 1,3,5번 칼럼을 선택하시오.
select(filter(iris, iris$Petal.Length >= 1.5), Sepal.Length, Petal.Length, Species)
dim(select(filter(iris, iris$Petal.Length >= 1.5), Sepal.Length, Petal.Length, Species))
## 답 : dim 했을 때 126,3

# 03. 02번 결과에서 1번 - 3번 칼럼의 차를 구해서 diff 파생변수를 만들고, 앞부분 6개만 출력하시오.
select(mutate(filter(iris, iris$Petal.Length >= 1.5), diff_Length = Sepal.Length - Petal.Length)
              , Sepal.Length, Petal.Length, Species, diff_Length)

# 04. 03번 결과에서 꽃의 종(Species)별로 그룹화하여 Sepal.Length와 Petal.Length 변수의 평균을 계산하시오.
group_spe <- group_by(select(mutate(filter(iris, iris$Petal.Length >= 1.5), diff_Length = Sepal.Length - Petal.Length)
                , Sepal.Length, Petal.Length, Species, diff_Length), Species)

summarise(group_spe, mean_SL = mean(Sepal.Length), sd_SL = sd(Sepal.Length),
          mean_PL = mean(Petal.Length), sd_PL = sd(Petal.Length))


# <reshape2 패키지 관련 연습문제> 
library('reshape2')

# 05. reshape2 패키지를 적용하여 각 다음 조건에 맞게 iris 데이터 셋을 처리하시오. 
# 조건1) 꽃의 종류(Species)를 기준으로 ‘넓은 형식’을 ‘긴 형식’으로 변경하기(melt()함수 이용)
# 조건2) 꽃의 종별로 나머지 4가지 변수의 합계 구하기(dcast()이용)
str(iris)
melt(iris, id = "Species")
dim(melt(iris, id = "Species"))

head(melt(iris, id = "Species"))
dcast(melt(iris, id = "Species"), Species ~ variable, sum)









