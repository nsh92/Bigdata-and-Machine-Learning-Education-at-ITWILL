package com.spark.ch03_sparkML
import org.apache.spark.sql.SparkSession
import org.apache.spark.ml.feature.VectorAssembler
import org.apache.spark.ml.classification.{LogisticRegression, LogisticRegressionModel}
import org.apache.spark.ml.evaluation.MulticlassClassificationEvaluator
import org.apache.spark.ml.{Pipeline, PipelineModel} // 파이프라인 관련 

/*
 * 로지스틱 회귀 + 파이프라인(model workfolw)
 */


object Step04_logistic_Pipeline {
    def main(args: Array[String]): Unit = {
    
     // SparkSession 객체 생성 
     val spark = SparkSession.builder
                 .master("local") 
                 .appName("dataFrameAPI")
                 .getOrCreate()
     
     // 1. dataset 생성
     import spark.implicits._  // scala -> DF
     // 1) train set : 키 몸무게 나이 성별
     val train = List((171, 68.65, 29, 1),
                      (175, 74.5, 35, 1),
                      (159, 58.6, 29, 0)).toDF("height", "weight", "age", "gender")
     train.show()
     // 2) test set : 키 몸무게 나이 성별
     val test = List((169, 65.0, 35, 1),
                     (161, 58.6, 29, 0),
                     (171, 70.5, 35, 1)).toDF("height", "weight", "age", "gender")
     test.show()
     
     // 2. assembler 생성 : features
     val assembler = new VectorAssembler()
                    .setInputCols(Array("height", "weight", "age")) // x변수 선택 
                    .setOutputCol("features") // x변수 -> features 지정
     val trainset = assembler.transform(train) // old DF -> new DF
     trainset.show()               
     
     // 3. model 생성
     val lr_obj = new LogisticRegression()
                  .setMaxIter(10)              // 반복학습 횟수
                  .setRegParam(0.01)           // 학습률
                  .setLabelCol("gender")       // Y변수
                  .setFeaturesCol("features")  // X변수
     val model = lr_obj.fit(trainset)              // 모델 생성 // 여까지 step 그대로 퍼옴
     
     // 4. 파이프라인 모델 생성
     // features 생성 -> lr_model 생성
     val pipeline = new Pipeline().setStages(Array(assembler, lr_obj))
     
     val PipeLineModel = pipeline.fit(train) // 모델 생성
     
     val pred =  PipeLineModel.transform(test) // 모델 평가
     pred.show()
     
     // 5. 파이프라인 sava/load
     val path = "C:/hadoop-2.6.0/pipeModel"
     PipeLineModel.write.overwrite().save(path) // model save
     println("model saved")
   
     //load
     val new_pipe = PipelineModel.load(path)
     val pred1 = new_pipe.transform(train)
     pred1.show()

     
     spark.close()
     }
}