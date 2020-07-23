'''
동적 멤버 변수 생성
 - 필요한 경우 특정 함수에서 멤버 변수 생성
 self : 클래스의 멤버를 호출하는 역할
 self.멤버 변수
 self.멤버 메소드()
'''
# 생성과 참조에서 모두 self가 쓰임 : 멤버들을 관리하고 호출
class Car:
    # 멤버 변수
    # door = cc = 0
    # name = None  # null

    # 생성자 : 객체 생성 + 변수 초기화
    def __init__(self, door, cc, name):
        # self.멤버변수 = 매개변수
        self.door = door  # 동적 멤버 변수
        self.cc = cc      # 동적 멤버 변수
        self.name = name  # 동적 멤버 변수

    # 멤버 메소드 : 자료 처리
    def info(self):
        self.kind = ""  # 동적 멤버 변수
        if self.cc >= 3000:  # 참조
            self.kind = "대형"
        else:
            self.kind = "소형"
        self.display()

    def display(self):
        print("%s는 %d cc이고(%s), 문짝은 %d개 이다."%(self.name, self.cc, self.kind, self.door))

# 객체 생성 : 생성자() -> object
car1 = Car(4, 2000, '소나타')
# car1.member or car1.member()
print('자동차 명 : ', car1.name)  # 자동차 명 :  소나타
car1.info()
# 소나타는 2000 cc이고(소형), 문짝은 4개 이다.

# 객체2
car2 = Car(4, 3000, '그렌저')
print('자동차 명 : ', car2.name)
car2.info()




