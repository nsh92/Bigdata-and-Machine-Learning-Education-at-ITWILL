package com.spark.ch01_rdd
import org.apache.spark.SparkConf
import org.apache.spark.SparkContext
/*
 * RDD Transformation : map 관련 메소드
 *  1. rdd.map()
 *  2. rdd.flatMap()
 *  3. rdd.filter()
 */
object Step02_rddTrans_map {
  def main(args: Array[String]): Unit = {
  val conf = new SparkConf()
    .setAppName("SparkTest")
    .setMaster("local")
  val sc = new SparkContext(conf)
  
  // 1. map(매핑연산자) : rdd 원소를 순서대로 받아서 연산 수행
  val rdd = sc.parallelize(List("a","b","c")) // 파티션 생략
  val map_re = rdd.map((_, 1)) // (a, 1), (b, 1), (c, 1)
  map_re.foreach(println) 
  
  val rdd2 = sc.parallelize(1 to 10)
  val map_re2 = rdd2.map(_+1)
  // rdd로부터 원소를 꺼내옴 : collect()
  println(map_re2.collect()) // [I@5df417a7 : mkstring 있고 없고 차이 확인
  println(map_re2.collect().mkString(", "))
  
  // 2. flatmap(매핑연산자) : rdd 원소를 순서대로 받아서 연산 수행(1:N)
  val names = sc.parallelize(List("홍길동", "강호동", "이순신, 강감찬, 유관순", "홍길동, 이순신, 강감찬"))
  val flatmat_re = names.flatMap(_.split(",")) // 3덩어리가 8개 원소로 쪼개지는 효과
  println("size : " + flatmat_re.count())
  println(flatmat_re.collect().mkString(", "))
  
  // 3. rdd객체.filter(조건식) : rdd 원소를 순서대로 받아서 조건이 참인 원소 반환
  val filter_re = names.filter(_.size >= 9)
  println(filter_re.collect().mkString("\t"))
    
  }
}