package com.spark.ch03_sparkML

import org.apache.spark.sql.SparkSession // DataFrame object
import org.apache.spark.ml.regression.LinearRegression // model 생성 

/*
 * libsvm file + linear regression model
 *   - libsvm file : label(y변수), features(x변수) 
 */

object Step01_LinearRegression {
   
    def main(args: Array[String]): Unit = {
    
     // SparkSession 객체 생성 
     val spark = SparkSession.builder
                 .master("local") 
                 .appName("dataFrameAPI")
                 .getOrCreate()
                 
     // 1. data set load 
     val dataset = spark.read.format("libsvm")
                  .load("src/main/resources/iris_libsvm.txt")
     
     //dataset.show() // 20 rows             
     dataset.show(150, false) // 전체 관측치 확인 
     /*
      * +-----+-------------------------------+
      * |label|features                       |
      * +-----+-------------------------------+
      * |0.0  |(4,[0,1,2,3],[5.1,3.5,1.4,0.2])| (size, index, data)
      *   생략
      * |2.0  |(4,[0,1,2,3],[5.9,3.0,5.1,1.8])|
      * +-----+-------------------------------+  
      */
     
     // 2. model 생성 
     val lr = new LinearRegression() // model 객체 생성  
     
     val model = lr.fit(dataset) // model 생성 
     
     // 3. model 결과 확인/평가  
     print(s"기울기 : ${model.coefficients}, 절편 : ${model.intercept}")
     // 기울기 : [-0.10974146329314512,-0.04424044671758584,0.22700138217196836,0.6098941197163089], 절편 : 0.19208399482813024
     
     val model_summary = model.summary
     
     // 잔차(오차)
     model_summary.residuals.show()
     
     // mse or r2 score     
     println(s"r2 score : ${model_summary.r2}") // 비정규화 
     println(s"MSE : ${model_summary.meanSquaredError}") // 정규화 
     // r2 score : 0.9304223675331595
     // MSE : 0.04638508831122697

     // 객체 닫기 
     spark.close()
     
  }
}












