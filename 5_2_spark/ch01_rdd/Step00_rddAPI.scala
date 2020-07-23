package com.spark.ch01_rdd
import org.apache.spark.SparkConf
import org.apache.spark.SparkContext


object Step01_rddAPI {
  def main(args: Array[String]): Unit = {
  // 1. SparkConf 생성
  val conf = new SparkConf()
    .setAppName("SparkTest")
    .setMaster("local") // Spark 환경 객체
    
  // 2. SparkContext 객체 생성 : rdd data 생성
  val sc = new SparkContext(conf)
  }// main end
}// class end
// rdd 생성을 위한 기본와꾸