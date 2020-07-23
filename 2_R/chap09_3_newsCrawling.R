# chap09_3_newsCrawling


# https://media.daum.net/
# <a href="url"> 기사 내용 </a>

# 1. 패키지 설치
install.packages('httr') # 원격 url 요청
library(httr)
install.packages('XML') # tag -> html 파싱
library(XML)

# 2. url 요청
# 요청 : 니네들이 올린 정보를 가져오겠다
url <- "https://media.daum.net/"
web <- GET(url)
# 페이지 소스를 요청함
web # status : 200 멀쩡

# 3. html 파싱(text -> html)
help("htmlTreeParse")
# xml이나 html 애들을 tag형태로 파싱한다
html <- htmlTreeParse(web, useInternalNodes = T,
                      trim=T, encoding = "utf8")
# 노드 사용여부 기본값이 F임, trim 앞뒤 공백 삭제여부

root_node <- xmlRoot(html)

# 4. tag 자료 수집 : "//태그[@속성 = '값']" 어떠한 속성을 가지고 있는 태그를 가져와라
news <- xpathSApply(html, "//a[@class='link_txt']", xmlValue)
news
# 59번까지 쓸만하고 그 밑으로는 무쓸모
news2<-news[1:59]
news2


# 5. news 전처리

news_sent = gsub('[\n\r\t]', '', news2) #문장부호 제거
news_sent = gsub('[[:punct:]]', '', news_sent)
news_sent = gsub('[[:cntrl:]]', '', news_sent) #특수문자 제거
news_sent = gsub('[a-z]', '', news_sent)
news_sent = gsub('[A-Z]', '', news_sent)
news_sent = gsub('\\s+', ' ', news_sent)

news_sent
#이 상태에서 선택적으로 토픽분석, 연관분석, 감정분석 판단하는 거임

# 6. file save
setwd("c://itwill/2_rwork/output")
write.csv(news_sent, 'news_data.csv', quote = F)

news_data <- read.csv('news_data.csv')
head(news_data) # 잘 저장댄건지 확인

colnames(news_data) <- c('no', 'news_text')
head(news_data)

news_text <- news_data$news_text
news_text

# 7. 토픽 분석 -> 단어구름 시각화(1day)
library(rJava)
library(hash)
library(tau)
library(RSQLite)
library(devtools)
library(KoNLP)
library(tm)
library(wordcloud) 

# 신규단어
user_dic = data.frame(term=c("펜데믹", "코로나19", "타다"), tag='ncn')
buildDictionary(ext_dic = 'sejong', user_dic = user_dic)

exNouns <- function(x) { 
  paste(extractNoun(as.character(x)), collapse=" ")
}

news1 <- sapply(news_text, exNouns)
news2 <- Corpus(VectorSource(news1))

news3 <- TermDocumentMatrix(news2, 
                             control=list(wordLengths=c(4,16)))
news4 <- as.data.frame(as.matrix(news3)) 
news5 <- sort(rowSums(news4), decreasing=TRUE)
news6 <- names(news5)
news7 <- data.frame(word=news6, freq=news5) 

pal <- brewer.pal(12,"Paired")
windowsFonts(malgun=windowsFont("맑은 고딕"))

wordcloud(news7$word, news7$freq, 
          scale=c(5,1), min.freq=2, random.order=F, 
          rot.per=.1, colors=pal, family="malgun")