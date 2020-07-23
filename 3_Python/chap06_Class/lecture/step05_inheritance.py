'''
클래스 상속(Inheritance)
 - 기존 클래스(부모 클래스)를 이용하여 새로운 클래스(자식 클래스)를 생성하는 문법
 - 부모클래스 정의 -> 자식클래스 생성
 - 상속의 대상 : 멤버(상속대상) + 생성자(상속제외)
 형식) class 자식클래스(부모클래스):  # 인수를 받는 것처럼 보이나 그런 구조가 아니다  # class new_class(old_class)
             멤버 ( 변수 + 메소드 )
             생성자
 self vs super()
 - self.member : 현재 클래스의 멤버를 호출
 - super().member : 부모 클래스의 멤버를 호출
'''
# 부모 클래스 만들어놓기 : old class
class Super:
    # 멤버변수
    name = None
    age = 0
    # 생성자 : 객체 생성 + 멤버변수 초기화
    def __init__(self, name, age):   # 부모 생성자
        self.name = name
        self.age = age
    # 멤버메소드 : 데이터 처리
    def display(self):
        print("이름 : {}, 나이 : {}".format(self.name, self.age))

# 부모의 멤버는 3개 : 상속 대상

# object 생성
sup = Super('부모', 55)
sup.display()  # 이름 : 부모, 나이 : 55

# 자식클래스
class Sub(Super):
   #name = None             # 상속대상 2가지
   #age = 0
   gender = None            # 자식 멤버

   def __init__(self, name, age, gender):      # 자식 생성자
       self.name = name
       self.age = age
       self.gender = gender

   def display(self):     # 상속대상 1가지
       print("이름 : {}, 나이 : {}, 성별 : {}".format(self.name, self.age, self.gender))

sub = Sub('자식', 22, '남자')
sub.display()  # 이름 : 자식, 나이 : 22, 성별 : 남자

## 부모 생성자를 써먹을 수도 있다
class Sub(Super):
   #name = None             # 상속대상 2가지
   #age = 0
   gender = None            # 자식 멤버

   def __init__(self, name, age, gender):      # 자식 생성자
       # 2차 : 부모 생성자 호출
       Super.__init__(self, name, age)   # 부모클래스 호출
       #super().__init__(name, age)        # 이렇게도 가능 : super()호출
       #self.name = name  # 1차 : 자식 생성자 초기화
       #self.age = age
       self.gender = gender

   def display(self):     # 상속대상 1가지
       print("이름 : {}, 나이 : {}, 성별 : {}".format(self.name, self.age, self.gender))

sub = Sub('자식', 22, '남자')
sub.display()  #  이름 : 자식, 나이 : 22, 성별 : 남자
               #  멀쩡히 나온다
               #  변수를 또 설정해야 하는 것을 개선할 수 있다.

# 1. 부모클래스 정의
class Parent:
    # 멤버 변수
    name = job = None

    # 생성자
    def __init__(self, name, job):
        self.name = name
        self.job = job

    # 멤버 메소드
    def display(self):
        print("이름 : {}, 직업 : {}".format(self.name, self.job))

p = Parent('홍길동', '공무원')
p.display()  # 이름 : 홍길동, 직업 : 공무원

# 자식클래스1
class Children1(Parent):
    # name = job = None 생략
    gender = None

    def __init__(self, name, job, gender):
        #Parent.__init__(self, name, job)  # 부모생성자 호출
        super().__init__(name,job)
        self.gender = gender              # 자식멤버 초기화

    def display(self):                    # 내용 확장
        print("이름 : {}, 직업 : {}, 성별 : {}".format(self.name, self.job, self.gender))

c1 = Children1("이순신", "군인", "남자")
c1.display()  # 이름 : 이순신, 직업 : 군인, 성별 : 남자

'''
parent -> Children2
이름 : 유관순
직업 : 독립열사
성별 : 여자
'''
class Children2(Parent):
    gender = None
    def __init__(self, name, job, gender):
        Parent.__init__(self, name, job)  # 부모생성자 호출
        self.gender = gender  # 자식멤버 초기화
    def display(self):  # 내용 확장
        print("이름 : {}, 직업 : {}, 성별 : {}".format(self.name, self.job, self.gender))

c2 = Children1("유관순", "독립열사", "여자")
c2.display()










