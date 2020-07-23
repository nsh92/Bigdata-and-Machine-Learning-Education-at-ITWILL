package chap04_FileRead_except

/*
 * 예외처리 : 실행 시점 오류 처리 과정
 * try{
 * 		예외 발생 가능한 코드
 * }catch{
 * 		실제 예외를 처리하는 코드
 * }
 */

object Step01_try_catch {
  def main(args: Array[String]): Unit = {
    
    var lst = List(10, 20, 30, 40, 50)
    var size = lst.size // 원소 개수 반환
    println("size = " + size)
    println(lst(0))      // 첫번째 원소
    println(lst(size-1)) // lst(4) = 50
    
    for(i <- lst) print(i + " ") // 10 20 30 40 50 
    
    println()
    
    try{
    for(i <- 0 until 6) //print(i + " ") // 0 1 2 3 4 5 
    print(lst(i) + " ") // 10 20 30 40 50 까지만 뜨고 오류 뜸
    }catch{     // 오류에 뜨는 거 복붙
      // case 객체 : 예외클래스 => 예외처리
      case ex : IndexOutOfBoundsException => println("예외정보 : " + ex) 
    }
    
    println("프로그램 종료")
    
  }
}