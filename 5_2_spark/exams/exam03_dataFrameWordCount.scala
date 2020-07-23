package com.spark.exams

import org.apache.spark.sql.SparkSession

object exam03_dataFrameWordCount {
  def main(args: Array[String]): Unit = {
    
     // SparkSession 객체 생성 
     val spark = SparkSession.builder
                 .master("local") 
                 .appName("dataFrameAPI")
                 .getOrCreate()
                 
      // 단계1 : HDFS의 /test 디렉터리에서 README.txt 파일 읽기(만약 file 없으면 file 업로드)
     val df = spark.read.text("hdfs://localhost:9000/test/README.txt")  
     df.show(false)
              
      // 단계2 : 줄단위 읽기 -> 공백 기준 단어 분리 
     import org.apache.spark.sql.functions._
     // 형식) df.select(column 표준내장함수)
          
     // sentence -> words
     val words = df.select(explode(split(col("value"), " ")).as("words"))
     println("단어 생성 결과")
     words.show()
     
     // word count
     val grp = words.groupBy("words") // df.groupBy()
     val wc = grp.count() // 단어 출현빈도수 
     wc.show()
      
      // 단계3 : 워드 카운트 구하고, HDFS의 /output_wc 디렉터리에 저장하기
     
      // 1) 여러개의 파일로 분산되어 저장 
      /*wc.write.format("csv")
            .option("header", "true")
            .mode("overwrite")
            .save("hdfs://localhost:9000/output_wc")*/
      
      // 2) 하나의 파일로 묶어서 저장       
      wc.coalesce(1)
        .write.format("csv")
        .option("header", "true")
        .mode("overwrite")
        .save("hdfs://localhost:9000/output_wc")
        
      println("file saved")       
      
      // 단계4 : HDFS의 /output_wc 디렉터리에 저장된 결과 파일 보기         
      /*
       * > hdfs dfs -ls /output_wc
       * > hdfs dfs -cat /output_wc/part*      
       */
            
     // 객체 닫기 
     spark.close()
     
  }
}