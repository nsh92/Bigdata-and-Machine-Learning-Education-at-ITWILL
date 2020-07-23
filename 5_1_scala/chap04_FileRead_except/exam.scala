package chap04_FileRead_except

import scala.io.Source

/*
 * 문) iris.csv 데이터셋에서 "setosa"가 포함된 행만 출력하기 
 */

object Exam {
  
  def csv_load(filename : String) : Unit = {
      val fileRead = Source.fromFile("C:/ITWILL/5_Hadoop_Spark/workspace/part1_Scala/src/fileDir/" + filename)
      println("csv load 성공")
      var lines = fileRead.getLines().drop(1)
      var row = 0
      for(line <- lines){
        var cols = line.split(",").map(_.trim)
        
        row += 1
        if(cols(4).contains("setosa"))
          println(s"${row} : ${cols(0)}, ${cols(1)}, ${cols(2)}, ${cols(3)}, ${cols(4)}")

      }
  } 
  
  def main(args: Array[String]): Unit = {
      csv_load("iris.csv")
  }
  
}

