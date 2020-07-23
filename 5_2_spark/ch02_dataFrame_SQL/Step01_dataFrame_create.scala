package com.spark.ch02_dataFrame_SQL
// import org.apache.spark.{SparkConf, SparkContext} // RDD 생성
import org.apache.spark.sql.SparkSession // DF 생성
object Step01_dataFrameAPI {
  def main(args: Array[String]): Unit = {
    // SparkSession 객체 생성 new없이 생성하는 것이 특징
    val spark = SparkSession.builder
                .master("local")
                .appName("dataFrameAPI")
                .getOrCreate()
    
    
    val df = spark.read
             .format("csv")
             .option("header", "true")
             .option("delimiter", ",")
             .option("inferSchema", "true")
             .load("src/main/resources/iris.csv")
             
    //df.show()  // df 내용 보기 (20)이 디폴트
    println("관측치 수 = " + df.count()) // rows
    //df.show(150)         
    
    // 컬럼 타입
    df.printSchema()  // 대충 자료구조
    
    // 컬럼 단위 통계 구하기
    // df.describe("Sepal.Length") 이래 하면 오류뜸 : .때문
    
    // 컬럼명 변경하기 : col1 ~ col4, Species
    val colNames = Seq("col1", "col2", "col3", "col4", "Species")
    // old DF -> new DF
    val iris_df = df.toDF(colNames : _*)
    iris_df.show()
    
    // 컬럼 단위 통계 구하기
    iris_df.describe("col1").show()
    
    // 집단 변수로 그룹화
    val df_grp = iris_df.groupBy("Species")
    df_grp.count().show()
    
    df_grp.max("col1").show()
    df_grp.min("col1").show()
    df_grp.mean("col1").show()
    df_grp.sum("col1").show()
    
    // DF save : project 디렉토리(로컬) 저장
    iris_df.write.format("csv")
           .option("header", "true")
           .mode("overwrite") // 기존에 뭐 있으면 덮어씌워라
           .save("src/main/resources/output_df")
    
    println("성공")
    
    iris_df.write.format("csv")
           .option("header", "true")
           .mode("overwrite") // 기존에 뭐 있으면 덮어씌워라
           .save("hdfs://localhost:9000/output_df")
    
    
    
    
    
     // 객체 닫기            
    spark.close()
  }
 
}