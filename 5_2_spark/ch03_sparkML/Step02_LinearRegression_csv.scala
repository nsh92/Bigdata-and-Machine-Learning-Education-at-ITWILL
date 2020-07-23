package com.spark.ch03_sparkML

/*
 * csv file + Linear Regression model 
 */

import org.apache.spark.sql.SparkSession // DataFrame object
import org.apache.spark.ml.regression.LinearRegression // model 생성 
import org.apache.spark.ml.feature.VectorAssembler // x, y변수 선택
import org.apache.spark.ml.evaluation.RegressionEvaluator // model 평가 

object Step02_LinearRegression_csv {
  
    def main(args: Array[String]): Unit = {
    
     // SparkSession 객체 생성 
     val spark = SparkSession.builder
                 .master("local") 
                 .appName("dataFrameAPI")
                 .getOrCreate()
                 
     // 1. data set load 
     val df = spark.read
              .format("csv")
              .option("header", "true")
              .option("delimiter", ",")
              .option("inferSchema", "true")
              .load("src/main/resources/iris.csv")
     df.show()  // df 내용 보기
     
     // 칼럼명 변경하기  
     val colNames = Seq("Sepal_Length","Sepal_Width","Petal_Length","Petal_Width","Species")
     // old DF -> new DF
     val iris_df = df.toDF(colNames : _*)
     iris_df.show()
     
     // x, y변수 생성 : y(Sepal_Length), x(나머지 3개)
     val iris_xy = iris_df.drop("Species")
     iris_xy.show()
     // |Sepal_Length|Sepal_Width|Petal_Length|Petal_Width|
     
     // 2. label(y), features(x) 생성 : VectorAssembler
     val assemble = new VectorAssembler()
                    .setInputCols(Array("Sepal_Width", "Petal_Length", "Petal_Width")) // x변수 선택 
                    .setOutputCol("features") // x변수 -> features 지정 
     
     val data = assemble.transform(iris_xy)
     data.show(false)
     // |Sepal_Length|Sepal_Width|Petal_Length|Petal_Width|     features|
     
     data.select("Sepal_Length", "features").show(false)
     
     // 3. train/test split(70% vs 30%)
     val Array(train, test) = data.randomSplit(Array(0.7, 0.3), seed = 123)     
     
     // 4. model 생성 : train set 이용 
     val lr = new LinearRegression()
              .setMaxIter(10) // hyper parameter
              .setFeaturesCol("features") // x변수 
              .setLabelCol("Sepal_Length") // y변수 
     
     
     println("Train dataset info")         
     val model = lr.fit(train) // 훈련셋 이용
     println(s"기울기 : ${model.coefficients}, 절편 :${model.intercept}")
     
     val model_summary = model.summary
     println(s"Train MSE : ${model_summary.meanSquaredError}")
     println(s"Train r2 score : ${model_summary.r2}")
     
     // 5. model 평가 : test set 이용 
     val pred = model.transform(test)
     pred.show()
     // |Sepal_Length|Sepal_Width|Petal_Length|Petal_Width|     features|       prediction|
     
     // 평가 객체 생성 
     val evaluater = new RegressionEvaluator()
                         .setLabelCol("Sepal_Length") // 정답 칼럼 
                         .setPredictionCol("prediction") // 예측치 칼럼 
          
     // 평가 방법과 예측치 변수 지정 
     val rmse = evaluater.setMetricName("rmse").evaluate(pred) // root 평균 제곱 오차                  
     val mse = evaluater.setMetricName("mse").evaluate(pred) // 평균 제곱 오차 
     val mae = evaluater.setMetricName("mae").evaluate(pred) // 평균 절대값 오차 
     val r2_score = evaluater.setMetricName("r2").evaluate(pred)
     
     println("Test set 적용 model 평가 결과")
     println(s"rmse : ${rmse}, mse : ${mse}, mae : ${mae}, r2 : ${r2_score}") 
     // rmse : 0.35527888737371266, mse : 0.1262230878135032, mae : 0.29288148507062084, r2 : 0.8295839370878721
     
     // 객체 닫기 
     spark.close()
  }
  
}





