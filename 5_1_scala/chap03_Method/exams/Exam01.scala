package chap03_Method.exams

/*
 * 문) 두 실수를 인수로 받아서 나눗셈 연산 후 실수값으로 반환하는  div 메서드 정의하기
 *    함수명 : div()
 */

object Exam01 {
  
  // div 메서드 정의
  def div(x:Double, y:Double): Double = {
    val diver:Double = x/y
    return diver
  }
  
  def main(args: Array[String]): Unit = {
      // div 메서드 호출 
  
   var a = div(5, 2)
   println("div = " + a)
  }
  
}


