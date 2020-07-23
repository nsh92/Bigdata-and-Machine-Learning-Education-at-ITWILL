#################################
## <제9장-2 연습문제>
################################# 
library(rJava)
library(hash)
library(tau)
library(RSQLite)
library(devtools)
library(KoNLP)
library(tm)
library(wordcloud) 

# 01. 트럼프 연설문(trump.txt)과 오바마 연설문(obama.txt)을 대상으로 빈도수가 2회 이상 단어를 대상으로 단어구름 시각화하시오.
trump <- file.choose()
obama <- file.choose()
trump1 <- readLines(trump)
obama1 <- readLines(obama)

exNouns <- function(x) { 
  paste(extractNoun(as.character(x)), collapse=" ")
}
trump2 <- sapply(trump1, exNouns)
obama2 <- sapply(obama1, exNouns)

trump3 <- Corpus(VectorSource(trump2))
obama3 <- Corpus(VectorSource(obama2))

trump4 <- tm_map(trump3, removePunctuation) # 문장부호 제거
trump4 <- tm_map(trump3, removeNumbers) # 수치 제거
trump4 <- tm_map(trump3, tolower) # 소문자 변경
trump4 <-tm_map(trump3, removeWords, stopwords('english'))

obama4 <- tm_map(obama3, removePunctuation) # 문장부호 제거
obama4 <- tm_map(obama3, removeNumbers) # 수치 제거
obama4 <- tm_map(obama3, tolower) # 소문자 변경
obama4 <-tm_map(obama3, removeWords, stopwords('english'))

trump5 <- TermDocumentMatrix(trump4, 
                            control=list(wordLengths=c(2,inf)))
obama5 <- TermDocumentMatrix(obama4, 
                            control=list(wordLengths=c(2,inf)))

trump6 <- as.data.frame(as.matrix(trump5)) 
obama6 <- as.data.frame(as.matrix(obama5)) 

trump7 <- sort(rowSums(trump6), decreasing=TRUE)
obama7 <- sort(rowSums(obama6), decreasing=TRUE)

trump8 <- names(trump7)
obama8 <- names(obama7)

trump9 <- data.frame(word=trump8, freq=trump7) 
obama9 <- data.frame(word=obama8, freq=obama7) 

pal <- brewer.pal(12,"Paired")
windowsFonts(malgun=windowsFont("맑은 고딕"))

wordcloud(trump9$word, trump9$freq, 
          scale=c(5,1), min.freq=2, random.order=F, 
          rot.per=.2, colors=pal, family="malgun")

wordcloud(obama9$word, obama9$freq, 
          scale=c(5,1), min.freq=2, random.order=F, 
          rot.per=.2, colors=pal, family="malgun")

# 02. 공공데이터 사이트에서 관심분야 데이터 셋을 다운로드 받아서 빈도수가 5회 이상 단어를 이용하여 
#      단어 구름으로 시각화 하시오.
# 공공데이터 사이트 : www.data.go.kr

call <- read.csv(file.choose())
str(call)

exNouns <- function(x) { 
  paste(extractNoun(as.character(x)), collapse=" ")
}

call1 <- sapply(call$상담세분류, exNouns)
head(call1)
str(call1)

call2 <- Corpus(VectorSource(call1))
call3 <- tm_map(call2, removePunctuation) # 문장부호 제거
call3 <- tm_map(call2, removeNumbers) # 수치 제거
call3 <- tm_map(call2, tolower) # 소문자 변경
call3 <-tm_map(call2, removeWords, stopwords('english'))

call4 <- TermDocumentMatrix(call3, 
                             control=list(wordLengths=c(4,30)))

call5 <- as.data.frame(as.matrix(call4)) 
call6 <- sort(rowSums(call5), decreasing=TRUE)
call7 <- names(call6)
call8 <- data.frame(word=call7, freq=call6) 

pal <- brewer.pal(12,"Paired")
windowsFonts(malgun=windowsFont("맑은 고딕"))

wordcloud(call8$word, call8$freq, 
          scale=c(5,1), min.freq=4, random.order=F, 
          rot.per=.1, colors=pal, family="malgun")