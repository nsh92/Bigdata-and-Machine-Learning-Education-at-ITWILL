package com.spark.ch02_dataFrame_SQL
import org.apache.spark.sql.SparkSession
import org.apache.spark.ml.regression.LinearRegression

/*
 * libsvm -> DF 생성
 *  - libsvm : label(y), features(x)
 */
object dataFrame_Step03_dataFrame__libsvm {
  def main(args: Array[String]): Unit = {
    // SparkSession 객체 생성 new없이 생성하는 것이 특징
    val spark = SparkSession.builder
                .master("local")
                .appName("dataFrameAPI")
                .getOrCreate()

    val df = spark.read.format("libsvm")
             .load("src/main/resources/iris_libsvm.txt")
    df.show(false)
                

  
    // 선형 회귀
    val trainset = spark.read.format("libsvm")
                   .load("src/main/resources/sample_libsvm_data.txt")
    trainset.show()
    
    // object 생성
    val lr = new LinearRegression()
    // 모델 생성
    val model = lr.fit(trainset)
    val trainSummary = model.summary
    
    // 모델 평가
    println(s"r2 scroe = ${trainSummary.r2}") 
    
    spark.close()
  }
}