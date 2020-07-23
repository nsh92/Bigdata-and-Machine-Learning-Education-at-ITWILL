package com.spark.ch01_rdd
import org.apache.spark.SparkConf
import org.apache.spark.SparkContext

/*
 * RDD Transformation : join 관련 메소드
 * 
 */


object Step03_rddTrans_join {
  
  def zip(sc : SparkContext) : Unit = {
    val rdd1 = sc.parallelize(Seq("a", "b", "c"))
    val rdd2 = sc.parallelize(List(1, 2, 3))
    val zip_re = rdd1.zip(rdd2)
    zip_re.foreach(println)
  }
  
  def reduceByKey(sc : SparkContext) : Unit = {
    val lst = List("data", "text", "word", "data", "word", "data") // 컬렉션 data
    val rdd = sc.parallelize(lst) // RDD 생성
    // Transformation : old rdd -> new rdd
    val new_rdd = rdd.map((_, 1)) // ("data", 1) ... ("word",1)
    println(new_rdd.collect.mkString(", "))    
    // Transformation : old rdd -> new rdd
    new_rdd.reduceByKey(_+_).foreach(println)
    
  }
  
  def main(args: Array[String]): Unit = {
  val conf = new SparkConf()
    .setAppName("SparkTest")
    .setMaster("local")
  val sc = new SparkContext(conf)
  
  // 1. join : 동일한 키를 기준으로 원소 묶음 : 길이는 서로 다름
  val rdd1 = sc.parallelize(Seq("kim", "lee", "park", "choi")).map((_,1))  // ("kim", 1)
  val rdd2 = sc.parallelize(List("lee","choi")).map((_,2))                 // ("lee", 2)
  println(rdd1.collect.mkString(" "))
  println(rdd2.collect.mkString(" "))
  
  val join_re = rdd1.join(rdd2) // 동일키 기준 join
  println(join_re.collect.mkString(", ")) // (lee,(1,2)), (choi,(1,2)) 이 최를 키로하여 원소 1, 2가 묶임
  
  // 2. zip : 원소의 순서대로 원소 묶음 : 길이는 동일함
  zip(sc)
  
  // 3. reduceByKey : 동일한 키를 기준으로 value를 합친다
  reduceByKey(sc)
  
  }
}