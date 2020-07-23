package chap01_Variable
/*
 * Scala 값 수정이 불가능한(상수) 변수 선언
 * 형식 ) val 변수명 : 자료형 = 값
 * 	- 초기화 이후 수정 불가능
 *  - 참조는 가능하다
 *  - 자료형 생략 추론
 */
object Step02_val {
  
  def main(args: Array[String]): Unit = {
    val numVal : Int = 100
    val numVal2 = 105.41
    println("numVal="+numVal)
    println("type="+numVal.getClass())
    println("numVal2="+numVal2)
    println("type="+numVal2.getClass())
    
    // 변수 수정 안 됨
    // numVal = 200
    
    // 참조는 가능
    var numVal_calc = numVal * 2
    println("numVal_calc="+numVal_calc)
  }
}