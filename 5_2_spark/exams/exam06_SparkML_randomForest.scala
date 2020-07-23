package com.spark.exams

import org.apache.spark.sql.SparkSession
import org.apache.spark.ml.{Pipeline, PipelineModel}
// label, features 전처리 
import org.apache.spark.ml.feature.{StringIndexer, VectorAssembler} 
// model 생성 & save
import org.apache.spark.ml.classification.RandomForestClassifier
import org.apache.spark.ml.classification.RandomForestClassificationModel
// model 평가 
import org.apache.spark.ml.evaluation.MulticlassClassificationEvaluator // model 평가  
import org.apache.spark.mllib.evaluation.MulticlassMetrics // 교차분할표 

/*
 * 문) 다음과 같은 단계별로 Pipeline 모델을 생성하시오.  
 */
object exam06_SparkML_randomForest {
    
  def main(args: Array[String]): Unit = {
    
    val spark = SparkSession
      .builder()
      .appName("exam06_SparkML_randomForest")
      .master("local[*]")
      .getOrCreate()
      
    // 단계1. dataset load   
    val filePath = "src/main/resources"  
    val df = spark.read
      .option("header", "true")
      .option("inferSchema", "true") // raw data type 적용 
      .csv(filePath + "/iris.csv")    
    
    // column 이름 변경 
    val newName = Seq("Sepal_Length","Sepal_Width","Petal_Length","Petal_Width","Species")
    val newDF = df.toDF(newName: _*)
           
    newDF.printSchema()    
    newDF.show()
    
    // 단계2. label 칼럼 생성 : Species 컬럼 이용 
    val sIndexer = new StringIndexer()
                  .setInputCol("Species")
                  .setOutputCol("label")
   
     
    // 단계3. features 칼럼  생성 : "Sepal_Length","Sepal_Width","Petal_Length","Petal_Width" 컬럼 이용  
    val assembler = new VectorAssembler()
                    .setInputCols(Array("Sepal_Length", "Sepal_Width", "Petal_Length", "Petal_Width"))
                    .setOutputCol("features")

    
    // 단계4. Split 70% vs 30% : weather_data -> data 수정 
    val Array(train, test) = newDF.randomSplit(Array(0.7,0.3))
    
    
    // 단계5. model 생성  : RandomForestClassifier 클래스 이용 
    val rf = new RandomForestClassifier()
             .setLabelCol("label")
             .setFeaturesCol("features")
             .setNumTrees(10)    
             
    // 단계6. pipeline model : step(label -> feature -> model) 
    val pipeline = new Pipeline().setStages(Array(sIndexer, assembler, rf))
    val pipeModel = pipeline.fit(train)
    val pred = pipeModel.transform(test)
    
    // 단계7. pipeline model 평가 : accuracy, confusion matrix
    val evaluator = new MulticlassClassificationEvaluator()
                    .setLabelCol("label")
                    .setPredictionCol("prediction")
    
    val acc = evaluator.setMetricName("accuracy").evaluate(pred)
    val f1 = evaluator.setMetricName("f1").evaluate(pred)
    println(s"accuracy : ${acc}, f1 score : ${f1}")
    
    import spark.implicits._
    val pred_rdd = pred.select("label", "prediction").as[(Double, Double)].rdd
    val con_max = new MulticlassMetrics(pred_rdd)
    println(con_max.confusionMatrix)
    
    
    spark.close()
  }
}