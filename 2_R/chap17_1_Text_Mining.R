# 텍스트 마이닝(Text Mining)
# - 정형화 되지 않은 텍스트를 대상으로 유용한 정보를 찾는 기술
# - 토픽분석, 연관어 분석, 감성분석 등
# - 텍스트 마이닝에서 가장 중요한 것은 형태소 분석
# - 형태소 분석 : 문장을 분해 가능한 최소한의 단위로 분리하는 작업 

# 1. sms_spam.csv 가져오기 - stringsAsFactors = FALSE : factor형으로 읽지 않음 
setwd("C:/ITWILL/2_Rwork/Part-IV")
sms_data <- read.csv('sms_spam.csv', stringsAsFactors = FALSE)
str(sms_data)
#'data.frame':	5558 obs. of  2 variables:
# $ type: chr  "ham" "ham" "ham" "spam" ...
# $ text: chr

# 2. 분석을 위한 데이터 처리 : sms 문장을 단어 단위로 생성 

#install.packages('tm')
install.packages('slam') # tm 패키지 의존 관계 
library(slam) 
library(tm)  

#install.packages('SnowballC') # 어근 처리 함수
install.packages('SnowballC')
library(SnowballC) 
# 어근을 처리한다 
#   -> 동명사 분사 등 -> 명사로 인식시켜줌

sms_corpus = Corpus(VectorSource(sms_data$text)) # 1) 말뭉치 생성(vector -> corpus 변환) 
inspect(sms_corpus[1]) # 이런 애들 조회하는 법
inspect(sms_corpus[4])

sms_corpus = tm_map(sms_corpus, tolower)  # 2) 소문자 변경  (대상 , 적용 함수)
inspect(sms_corpus[1]) # 소문자 변경되었는지 확인
sms_corpus = tm_map(sms_corpus, removeNumbers) # 3) 숫자 제거 
inspect(sms_corpus[4]) # 숫자 제거 확인
sms_corpus = tm_map(sms_corpus, removePunctuation) # 4) 문장부호(콤마 등) 제거 
inspect(sms_corpus[4]) # 문장부호 제거 확인

stopwords("SMART") # 571개의 '불용어'가 모여있음
stopwords("en") # 얘는 174개고 스마트가 더 많음
sms_corpus = tm_map(sms_corpus, removeWords, c(stopwords("SMART"),"짙")) # 5) stopwords(the, of, and 등) 제거  
inspect(sms_corpus[4]) # 불용어가 없어지고 그 자리에 눈에 띄게 공백이 남음
sms_corpus = tm_map(sms_corpus, stripWhitespace) # 6) 여러 공백 제거(stopword 자리 공백 제거)   
inspect(sms_corpus[4])
sms_corpus = tm_map(sms_corpus, stemDocument) # 7) 유사 단어 어근 처리 
inspect(sms_corpus[1]) # ing같은 어근 족침 그 자리에 또 공백이 남음
sms_corpus = tm_map(sms_corpus, stripWhitespace) # 8) 여러 공백 제거(어근 처리 공백 제거)   
# 공백 또 족침
inspect(sms_corpus[1]) # 이제 전처리 끗

sms_dtm = DocumentTermMatrix(sms_corpus) # 9) 문서와 단어 집계표 작성
# 희소행렬 DTM 등장
# <<DocumentTermMatrix (documents: 5558, terms: 6764)>> # 행5558, 열6764
#   Non-/sparse entries: 33887/37560425                 # 실제 수 : 1이상을 가지는 셀의 수 / 0 셀의 수
# Sparsity           : 100%                             # 희소비율 : 너무 대부분이 0이라는거고 반올림해서 100%임
# Maximal term length: 40                               # 가장 긴 단어
# Weighting          : term frequency (tf)              # 단어 출현빈도수 가중치 계산

# 단어 구름 시각화 
library(wordcloud) # 단어 시각화(빈도수에 따라 크기 달라짐)

# 색상 12가지 적용 
pal <- brewer.pal(12,"Paired") # RColorBrewer 패키지 제공(wordcloud 설치 시 함께 설치됨)

# DTM을 갖다 행 열을 스왑하여 TDM을 만듬 그리고 이 걸 as.matrix로 평서문으로 변환
sms_mt <- as.matrix(t(sms_dtm)) # 행렬 변경 

# 행 단위(단어수) 합계 -> 내림차순 정렬   
rsum <- sort(rowSums(sms_mt), decreasing=TRUE) 
rsum[1:10] # 출현빈도 탑텐

# vector에서 칼럼명(단어명) 추출 
myNames <- names(rsum) # rsum 변수에서 칼럼명(단어이름) 추출  
myNames # 단어명 

# 단어와 빈도수를 이용하여 df 생성 
df <- data.frame(word=myNames, freq=rsum) 
head(df) # word freq

# wordCloud(단어(word), 빈도수(v), 기타 속성)
# random.order=T : 위치 랜덤 여부(F 권장) , rot.per=.1 : 회전수, colors : 색상, family : 글꼴 적용 
wordcloud(df$word, df$freq, min.freq=2, random.order=F, scale=c(4,0.7),
          rot.per=.1, colors=pal, family="malgun") 


########################################
### 단어수 조정 - 단어길이, 가중치 적용 
########################################
sms_dtm = DocumentTermMatrix(sms_corpus) # 9)
sms_dtm 
# 너무 긴 단어는 족쳐야 되겠다

