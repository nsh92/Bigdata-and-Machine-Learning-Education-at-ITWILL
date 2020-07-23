package com.spark.ch02_dataFrame_SQL

import org.apache.spark.sql.SparkSession // DataFrame 생성 

/*
 * case class -> DataFrame 
 *  - 서로 다른 type을 갖는 원소를 이용하여 객체 생성 
 */

// case class 선언 
case class Dataset(var name : String, var pay : Int, var bouns : Int, var dno : Int)

object Step07_dataFrame_class {
  def main(args: Array[String]): Unit = {
    
     // SparkSession 객체 생성 
     val spark = SparkSession.builder
                 .master("local") 
                 .appName("dataFrameAPI")
                 .getOrCreate()
                 
     // class object : 생성자 이용 
     val row1 = Dataset("홍길동", 250, 50, 10)
     val row2 = Dataset("이순신", 350, 80, 20)
     val row3 = Dataset("유관순", 200, 70, 10)
     
     import spark.implicits._
     
     val emp_df = List(row1, row2, row3).toDF("name","pay","bonus","dno")
     emp_df.show()
                 
     // 객체 닫기 
     spark.close()
     
  }
}




