#################################
## <제3장 연습문제>
#################################
data()
# 문1) acq 데이터 셋을 대상으로 다음과 같이 TDM 객체를 생성하시오.
# <조건1> 전체 단어의 갯수는 몇 개인가 ? 
# <조건2> 최대 단어 길이는 몇 개인가 ? 

data(acq) # corpus 객체 
str(acq)
head(str(acq[1]))

# 작업절차 : acq -> DATA전처리(2단계 ~ 8단계) -> DTM -> TDM -> ?

# 1. DATA 전처리(3단계 ~ 8단계)
acq_corpus = tm_map(acq, tolower)  # 2) 소문자 변경
acq_corpus = tm_map(acq_corpus, PlainTextDocument) # [추가] 평서문 변경

acq_corpus = tm_map(acq_corpus, removeNumbers)
acq_corpus = tm_map(acq_corpus, removePunctuation)
acq_corpus = tm_map(acq_corpus, removeWords, stopwords("SMART"))
acq_corpus = tm_map(acq_corpus, stripWhitespace)
acq_corpus = tm_map(acq_corpus, stemDocument)
acq_corpus = tm_map(acq_corpus, stripWhitespace)


# 2. DTM 생성(9단계) 
acq_dtm = DocumentTermMatrix(acq_corpus,
                              control = list(wordLengths= c(1,8),  weighting = weightTfIdf))

# 3. TDM 생성(전치행렬) 
acq_tdm <- as.matrix(t(acq_dtm))

# 문2) crude 데이터 셋을 대상으로 다음과 같이 TDM 객체를 생성하시오.
# <조건1> 단어 길이 : 1 ~ 8
# <조건2> 가중치 적용 : 출현빈도수의 비율 
# <조건3> 위 조건의 결과를 대상으로 단어수는 몇개인가 ?  

data(crude)

# 1. DATA전처리(3단계 ~ 8단계)
crude_corpus = tm_map(crude, tolower)  # 2) 소문자 변경
crude_corpus = tm_map(crude_corpus, PlainTextDocument) # [추가] 평서문 변경

crude_corpus = tm_map(crude_corpus, removeNumbers)
crude_corpus = tm_map(crude_corpus, removePunctuation)
crude_corpus = tm_map(crude_corpus, removeWords, stopwords("SMART"))
crude_corpus = tm_map(crude_corpus, stripWhitespace)
crude_corpus = tm_map(crude_corpus, stemDocument)
crude_corpus = tm_map(crude_corpus, stripWhitespace)

# 2. DTM 생성 
crude_dtm = DocumentTermMatrix(crude_corpus,
                             control = list(wordLengths= c(1,8),  weighting = weightTfIdf))

# 3. TDM 생성 
crude_tdm <- as.matrix(t(crude_dtm))
str(crude_tdm)
