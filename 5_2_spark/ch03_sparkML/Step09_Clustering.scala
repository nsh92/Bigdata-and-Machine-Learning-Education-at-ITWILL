package com.spark.ch03_sparkML
import org.apache.spark.sql.SparkSession
import org.apache.spark.ml.clustering.{KMeans, KMeansModel}
import org.apache.spark.mllib.evaluation.MulticlassMetrics



object Step09_Clustering {
    def main(args: Array[String]): Unit = {
    
    // SparkSession 객체 생성 
    val spark = SparkSession.builder()
                .master("local") 
                .appName("Clustering")
                .getOrCreate()
    
    // 1. dataset load
    val data = spark.read.format("libsvm")
               .load("src/main/resources/iris_libsvm.txt")
    data.show()
    
    // 2. k-means : 확인적 군집분석(k=군집수)
    val kmeans = new KMeans()
                     .setK(3)
                     .setSeed(123l)
    val model = kmeans.fit(data)                 
    val pred = model.transform(data)
    pred.show(150, false)
    
    // 3. model 평가
    import spark.implicits._
    
    val predRdd = pred.select("label", "prediction").as[(Double, Double)].rdd
    val conMax = new MulticlassMetrics(predRdd)
    println(conMax.confusionMatrix)
    
    
    spark.close()
    }            
}