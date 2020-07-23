package com.spark.ch03_sparkML
import org.apache.spark.sql.SparkSession
import org.apache.spark.ml.classification.{DecisionTreeClassifier}
import org.apache.spark.ml.evaluation.MulticlassClassificationEvaluator
import org.apache.spark.mllib.evaluation.MulticlassMetrics // RDD ml의 교차분할표
/*
 * Tree model + confusion matrix
 * 
 * ml vs mllib
 * ml : DF로 모델링
 * mllib : RDD로 모델링
 */






object Step06_Classification {
     def main(args: Array[String]): Unit = {
    
     // SparkSession 객체 생성 
     val spark = SparkSession.builder
                 .master("local") 
                 .appName("dataFrameAPI")
                 .getOrCreate()
                 
    // 1. dataset load                 
    val df = spark.read.format("libsvm")
             .load("src/main/resources/iris_libsvm.txt")
    df.show()                 
    
    // 2. train / test split
    val Array(train, test) = df.randomSplit(Array(0.7, 0.3))
    // 메모리(캐시)에 데이터셋 로딩
    train.cache()
    test.cache()
    
    // 3. Tree Model
    val dt = new DecisionTreeClassifier()
             .setLabelCol("label")
             .setFeaturesCol("features")
             //.setPredictionCol("predictions")
    val model = dt.fit(train)
    
    println(s"변수의 중요도 : ${model.featureImportances}")
    
    // old DF(dt) -> new DF(pred)
    val pred = model.transform(test)
    pred.show()
    
    val evaluator = new MulticlassClassificationEvaluator()
                    .setLabelCol("label")
                    .setPredictionCol("prediction")
    val acc = evaluator.setMetricName("accuracy").evaluate(pred)
    val f1 = evaluator.setMetricName("f1").evaluate(pred)
    
    // confusion matrix
    import spark.implicits._ // 스칼라->DF, RDD<->DF
    // DF -> rdd
    val predrdd = pred.select("label", "prediction").as[(Double, Double)].rdd
    println(predrdd) // MapPartitionsRDD[78] at rdd at Step06_Classification.scala:61
    val con_mat = new MulticlassMetrics(predrdd)  // RDD데이터를 요구함
    println(con_mat.confusionMatrix)              
     
     spark.close()
}}