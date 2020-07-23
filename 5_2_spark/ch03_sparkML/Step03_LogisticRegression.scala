package com.spark.ch03_sparkML // DF 생성
import org.apache.spark.sql.SparkSession // features 생성
import org.apache.spark.ml.feature.VectorAssembler
import org.apache.spark.ml.classification.{LogisticRegression, LogisticRegressionModel} // 모델 생성, save/load
import org.apache.spark.ml.evaluation.MulticlassClassificationEvaluator


object Step03_LogisticRegression {

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
     val assemble_train = new VectorAssembler()
                    .setInputCols(Array("height", "weight", "age")) // x변수 선택 
                    .setOutputCol("features") // x변수 -> features 지정
     val trainset = assemble_train.transform(train) // old DF -> new DF
     trainset.show()               
     
     // 3. model 생성
     val lr = new LogisticRegression()
                  .setMaxIter(10)              // 반복학습 횟수
                  .setRegParam(0.01)           // 학습률
                  .setLabelCol("gender")       // Y변수
                  .setFeaturesCol("features")  // X변수
     val model = lr.fit(trainset)              // 모델 생성
     
     // 4. model 평가
     val assemble_test = new VectorAssembler()
                    .setInputCols(Array("height", "weight", "age")) // x변수 선택 
                    .setOutputCol("features") // x변수 -> features 지정
     val testset = assemble_test.transform(test) // old DF -> new DF
     testset.show()    
     
     // model 예측치
     val pred = model.transform(testset)
     pred.show()
     pred.select("gender", "prediction").show()  // 정답과 예측치만 출력
     
     // 이항 or 다항 분류 평가
     val evaluator = new MulticlassClassificationEvaluator()
                          .setLabelCol("gender")           // 정답 컬럼
                          .setPredictionCol("prediction")  // 예측치 컬럼
     val acc = evaluator.setMetricName("accuracy").evaluate(pred)
     val f1 = evaluator.setMetricName("f1").evaluate(pred)
     println(s"accuracy : ${acc}, f1 score : ${f1}")
     
     // 5. model save & load
     val path = "C:/hadoop-2.6.0/lrModel"
     
     model.write.overwrite().save(path)
     println("model saved")
     
     // model load
     val new_lrmodel = LogisticRegressionModel.load(path)
     val result = new_lrmodel.transform(trainset)
     println("hi")
     result.show()
     result.select("gender", "prediction").show()
     
     spark.close()
     }
    
}