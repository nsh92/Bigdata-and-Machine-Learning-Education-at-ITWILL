package chap01_Variable

/*
 * Scala 변수/상수 선언
 *  - var : 값을 수정하는 변수 선언
 *  형식) var 변수명 : 자료형 = 값
 *       var num : Int = 100  num에 100이란 정수가 담김
 *       자료형 생략시 추론하는 기능이 있음
 */
object Step01_var {
  
  def main(args: Array[String]): Unit = {
     var num1 : Int = 1000 // type 명시
     println("num1="+num1) // 콘솔에 출력
     var num2 = 2000       // type 생략 : 지가 추론함
     println("num2="+num2)
     
     var str1 : String = "대한민국, 우리나라"
     println("str1="+str1)
     var str2 = "korean"
     println("str2="+str2)
     
     // 변수 값 수정
     num1 = 100
     println("num1="+num1)
  }
}