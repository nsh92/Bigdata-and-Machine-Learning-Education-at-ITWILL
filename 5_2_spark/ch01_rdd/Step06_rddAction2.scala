package com.spark.ch01_rdd

import org.apache.spark.{ HashPartitioner, SparkConf, SparkContext }
import org.apache.spark.storage.StorageLevel
import scala.collection.mutable.ListBuffer

/*
 * RDD Action 관련 method  
 *
 *  - rdd.takeSample() : RDD 원소를 대상으로 샘플 수를 지정하여 샘플링 
 *  - rdd.countByValue() : RDD 대상으로 단어 -> 출현빈도수 형태로 반환  
 *  - rdd.reduce() : RDD 전체 원소를 대상으로 하나의 값으로 병합하여 반환 
 *  - rdd.sum() : RDD 전체 원소의 합 반환 
 */

object Step06_rddAction {
  
  def takeSample(sc: SparkContext) {
    val rdd = sc.parallelize(1 to 100)
    val result = rdd.takeSample(false, 20) 
    println(result) // object info
    println(result.length) 
    result.foreach((x : Int)=>print(x+ " "))
  }

  def countByValue(sc: SparkContext) {
    val rdd = sc.parallelize(List(1, 1, 2, 3, 3))
    val result = rdd.countByValue()
    println(result) 
  }

  def reduce(sc: SparkContext) {
    val rdd = sc.parallelize(1 to 10, 3)
    val result = rdd.reduce(_+_)
    println(result) 
  }
  
  def sum(sc: SparkContext) {
    val rdd = sc.parallelize(1 to 10)
    val result = rdd.sum()
    println(result) 
  }
  
  def main(args: Array[String]) {      
      val conf = new SparkConf()
          .setAppName("WordCountMapReduce")
          .setMaster("local")
  
      val sc = new SparkContext(conf)
     
      takeSample(sc)
      //countByValue(sc)
      //reduce(sc)      
      //sum(sc)
    }

}