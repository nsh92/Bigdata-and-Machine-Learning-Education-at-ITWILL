package chap02_Control
/*
 * 형식1)
 * for(변수 <- 컬렉션){
 * 		반복문1
 * 		반복문2
 * }
 * - 컬렉션(collection) : 열거형 data를 저장하는 자료구조(Array, List)
 * - 제너레이터 식 : (변수 <- 컬렉션)
 * 
 * 형식2)
 * for(변수 <- 컬렉션 if 조건식) 반복문
 *  - 가드(guard) : 조건에 만족하는 경우만 반복문 실행
 */
object Step02_for {
  def main(args: Array[String]): Unit = {
  // for 형식1)
    var tot = 0
    
    for(i <- 1 until 11){ // start until stop-1 : 정수컬렉션 : 1~10 : range(n)과 유사
      print(i + " ")      // 같은 라인에 출력       
      tot += i            // 누적변수
    }//for end
    println("\ntot = "+tot)
    
    // start to stop도 정수 컬렉션 생성
    tot = 0
    for(i <- 1 to 10){
      // format() 함수
      print("i = %d, tot = %d\n".format(i, tot))
      tot += i
    }//for end
    
    println("\ntot = "+tot)
    
    // List 컬렉션
    var dogList = List("진돗개-한국", "셰퍼드-독일", "불독-독일","풍산개-한국")
    // 블록 없는 for문
    for(dog <- dogList) println(dog)
    
    
    // for 형식2) 가드 포함
    println("가드 포함 경우")
    for(dog <- dogList if(dog.contains("한국"))) println(dog)
    // python : [ for 변수 in 열거형 if 조건식]
    
    // 조건식 추가
    println("조건식 추가")
    for(dog <- dogList if(dog.contains("한국")&&dog.startsWith("풍산"))) println(dog)
    
    println("조건식 수정")
    for(dog <- dogList if(dog.contains("한국")||dog.startsWith("풍산"))) println(dog)
    
    /*
     *  문) 가드문법을 적용하여 다음 결과를 출력하셈
     *  진돗개 - 한국
     *  셰퍼드 - 독일
     *  불독 - 독일
     */
    println("문제풀이ㅋ")
    for(dog <- dogList if(dog.contains("독일")||dog.startsWith("진돗개"))) println(dog)
    
    // yield(양보) 및 for를 변수에집어넣기
    // var 변수 = for(변수 <- 컬렉션 if 조건식) yield
    var dogVar = for(dog <- dogList if(dog.contains("한국"))) yield dog 
    println("dogVar ="+dogVar)
  }
}