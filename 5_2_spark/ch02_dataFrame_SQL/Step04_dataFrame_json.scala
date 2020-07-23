package com.spark.ch02_dataFrame_SQL
import org.apache.spark.sql.SparkSession
import org.apache.spark.ml.regression.LinearRegression

/*
 * json file -> DF
 */

object Step04_dataFrame_json {
  def main(args: Array[String]): Unit = {
    val spark = SparkSession.builder
                .master("local")
                .appName("dataFrameAPI")
                .getOrCreate()
                
    // path 변수 생성
    val path = "src/main/resources/usagov_bitly.txt"            
    // 제이슨 -> DF
    val df = spark.read.json(path)
    df.show()
    
    df.printSchema()
    
    // 가상 테이블 만들기
    df.createOrReplaceTempView("json_df")
    
    // sql문 작성
    spark.sql("select * from json_df").show()
    spark.sql("select count(*) from json_df").show()
    
    // subset 생성
    val nk_true = spark.sql("select * from json_df where nk=1")
    nk_true.show()
    println(nk_true.count())
    
    spark.close()             
  }
}