# 1. 단어길이 : 1 ~ 8
sms_dtm1 = DocumentTermMatrix(sms_corpus,
                              control = list(wordLengths= c(1,8)))
sms_dtm1 # 단어의 수가 좀 줄었지

# DTM -> TDM 변경 
t(sms_dtm1) # (terms: 6156, documents: 5558)
sms_tdm1 <- as.matrix(t(sms_dtm1))
dim(sms_tdm1) # [1] 6079 5558 
sms_tdm1[1,] # 1번 단어가 문서에서 출현하는 정도

# 2. 가중치 : 단어출현빈도로 가중치(비율) 적용 
# - 출현빈도수 -> 비율 가중치 조정  
sms_dtm2 = DocumentTermMatrix(sms_corpus,
                              control = list(wordLengths= c(1,8),  weighting = weightTfIdf))
sms_dtm2
# Weighting : term frequency - inverse document frequency (normalized) (tf-idf)
# 중요하지 않은데 자주 나오는 애들을 족침
## 가중치 적용 방법
## 1. TF : 단어의 출현빈도수
## 2. TfIdf = TF * (1/DF)
TF <- 2 # 한 문장에서 두 번 출현 가정
DF <- 10 # 문서에서 10번 나왔다 가정
TfIdf = TF * (1/DF) # 0.2
DF <- 20 # 문서에서 20번 나왔다 가정
TfIdf = TF * (1/DF) # 0.1

# DTM -> TDM 변경 
sms_tdm2 <- as.matrix(t(sms_dtm2))
str(sms_tdm2)
dim(sms_tdm2)

################################
### DTM 대상 단어 검색 
################################

# 단어 길이 검색 
class(sms_dtm1)
str(sms_dtm1)
terms <- sms_dtm1$dimnames$Terms
terms

# 길이가 5~6자 이상 단어 검색 이렇게 조건 붙여서 조회 가능하다
library(stringr)
result <- terms[str_length(terms) >= 5 & str_length(terms) >= 6]
result
length(result) # 2512

# 단어 출현빈도수 검색
freq <- findFreqTerms(sms_dtm1, lowfreq = 40) # tm
freq



###############################
## chap17_Text_Mining(2)
###############################
# 기계학습을 위한 데이터 셋 생성 

# 1. sms_spam.csv 가져오기 - stringsAsFactors = FALSE : factor형으로 읽지 않음 

sms_data <- read.csv('sms_spam.csv', stringsAsFactors = FALSE)
str(sms_data)


# 2. 분석을 위한 데이터 처리 : sms 문장을 단어 단위로 생성해야 한다. 
library(tm)
library(SnowballC) # stemDocument()함수 제공 
sms_corpus = Corpus(VectorSource(sms_data$text)) # 1) 말뭉치 생성(vector -> corpus 변환) 
sms_corpus = tm_map(sms_corpus, tolower)  # 2) 소문자 변경
sms_corpus = tm_map(sms_corpus, removeNumbers) # 3) 숫자 제거 
sms_corpus = tm_map(sms_corpus, removePunctuation) # 4) 문장부호(콤마 등) 제거 
sms_corpus = tm_map(sms_corpus, removeWords, stopwords("SMART")) # 5) stopwords(the, of, and 등) 제거  
sms_corpus = tm_map(sms_corpus, stripWhitespace) # 6) 여러 공백 제거(stopword 자리 공백 제거)   
sms_corpus = tm_map(sms_corpus, stemDocument) # 7) 유사 단어 어근 처리 
sms_corpus = tm_map(sms_corpus, stripWhitespace) # 8) 여러 공백 제거(어근 처리 공백 제거)   


################################
### DTM 생성 -> X변수 생성 
################################

# 1. DTM 생성 -> 단어길이 : 2 ~ 8, 출현빈도수로 가중치 
sms_dtm = DocumentTermMatrix(sms_corpus,
                             control = list(wordLengths= c(2,8))) 

sms_dtm
# 2. DTM -> matrix 변경
sms_dtm_mat <- as.matrix(sms_dtm) # 평서문으로 바꾸기
sms_dtm_mat


# 3. 가중치 -> Factor('YES', 'NO')
convert_Func <- function(x){
  # 가중치가 1이상 : 1, 0이면 0
  x <- ifelse(x > 0, 1, 0) # 가중치 비율인 경우 
  f <- factor(x, levels = c(0,1), labels = c('NO','YES')) # 0 : no, 1이상 : yes
  return(f) 
}

# 4. sms_dtm 사용자 함수 적용 
dim(sms_dtm_mat) # 5558 6122
sms_dtm_mat_text <- apply(sms_dtm_mat, 2, convert_Func)
#                                      열(단어)을 저따 넣어라
dim(sms_dtm_mat_text) # 5558 6122
sms_dtm_mat_text[1,] # 첫번째 단어 : 6122 단어 중 뭐가 나왔는가
table(sms_dtm_mat_text[1,])
# NO    YES 
# 6118  4 
# 첫 문장에서 4단어가 출현했다

# 5. DF = y + x(sms_dtm_mat_text) / 정답과 변수
sms_dtm_df = data.frame(sms_data$type, sms_dtm_mat_text)
dim(sms_dtm_df) # 5558 6123

# 6. csv file save
write.csv(sms_dtm_df, "c:/itwill/2_rwork/part-iv/sms_dtm_df.csv",
          quote = F, row.names = F)















