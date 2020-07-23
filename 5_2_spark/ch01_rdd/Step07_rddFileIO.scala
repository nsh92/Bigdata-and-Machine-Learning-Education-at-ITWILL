package com.spark.ch01_rdd
import org.apache.spark.SparkConf
import org.apache.spark.SparkContext

object Step07_rddFileIO {
  def main(args: Array[String]): Unit = {
  val conf = new SparkConf()
    .setAppName("SparkTest")
    .setMaster("local")
  val sc = new SparkContext(conf)
  
  val filePath = "src/main/resources/"
  val rdd = sc.textFile(filePath + "input.txt")
  println(rdd.collect.mkString(", "))
  
  val rdd2 = rdd.flatMap(_.split(" ")) // words
  
  val rdd3 = rdd2.filter(_.size >= 3)
  
  val wc = rdd3.map((_, 1)).reduceByKey(_+_)
  
  wc.saveAsTextFile(filePath + "output")
  println("성공")
  sc.stop()   
  }
}