package chap06_Collection_exams

import scala.io.Source // file read package import
import scala.collection.mutable // 수정 가능 컬렉션 

/*
 * 문) text_data.txt 텍스트 파일을 대상으로 단어 빈도수를 구하는 함수 정의하기 
 */

object Exam03 {     
  
    // 워드카운터 함수 
    def countWords(text: String) = {
        var word_count = mutable.Map.empty[String, Int]
        var words = text.split("[ ,.!]+")
        println(words)
        println(words.mkString(" ,"))
        for(wd <- words){
          var word = wd.toLowerCase()
          var word_value
          = if(word_count.contains(word)){
            word_count(word)
            }else{
              0
            }
          word_count += (word -> (word_value + 1))
        }
        println(word_count)
    }
    
    // main 함수 
    def main(args: Array[String]): Unit = {
         try {
              // text file read
              var texts = ""
              for(line <- Source.fromFile("C:\\ITWILL\\5_Hadoop_Spark\\workspace\\part1_Scala\\src\\fileDir\\text_data.txt").getLines){
                  //println(line)
                  texts += line
              }
              
              // 워드 카운트 함수 호출 
              countWords(texts)  
          } catch {
              case ex: Exception => println(ex)
          }       
          
    }
  
}