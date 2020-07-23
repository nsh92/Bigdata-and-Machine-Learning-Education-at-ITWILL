'''
step01_Class01 관련 문제 
 문1) Rectangle 클래스를 작성하시오.
 <처리조건>
1. 멤버변수 : 가로(width), 세로(height) 
2. 생성자 : 가로(width), 세로(height) 멤버 변수 초기화  
3. 멤버함수(area_calc) : 사각형의 넓이를 구하는 메서드 
          사각형 넓이 = 가로 * 세로 
4. 멤버함수(circum_calc) : 사각형의 둘레를 구하는 메서드
          사각형 둘레 = (가로 + 세로) * 2
  5. 기타 나머지는 출력 예시 참조         
   
       << 출력 예시 >>       
    사각형의 넓이와 둘레를 계산합니다.
    사각형의 가로 입력 : 10
    사각형의 세로 입력 : 5
    ----------------------------------------
    사각형의 넓이 : 50
    사각형의 둘레 : 30
    ----------------------------------------
'''
# class Rectangle:
    # 1. 멤버변수 : 가로(width), 세로(height)

    # 2. 생성자 : 가로(width), 세로(height) 멤버 변수 초기화
    # 구성요소로 3번 4번 : area_calc, circum_calc

class Rectangle:
    x = y = 0
    def __init__(self, w, h):
        self.x = w
        self.y = h
    def area_calc(self):
        return self.x * self.y
    def circum_calc(self):
        return (self.x + self.y) * 2


print("사각형의 넓이와 둘레를 계산합니다.")
w = int(input('사각형의 가로 입력 : '))
h = int(input('사각형의 세로 입력 : '))
Rec1 = Rectangle(w, h)
print('----------------------------------------')
print('사각형의 넓이 : ', Rec1.area_calc())
print('사각형의 둘레 : ', Rec1.circum_calc())
print('----------------------------------------')