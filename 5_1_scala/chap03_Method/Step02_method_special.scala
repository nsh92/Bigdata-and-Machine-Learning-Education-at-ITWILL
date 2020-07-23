package chap03_Method
/*
 * 1. 익명 함수 : 함수에 이름이 없음
 * 		- python의 람다와 유사
 * 		- 한 줄 함수(not 블록)
 * 		- 형식) (인수:타입, 인수:타입, ..) => 리턴값
 * 		ex) (x,y) => x+y
 * 
 * 2. 컬렉션 인수 사용
 * 		- 함수에서 컬렉션을 인수로 받는 함수
 * 		- 컬렉션 : 여러개의 원소를 저장하는 배열 자료구조
 * 		- Array[type], List 클래스에 객체
 */

object Step02_method_special {

  // 1. 익명함수 정의
  var any_func = (x : Int) => x * x // 넣은 x에 대하여 제곱하는 함수를 변수에다 정의함
  println("any func = " + any_func(10)) // 생성한 변수 호출
  
  // 정의 & 호출 동시에
  ((x : Int) => println(x * x))(10)
  ((x : Int, y:Int) => println(x * y))(10, 20)
  
  // 익명함수 -> 일반함수
  def any_func2(x : Int, y : Int) : Int = {
    return x*y
  }
  println("any func = " + any_func2(10,20))
  
  // 일반함수 -> 익명함수 + 함수 축소기법
  val any_func3 : (Int, Int) => Int = _*_
  println("any func = " + any_func3(10,20))
  
  /*
   * 매핑된 아규먼트 : _
   *  - 인수에 의해서 넘겨받은 실제값(아규먼트)을 받는 역할
   *  - 매개변수(인수) vs 아규먼트(인수의 값)
   */
  
  // 2. 컬렉션 인수 함수 정의
  def textPro(texts : Array[String]) : Unit = {
    println("texts size = " + texts.size)
    for(txt <- texts if(txt.contains("한국"))) println(txt)
  }
  
  def main(args: Array[String]): Unit = {
    // 2. 컬렉션 인수 사용
    var txtAry = Array("홍길동-한국", "존-미국", "강감찬-한국", "마이클-호주")
    textPro(txtAry)
 }
}