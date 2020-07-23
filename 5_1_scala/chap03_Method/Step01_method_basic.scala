package chap03_Method
/*
 * method vs function 함수인 건 마찬가지
 * method : class or object에서 선언한 함수(객체 지향 언어)
 * function : 단독으로 선언한 함수(함수 지향 언어)
 * 
 * 형식)
 * def 함수명(매개변수:타입): 리턴타입 = {
 *     실행문1
 *     실행문2
 * }
 * 
 * 반환값이 없는 경우 :리턴타입 = Unit
 */

object Step01_method_basic {
  def max(x: Int, y: Int): Int = {
    if(x>y) x else y
  }
  
  def adder(x: Float, y: Float): Float = {
    val add: Float = x+y * 0.5f
    return add
  }
  
  // 반환값이 없음
  def adder2(x: Float, y: Float): Unit = {
    val add: Float = (x+y) * 0.5f
    println("adder2 = "+add) // return을 이렇게 지정함
  }
  
  // 매개변수 없는 메소드, PI = 3.14159
  def getPI(): Double = {
    val PI = 3.14159  // 상수선언 -> default : double, 이 줄을 생략하고 return에 3.14159 써도 됨
    return PI
  }

  // return, {} 생략하기
  def getPI2(): Double = 3.14159
  
  // return, {}, () 생략하기
  def getPI3 : Double = 3.14159
  
  def main(args: Array[String]): Unit = {
    println("max method")
    val x = 20
    val y = 15
    // 함수 호출
    var max_re = max(x,y)
    println("max = "+max_re)
    var adder_re = adder(15f, 20f)
    println("add = "+adder_re)
    adder2(1.5f, 25.5f)
    println("PI = "+getPI())
    println("PI = "+getPI2())
    println("PI = "+getPI3) // ()없으니 호출도 ()없이
  }
}