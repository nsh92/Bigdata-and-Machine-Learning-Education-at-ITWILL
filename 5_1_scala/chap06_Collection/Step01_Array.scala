package chap06_Collection
/*
 * 컬렉션(collection)
 *  - 데이터의 집합 의미
 *  - 수정 여부, 순서 보장(index), 중복 허용 등으로 분류
 * 
 * Array 컬렉션 특징
 *  - 수정이 가능
 *  - 순서가 존재 : 인덱스 사용
 *  - 중복 허용
 *  - 동일한 타입만 저장 가능
 *  형식) var 변수  : Array[type] = new Arraay[type](size)
 * 
 */
object Step01_Array {
  def main(args: Array[String]): Unit = {
    // 1. new 명령어 객체 생성
    var arr : Array[Int] = new Array[Int](5)
    arr(0) = 10 // arr[index] = 값
    arr(1) = 20
    arr(2) = 30
    arr(3) = 10 // 중복 가능
    arr(4) = 50
    
    // 원소 수정
    arr(4) = 500  // 반영이 됨 : 수정이 가능하다
    
    // 다른 자료형
    // arr(4) = 500.1 // 오류뜨고 반영이 안됨 : 타입이 다르기 때문
    
    for(i <- arr) print(i + " ")
    
    println() //line skip
    
    // 2. 절차를 줄여보자 : 객체 생성과 동시에 값 초기화
    var arr2 = Array(10,20,33,40,50)
    for(i <- arr2 if(i % 2 == 0)) print(i + " ")
    
    // 3. Array 생성 축약형
    var arr3 = new Array[Double](50)
    
    // index : 0 ~ 49 -> start until stop-1
    var idx = 0 until 50
    for(i <- idx){
      var r = Math.random()
      arr3(i) = r
    }
    
    println()
    // 컬렉션 원소 출력
    println("arr3 size = " + arr3.size)
    var cnt = 0
    for(a <- arr3 if(a >=0.5 && a <= 0.8)){
      print(a + " ")
      cnt += 1
    }
    println("\n선택된 원소 : " + cnt)
  }
}