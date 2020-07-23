package com.spark.exams

  /*
   * 문) iris_libsvm.txt 파일을 이용하여 로지스틱 선형회귀모델을 생성하시오. 
   * y변수 : label 
   * x변수 : features
   * train/test split 비율 - 70 : 30 
   * train set : model 생성 
   * test set : model 평가(accuracy, f1 score)   
   */

import org.apache.spark.sql.SparkSession
import org.apache.spark.ml.feature.VectorAssembler // x,y 변수 선택 
import org.apache.spark.ml.classification.{LogisticRegression, LogisticRegressionModel} // model, save/load 
import org.apache.spark.ml.{Pipeline, PipelineModel} // pipeline model, save/load
import org.apache.spark.ml.evaluation.MulticlassClassificationEvaluator // model 평가

object exam05_SparkML_logisticRegression {
  def main(args: Array[String]) {

    val spark = SparkSession
      .builder()
      .appName("Logistic_PipelineSample")
      .master("local[*]")
      .getOrCreate()

    // 1. data set Load
    val data = spark.read.format("libsvm")
      .load("src/main/resources/iris_libsvm.txt") 
    data.show() // label, features 확인 
          

    // 2. train/test split    
    val Array(train, test) = data.randomSplit(Array(0.7, 0.3), seed = 123)  
    
    // 3. model 생성 환경 : 로지스틱 회귀 모델 
    val lr = new LogisticRegression()
                 .setMaxIter(10)              // 반복학습 횟수
                 .setRegParam(0.01)           // 학습률
                 .setLabelCol("label")       // Y변수
                 .setFeaturesCol("features")
    val model = lr.fit(train)
    
    val pred = model.transform(test)
    pred.show()
    pred.select("label", "prediction").show()
        
    // 4. model 평가 : 이항/다항 모두 적용 가능 
    val evaluator = new MulticlassClassificationEvaluator()
                        .setLabelCol("label") 
                        .setPredictionCol("prediction")
    val acc = evaluator.setMetricName("accuracy").evaluate(pred)
    val f1 = evaluator.setMetricName("f1").evaluate(pred)
    println(s"accuracy : ${acc}, f1 score : ${f1}")
    
    
    spark.stop()
  }
  
}