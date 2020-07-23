package chap06_Collection_exams

import scala.io.Source
import scala.collection.mutable // 가변 컬렉션 제공 

/*
 *  문) input.txt 파일를 대상으로 공백 단위로 토큰을 생성한 후 중복된 토큰을 제거하고 다음과 같이 출력하시오.
 *  
 *  <출력결과>  
 *  Set(good, output, funvery, timemouse, programming, is, devicekeyboard, devicecomputer, system, fun, a, have, input)
 *  단어 수 = 13
 */
object Exam02 {
  
  // 시작점 : main 함수 
  def main(args: Array[String]): Unit = {
    
      try {
          var texts = ""
          for(line <- Source.fromFile("C:/ITWILL/5_Hadoop_Spark/workspace/part1_Scala/src/fileDir/input.txt").getLines){
              texts += line
          }
          
          // 내용 작성 
          val wordArr = texts.split("[ !]+")
          for(word <- wordArr) println(word)
          val words = mutable.Set.empty[String]
          for(word <- wordArr){
            words += word
          }
          println(words)
          println("단어 수 = "+words.size)
     
      } catch {
          case ex: Exception => println(ex)
      } 
       
  }
}