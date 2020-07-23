package com.spark.ch01_rdd
import org.apache.spark.SparkConf
import org.apache.spark.SparkContext
/*
 * RDD Action : load & save
 *  - rdd.collect() : rdd 원소 추출 -> vector 형식 생성
 *  - rdd.textFile() : rdd 객체를 텍스트 파일 저장
 */
object Step05_rddAction {
  def main(args: Array[String]): Unit = {
  val conf = new SparkConf()
    .setAppName("SparkTest")
    .setMaster("local")
  val sc = new SparkContext(conf)
  
  // 1. rdd.collect(), first(), take()
  val rdd = sc.parallelize(1 to 100, 5)
  println(rdd.collect.mkString(" "))
  println(rdd.first)
  println(rdd.take(10).mkString(" "))
  
  // 2. rdd = sc.textFile(local file or HDFS)
  val rdd2 = sc.textFile("file:/C:/hadoop-2.6.0/README.txt")
  println(rdd2.count())
  println(rdd.take(20).mkString("\n"))
      
  // 3. save 관련 : rdd 객체 -> 저장
  // rdd.saveAsTextFile("file:/C:/hadoop-2.6.0/output1")  // 파티션 나눈만큼 저장된 파일도 마찬가지
  // rdd2.saveAsTextFile("file:/C:/hadoop-2.6.0/output2") // 파티션 명시가 없으니 파일도 하나임
  
  // 4. HDFS file load & HDFS file save
  val hdfs_rdd = sc.textFile("hdfs://localhost:9000/test/README.txt")
  // old rdd -> new rdd
  val hdfs_rdd2 = hdfs_rdd.take(10)
  hdfs_rdd.saveAsTextFile("hdfs://localhost:9000/output")
  
  // 기존 디렉토리가 있는 경우 오류 뜸
  
  println("success")
  sc.stop
}}