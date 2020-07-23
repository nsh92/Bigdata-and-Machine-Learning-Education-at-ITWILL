package com.spark.exams

import org.apache.spark.sql.SparkSession // DataFrame object
import org.apache.spark.ml.regression.LinearRegression // model 생성 
import org.apache.spark.ml.feature.VectorAssembler // x, y변수 선택
import org.apache.spark.ml.evaluation.RegressionEvaluator // model 평가 

  /*
   *  문) score_iq.csv 파일을 대상으로 선형회귀분석을 수행하시오.
   *  - y 변수(label) : score
   *  - x 변수(features) : iq, academy, game, tv
   *  - sid 변수 제거 
   *  - train/test split(8:2)
   *  - model 생성 : train set
   *  - model 평가  : test set 
   */

object exam04_sparkML_linearRegression {
  
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
              .load("src/main/resources/score_iq.csv")
     df.show()  // df 내용 보기
     val score_df = df.drop("sid") // sid 칼럼 삭제 
     score_df.printSchema() // 칼럼 type 확인 
     
     score_df.show() // |score| iq|academy|game| tv|
     

     // 2. assembler 생성 
     val assember = new VectorAssembler()
         .setInputCols(Array("iq", "academy", "game", "tv"))
         .setOutputCol("features")
     
     // old DF(|score| iq|academy|game| tv|) -> new DF(|score| iq|academy|game| tv|features|)
     val data = assember.transform(score_df)
     data.show()
     
     // 3. train/test split
     val Array(train, test) = data.randomSplit(Array(0.8, 0.2))
     
     // 4. model 생성 
     val lr = new LinearRegression()
              .setMaxIter(10) // 반복학습 
              .setFeaturesCol("features") // x변수 
              .setLabelCol("score") // y변수 
     
     val model = lr.fit(train)     
     println(s"기울기 : ${model.coefficients}, 절편 : ${model.intercept}")
     
     // 5.model 평가
     val pred = model.transform(test)     
     pred.show() // |score| iq|academy|game| tv|           features|       prediction|
     
     pred.select("score", "prediction", "features").show()
     /*
      * +-----+-----------------+-------------------+
      * |score|       prediction|           features|
      * +-----+-----------------+-------------------+
      * |   65|64.05187421922808|[105.0,0.0,4.0,4.0]|
      * |   65|64.05187421922808|[105.0,0.0,4.0,4.0]|
      */
     
     val evaluator = new RegressionEvaluator()
                     .setLabelCol("score")
                     .setPredictionCol("prediction")
     val mse = evaluator.setMetricName("mse").evaluate(pred)
     val r2 = evaluator.setMetricName("r2").evaluate(pred)
     
     println(s"mse : ${mse}, r2 : ${r2}")
     // mse : 1.527177246820358, r2 : 0.9548837088854739
    }       
}








