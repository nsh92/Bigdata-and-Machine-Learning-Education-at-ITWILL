package chap06_Collection

/*
 * 1. List 컬렉션 특징
 *  - 수정 불가(값 초기화)
 *  - 순서 존재(index)
 *  - 중복 허용
 *  - 동일 자료형 저장
 *  형식) val 변수 = List(값1, 값2, ....)
 * 
 * 2. Tuple 컬렉션
 *  - Tuple 클래스는 없음 (기호를 이용함)
 *  - 수정 불가(값 초기화)
 *  - 순서는 존재(index)
 *  - 다른 자료형 저장 가능
 *  형식) val 변수 = (값1, 값2, ...)
 * 
 * 3. Set 컬렉션
 *  - (일반적으로)수정 불가 or 수정 가능(import요구)
 *  - 중복 불가, 순서 없음
 *  형식) val 변수 = Set(값1, 값2, ...)
 */
// 수정가능한 셋 임포트
import scala.collection.mutable // 수정 가능한 컬렉션 객체

object Step02_List__Tuple_Set {
  def main(args: Array[String]): Unit = {
    // 1. List 컬렉션
    val num = List(1,2,3,4,5,1,2,3,7)
    println("num size = " + num.size)
    println(num) // List(1, 2, 3, 4, 5, 1, 2, 3, 7)
    println(num.mkString(",")) // 1,2,3,4,5,1,2,3,7 : 원소만 출력 및 ,로 구분
    println(num(0)) // 인덱스 출력
    
    // 원소 수정
    // num(num.size = 1) = 70 // 오류 발생 : 수정이 불가능하기 때문
    
    val num2 = List.range(1, 11)
    for(n <- num2) print(n+" ")
    
    // 2. Tuple 컬렉션
    val names = ("홍길동", 35, "이순신", 45, "유관순", 25)
    println(names)     // (홍길동,35,이순신,45,유관순,25)
    println(names._1)  // 홍길동
    println(names._2)  // 35
    
    // 제너레이터 식으로 사용 불가
    // for(name <- names) print(name)
    
    // 3. Set 컬렉션
    val num3 = Set(1,2,3,4,5,1,2,3)
    println("num3 size = " + num3.size) // 5 : 중복 ㄴㄴ하기때문
    println(num3) // Set(5, 1, 2, 3, 4)
    
    // 문장 -> 단어 추출
    val texts = "kim hong! kim, park, hong"
    val wordArr = texts.split("[ !,.]+") // 얘내들을 구분자로 스플릿한다(공백도있음), + : 1번이상 반복할때 표시
    println("word : " + wordArr) // [Ljava.lang.String;@506e1b77 이딴식으로 떠서 추가적인 절차가 필요
    for(word <- wordArr) println(word)
    
    // 수정 가능한 set 컬렉션 생성
    val words = mutable.Set.empty[String] // String 원소를 갖는 Set 객체 생성
    for(word <- wordArr){
      words += word // 적재시킴
    }
    
    println(words) // Set(hong, park, kim)
    
  }
}