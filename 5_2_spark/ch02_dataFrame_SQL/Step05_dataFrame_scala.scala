package com.spark.ch02_dataFrame_SQL

import org.apache.spark.sql.SparkSession // DataFrame 생성
/*
 * scala collection -> spark DataFrame
 */
object Step05_dataFrame_scala {
   def main(args: Array[String]): Unit = {
    
     // SparkSession 객체 생성 
     val spark = SparkSession.builder
                 .master("local") 
                 .appName("dataFrameAPI")
                 .getOrCreate()
     
     // tuple vector 
     val v1 = (1001, 250, 60, 10) // eno, pay, bonus, dno
     val v2 = (1002, 350, 70, 20)
     val v3 = (1003, 200, 55, 10)
     val v4 = ("kim", 300, 100, 30) // ename, pay, bouns, dno
     
     // spark 암묵적 변환 방식 : scala -> DF
     import spark.implicits._ 
     // scala -> DataFrame
     val emp = List(v1, v2, v3, v4).toDF("eno", "pay", "bonus", "dno")
     emp.show()
     
     // column 사용을 위한 표준내장함수 
     import org.apache.spark.sql.functions._
     
     // 형식) df.select(column 표준내장함수)
     emp.select(max("pay"), sum("bonus"),mean("bonus"),stddev("bonus")).show()
     
     
     // 객체 닫기 
     spark.close()
     
  }
}