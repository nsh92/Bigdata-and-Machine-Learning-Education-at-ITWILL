'''
기본(default) 생성자
 - 생성자를 생략하면 기본 생성자가 만들어진다.
 - 묵시적 생성자
 - 객체만 생성하는 역할 : 다른 역할은 딱히 없다
'''

class default_cost:
    # 생성자 생략 : def __init__(self):
    def data(self, x, y):
        self.x = x
        self.y = y
    def mul(self):
        re = self.x * self.y
        return re


obj = default_cost()  # 인수가 없음 : 기본생성자를 사용하였기 때문
obj.data(10, 20)  # data 생성
print('mul = ', obj.mul())  # 연산 : mul = 200
# 멀쩡히 작동됨
# def __init__(self): 얘는 명시적이든 묵시적이든 항상 작동하는 기본 생성자임


# Tv class 정의
class TV:                    # class = 변수(명사, 자료) + 메소드(동사, 기능)
    # 멤버 변수 : 자료 저장
    channel = volume = 0
    power = False            # 전원 꺼져있음으로 초기화상태
    color = None

    # 기본 생성자 def __init__(self):

    # 멤버 메소드
    def volumeUp(self):
        self.volume += 1
    def volumeDown(self):
        self.volume -= 1
    def channelUp(self):
        self.channel += 1
    def channelDown(self):
        self.channel -= 1
    def changePower(self):
        self.power = not(self.power)  # 반전(T <-> F)

    # 멤버 변수 초기화 메소드
    def data(self, channel, volumn, color):
        self.channel = channel
        self.volume = volumn
        self.color = color
    # 이 덩어리를 기본 생성자 자리에 넣으면 객체 + 초기화 메소드 기능함
    # 함수 이름 대신 init으로 바꾸면 됨
    # 이리되면 data()로 뭘 넣을 필요가 없고 바로 TV()에 값을 넣으면 되지

    # TV 정보 출력 메소드
    def display(self):
        print("전원 : {}, 채널 : {}, 볼륨 : {}, 색상 : {}".format(self.power, self.channel, self.volume, self.color))

# 객체 생성
tv1 = TV()  # 기본 생성자 -> 객체
tv1.display()
# 전원 : False, 채널 : 0, 볼륨 : 0, 색상 : None
# 그 어떤 값도 넣지 않은 초기값 상태가 출력됐음

tv1.data(5, 10, '검정색')  # 멤버 변수 값 수정함
tv1.display()
# 전원 : False, 채널 : 5, 볼륨 : 10, 색상 : 검정색
# 초기값 세팅

tv1.changePower()  # 전원 off -> on
tv1.channelUp()    # 채널 5번 -> 6번
tv1.volumeUp()     # 소리 10 -> 11
tv1.display()
# 전원 : True, 채널 : 6, 볼륨 : 11, 색상 : 검정색

'''
문) tv2 객체를 다음과 같이 생성하셈
단계 1. 전원 : false, 채널 1, 볼륨 :1, 색상 : 파랑색
단계 2. 전원 : true, 채널 10, 볼륨 15
단계 3. tv2 객체 정보 출력
'''

tv2 = TV()
tv2.display()
tv2.data(1, 1, '파랑색')
tv2.changePower()
for i in range(9):
    tv2.channelUp()
for i in range(14):
    tv2.volumeUp()
tv2.display()














