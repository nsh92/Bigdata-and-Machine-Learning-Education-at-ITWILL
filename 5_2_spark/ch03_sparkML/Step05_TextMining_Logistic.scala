package com.spark.ch03_sparkML
import org.apache.spark.sql.SparkSession
import org.apache.spark.ml.feature.StringIndexer    // y변수(더미변수) 생성 : ham(0), spam(1)
import org.apache.spark.ml.feature.VectorAssembler  // x변수 : features 생성
import org.apache.spark.ml.feature.{RegexTokenizer, StopWordsRemover, CountVectorizer, IDF}
                                    // 토큰 생성(word),     불용어 제거,        고유번호 ,     가중치(희소행렬)      
import org.apache.spark.ml.classification.LogisticRegression
import org.apache.spark.ml.evaluation.MulticlassClassificationEvaluator



object Step05_TextMining_Logistic {
     def main(args: Array[String]): Unit = {
    
     // SparkSession 객체 생성 
     val spark = SparkSession.builder
                 .master("local") 
                 .appName("dataFrameAPI")
                 .getOrCreate()
     
     // 1. dataset load
     val df = spark.read
              .format("csv")
              .option("header", "false")
              .option("delimiter", ",")
              .option("inferSchema", "true")
              .load("src/main/resources/sms_spam_data.csv")
     df.show()
     /*
      * +----+--------------------+
        | _c0|                 _c1|
        +----+--------------------+
        | ham|Go until jurong p...|
        
              전처리 과정 : _c0 -> 더미변수, _c1 => sparse matrix(features)
      */
     
     // 2. StringIndexer : String(ham, spam) -> 더미변수
     val idx = new StringIndexer()
               .setInputCol("_c0")
               .setOutputCol("label")
     // fit() : 모델 생성 -> transform() : old DF -> new DF
     val sms_data_label =  idx.fit(df).transform(df)
     sms_data_label.show()
     
     // 3. RegexTokenizer 토큰 생성기 : 정규표현식을 이용하여 토큰을 생성함
     val tokenizer =  new RegexTokenizer()
                      .setInputCol("_c1")     // 문장이 들어감
                      .setOutputCol("words")  // 단어가 저장됨
                      .setPattern("\\W+")     // 토큰 구분자 : 정규표현식
     val tokenized = tokenizer.transform(sms_data_label)
     tokenized.show()
     
     // 4. StopWordsRemover 불용어 족치기
     val stopWord = new StopWordsRemover()
                    .setInputCol("words")   // 정제 전 단어들
                    .setOutputCol("terms")  // 정제된 단어들
     // old DF -> new DF               
     val newData = stopWord.transform(tokenized)
     newData.select("words", "terms").show()
     
     // 5. CountVectorizer : word -> 고유번호, 단어 길이 제한
     val countVec = new CountVectorizer()
                    .setInputCol("terms")       // 단어
                    .setOutputCol("countVec")  // 고유 번호
                    .setVocabSize(4000)        // 단어 길이
                
     // fit() : 모델 ->transform() : old -> new DF               
     val newDataCount = countVec.fit(newData).transform(newData)
     newDataCount.show()
     
     // 6. IDF : 단어 출현빈도수에 대한 가중치(TFiDF)
     val tfidf = new IDF()
                 .setInputCol("countVec")
                 .setOutputCol("tfidfVec")  // features
     val tfidf_data = tfidf.fit(newDataCount).transform(newDataCount)
     tfidf_data.show()
     // label : y, tfidfVec : x
     tfidf_data.select("label","tfidfVec").show(false)
     
     // 7. features 생성
     val assemble = new VectorAssembler()
                    .setInputCols(Array("tfidfVec"))
                    .setOutputCol("features")
     // old DF -> new DF
     val data = assemble.transform(tfidf_data)
     data.show()     
     data.select("label", "features").show() // libsvm file
     
     // 8. train / test split
     val Array(train, test) = data.randomSplit(Array(0.8, 0.2))
     
     // 9. model
     val lr = new LogisticRegression()
                  .setMaxIter(10)
                  .setRegParam(0.01)
                  .setLabelCol("label")
                  .setFeaturesCol("features")
     
     val model = lr.fit(train)
     val pred = model.transform(test)
     pred.show()
     pred.select("label", "prediction").show(1000)
     
     // 10. 모델 평가
     val evaluator =  new MulticlassClassificationEvaluator()
                          .setLabelCol("label")
                          .setPredictionCol("prediction")
     val acc = evaluator.setMetricName("accuracy").evaluate(pred)
     val f1 = evaluator.setMetricName("f1").evaluate(pred)
     print(s"accuray : ${acc}, f1 score : ${f1}")

     
     spark.close()
     }
}