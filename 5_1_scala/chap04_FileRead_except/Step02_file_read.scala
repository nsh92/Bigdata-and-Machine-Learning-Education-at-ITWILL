package chap04_FileRead_except
// io 패키지 import
import scala.io.Source               // file source read
import java.io.FileNotFoundException // 예외처리

object file_read {
  
  // iris.csv -> read 함수 정의 : csv를 가져오는 함수를 정의함
  def csv_load(filename : String) : Unit = {
    try{
      val fileRead = Source.fromFile("C:/ITWILL/5_Hadoop_Spark/workspace/part1_Scala/src/fileDir/" + filename)
      println("csv load 성공")

      var lines = fileRead.getLines().drop(1) // 제목줄 제거, 전체 줄 단위 읽기
      for(line <- lines){// 한 줄 읽기는 println(line)
        // 콤마 기준 토큰 생성하고, 토큰 앞뒤 공백족치고, 변수로 저장해보자
        var cols = line.split(",").map(_.trim) // line을 넘겨받아 column으로 만듦
        // 컬럼 단위 출력 : s"${칼럼}"  (파이썬에선 s가 f였음)
        println(s"${cols(0)}, ${cols(1)}, ${cols(2)}, ${cols(3)}, ${cols(4)}")
      }
      fileRead.close // file 객체 닫기
      
    }catch{
      case ex : FileNotFoundException => println("예외정보 : " + ex )
    }
  }
  def main(args: Array[String]): Unit = {
    try{
      val fileRead = Source.fromFile("C:/ITWILL/5_Hadoop_Spark/workspace/part1_Scala/src/fileDir/scala_object.txt")
      println("파일 읽기 성공")
      
      // 줄단위 전체 읽기
      var lines = fileRead.getLines()
      for(line <- lines) println(line)
      
      fileRead.close
      
    }catch{
      case ex : FileNotFoundException => println("예외정보 : " + ex )
    }
    
    // csv 가져오는 함수 호출
    csv_load("iris.csv")
    
  }
}