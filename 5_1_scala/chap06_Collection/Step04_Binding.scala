package chap06_Collection
/*
 * 바인딩 메소드(Bingding method)
 *  - 컬렉션 객체에서 호출 가능한 함수
 *  형식) object.method1().method2()
 *  - 처리 : 원소를 순차적으로 method1 넘기고 -> 처리 -> method2(처리) 넘김
 *  - 자체 제너레이터(반복) 기능 포함
 */
object Step04_Binding {
  def main(args: Array[String]): Unit = {
    // 1. 컬렉션 객체 생성
    // var nums = 1 to 20 // 숫자 컬렉션 생성
    // println(nums.size)
    
    val nums = List(1,2,3,4,5,1,2,3,7)  // List 컬렉션 넣어보기
    
    // 2. 바인딩 메소드 생성
    // 1) 객체.foreach(func) : 객체 원소를 순차적으로 받고, func 자료 처리
    println("foreach 두둥")
    nums.foreach((x : Int) => print(x + " ")) // 무명함수 : (x) => x+1
    
    // 2) 객체.map(_매핑연산자) : 객체 원소를 순차적으로 받고(_), 연산 수행
    println("map 두둥")
    var map_re = nums.map(_*2)
    println(map_re)
    
    // 3) 객체.filter(_조건식) : 객체 원소를 순차적으로 받고(_), 조건에 따라 필터링
    var filter_re = nums.filter(_ % 2 == 0)
    println(filter_re)
    
    // 4) 객체.filter().map
    var filter_map_re = nums.filter(_ > 10).map(_ + 0.5)
    println(filter_map_re)
    
  }
}