package com.spark.ch01_rdd
import org.apache.spark.SparkConf
import org.apache.spark.SparkContext

object Step01_rdd_Create {
  def main(args: Array[String]): Unit = {
  val conf = new SparkConf()
    .setAppName("SparkTest")
    .setMaster("local")
  val sc = new SparkContext(conf)
  
  // 1. 파티션 지정 RDD 생성 : parallelize(data, 파티션수) 이용
  val rdd1 = sc.parallelize(1 to 100, 5) // data : vector 이용, 1~100을 5개로 쪼갠다
  // RDD read -> 구분자 기준 원소 출력
  println(rdd1.collect().mkString(", ")) // 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ..., 100

  // 객체.bind()
  rdd1.foreach((x : Int) => print(x + " ")) // 무명함수, 쪼개진 것 끼리 뜸(5집단)
  
  val rdd1_2 = sc.parallelize(List("a", "b", "c", "d", "e")) // 리스트 컬렉션 사용, 파티션 지정 안 함
  println(rdd1_2.collect().mkString(", ")) // a, b, c, d, e
  rdd1_2.foreach((x : String) => print(x + " ")) // 파티션 지정 안 했으니 한 라인에 출력됨
  
  // 2. 외부 저장 매체(file, HDFS) 데이터 이용 RDD 생성
  val rdd2 = sc.textFile("file:/C:/hadoop-2.6.0/NOTICE.txt")
  // ("file:/c:/localDir/file")
    
  // 텍스트 파일의 한 줄은 한 개의 RDD의 한 개의 원소
  println(rdd2.collect().mkString("\n")) // 줄바꿈 구분자 이용 줄 단위 출력
  rdd2.foreach((x : String) => println(x)) // 줄단위 출력
  
  //객체 닫기
  sc.stop
  }// main end
}