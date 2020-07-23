package chap06_Collection

/*
 * Map 컬렉션 특징
 *  - 파이썬 dict 유사
 *  - (key -> value)
 *  - 수정 불가능 / 근대 뭘 임포트해서 수정 가능하긴함
 *  - 순서 없음
 *  - 키를 통해 value 접근
 *  형식) Map(key -> value, key -> value, ...)
 */

import scala.collection.mutable // 수정 가능 map 컬렉션 및 wc함수 생성

object Step03_Map {
  
  def wc(texts : String) : Unit = {
    var word_count = mutable.Map.empty[String, Int] // [key타입, value타입]
    // 받은 문자를 쪼개기
    var words = texts.split("[ ,!]+")
    println(words) // [Ljava.lang.String;@7cc355be : 라는 객체가 있다는 의미
    println(words.mkString(" ,"))
    
    for(wd <- words){
        var word = wd.toLowerCase() // 소문자변경
        var word_value
        = if(word_count.contains(word)){ // 기존에 있는 word면 word에 집어넣어라
          word_count(word) // key -> value
          }else{
            0 // 최초 출현 word
          } // if 및 else의 실행문이 하나뿐이니 {} 생략 가능
        word_count += (word -> (word_value + 1)) // 수정 가능한 map에 저장시키는 것
    }//for end
    println(word_count)
  }//func end
  
  def main(args: Array[String]): Unit = {
    // 1. 수정 불가
    val map_list = Map("one" -> 1, "two" -> 2)
    println(map_list)
    println(map_list.size)
    println(map_list("two")) // key로 value 호출
    
    // Map("key" -> (값1, 값2, 값3)) 가능
    val emp = Map(1001 -> ("홍길동", 250, 50), 1002 -> ("이순신", 350, 100), 1003 -> ("유관순", 200, 40))
    println(emp)
    println(emp(1001))
    
    for(e <- emp.keys){
      println(e)       // key 출력
      println(emp(e))  // 각 value 출력
    }
    
    // 2. 수정 가능
    val texts = "Kim, Hong! kim, Hong, You"
    // 함수호출
    wc(texts)
    
  }
}
