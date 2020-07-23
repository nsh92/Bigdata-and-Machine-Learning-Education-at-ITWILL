package com.spark.exams

import org.apache.spark.sql.SparkSession
// label, features 전처리 
import org.apache.spark.ml.feature.{StringIndexer, VectorAssembler}
import org.apache.spark.ml.clustering.{KMeans, KMeansModel}
import org.apache.spark.mllib.evaluation.MulticlassMetrics

object exam07_SparkML_clustering {
  /*
   *  문) sample_kmeans_data.txt 파일을 이용하여 2개의 군집으로 k-means model을 생성하고,
   *     군집을 확인 하시오.
   */
  def main(args: Array[String]) {
    val spark = SparkSession
      .builder()
      .appName("exam07_SparkML_clustering")
      .master("local[*]")
      .getOrCreate()

    val data = spark.read.format("libsvm")
               .load("src/main/resources/sample_kmeans_data.txt")
    data.show()
    
    val kmeans = new KMeans()
                     .setK(2)
                     .setSeed(123l)
    val model = kmeans.fit(data)                 
    val pred = model.transform(data)
    pred.show()
     
  }           
}