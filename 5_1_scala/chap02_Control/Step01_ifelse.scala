package chap02_Control

object Step01_ifelse {
  def main(args: Array[String]): Unit = {
     
    var score = 50 // 변수 선언
    // 1. 블록없는 if문
    if(score >= 60) println("합격") else println("불합격")
    
    // 2. 어떤 변수에 if문 저장하기
    var result = if(score >= 60) "합격" else "불합격"
    println("result="+result)
    
    // 3. 블록있는 if문
    score = 75 // 변수 값 수정
    var grade = "" // 등급변수
    if(score >= 90 && score <= 100){ // &&:and
      println("A학점")
      grade = "A학점"
    }else if(score >=80){
      println("B학점")
      grade = "B학점"
    }else{
      println("F학점")
      grade = "F학점"
    }
    printf("score = %d, grade=%s\n", score, grade)
    print("프로그램 종료") //줄바꿈 없음
  }
}