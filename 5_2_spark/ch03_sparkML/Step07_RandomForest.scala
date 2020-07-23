package com.spark.ch03_sparkML
import org.apache.spark.sql.SparkSession
import org.apache.spark.ml.feature.StringIndexer
import org.apache.spark.ml.classification.{RandomForestClassifier, RandomForestClassificationModel}
import org.apache.spark.ml.evaluation.MulticlassClassificationEvaluator
import org.apache.spark.mllib.evaluation.MulticlassMetrics
import org.apache.spark.ml.feature.VectorAssembler




object Step07_RandomForest {
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
              .load("src/main/resources/weather.csv")
     df.show()
     df.printSchema()
     
     // 2. label 생성 : RainTomorrow -> yes / no -> 더미(1/0)
     val sIndexer = new StringIndexer()
               .setInputCol("RainTomorrow")
               .setOutputCol("label")

     val sIndexerDF =  sIndexer.fit(df).transform(df)
     sIndexerDF.show()
     
     // 3. features 생성 : Sunshine|WindGustSpeed|Humidity|Pressure -> features
     val assembler = new VectorAssembler()
                     .setInputCols(Array("Sunshine", "WindGustSpeed", "Humidity", "Pressure"))
                     .setOutputCol("features")
     val weather_df = assembler.transform(sIndexerDF)
     weather_df.show()
     
     // 4. train / test split (7:3)
     val Array(train, test) = weather_df.randomSplit(Array(0.7,0.3), seed=123)
     
     // 5. model 생성
     val rf = new RandomForestClassifier()
              .setLabelCol("label")
              .setFeaturesCol("features")
              .setNumTrees(10) // 트리의 수
              
     val model = rf.fit(train)
     val pred = model.transform(test)
     pred.show()
     println("hi")
     pred.select("label", "prediction").show()

     // 6. 모델 평가
     
     // (1) accuracy 분류정확도 
     val evaluator = new MulticlassClassificationEvaluator()
                     .setLabelCol("label")
                     .setPredictionCol("prediction")

     println("hello")
     val acc = evaluator.setMetricName("accuracy").evaluate(pred)
     val f1 = evaluator.setMetricName("f1").evaluate(pred)
     println("haha")
     println(s"accuracy : ${acc}, f1 score : ${f1}")
     
     // (2) confusion matrix
     import spark.implicits._
     val pred_rdd = pred.select("label", "prediction").as[(Double, Double)].rdd
     val con_max = new MulticlassMetrics(pred_rdd)
     println(con_max.confusionMatrix)
     
                          
     // 7. model save/load
     val path = "c:/hadoop-2.6.0/rfModel"
     model.write.overwrite().save(path)
     println("model save")
     
     /// model load
     val rfModel_load = RandomForestClassificationModel.load(path)
     rfModel_load.transform(test).show()
     
     spark.close()
     }
}