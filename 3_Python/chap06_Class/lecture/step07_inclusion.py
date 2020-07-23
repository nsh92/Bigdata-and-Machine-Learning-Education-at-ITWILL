'''
1. private 변수 = 클래스 내의 은닉변수
   - object.member : 이렇게 접근이 안되게끔 하는 변수임, 접근 차단함
   - getter() / setter() -> 이를 통해야 접근 가능하도록 함

2. class 포함관계(inclusion)
   - 특정 객체가 다른 객체를 포함하는 클래스 설계 기법
   - 두 객체 간의 통신 지원
   - ex) class A(a) -> class B(b)  : 통신
'''

# 1. private 변수
class Login:   # uid(유저아이디), pwd -> db['hong', '1234'] 저장
    # 생성자
    def __init__(self, uid, pwd):
        self.__dbId = uid
        # self.__private    # uid는 은닉변수다
        self.__dbPwd = pwd

    # getter() : 획득자, 인수가 없음 : 받기만 하기 때문, 하지만 리턴이 있지
    def getIdPwd(self):
        return self.__dbId,  self.__dbPwd

    # setter() : 지정자, 넣을 인수가 있어야 지정을 하지
    def setIdPwd(self, uid, pwd):
        self.__dbId = uid
        self.__dbPwd = pwd


# object
login = Login('hong', '1234')
# object.member
print(login.__dbId)
# 멤버이긴하나, 이렇게 접근이 안되도록하였으니 에러가 뜸

# object.getter()
uid, pwd = login.getIdPwd()
print(uid, pwd, sep = ', ')

# object.setter(인수) : 수정이 필요해졌다
login.setIdPwd('lee', '2345')  # 수정함
uid, pwd = login.getIdPwd()    # 확인함
print(uid, pwd, sep = ', ')

# Server <-> Login
class Server:
    # 기본 생성자

    # 멤버 메소드
    def send(self, obj):  # object 인수로 받음
        self.obj = obj    # 멤버변수 생성

    # 인증 메소드
    def cert(self, uid, upwd):  # 사용자(id/pwd)  # 서버 핵심 코딩 한 줄
        dbId, dbPwd = self.obj.getIdPwd()  # getter 호출해가지고 값을 받음
        if dbId == uid and dbPwd == upwd:  # 입력된 것이 맞는지 인증함
            print('로그인 성공~~')
        else:
            print('로그인 실패')

server = Server()
server.send(login)
server.cert('hong', '1234')
server.cert('lee', '2345')
# login클래스와 서버클래스는 상하관계가 아니라 서로 동등한 통신하는 관계임
# 따로 저장해둔 객체가 아닌 클래스 안의 객체로도 호출 가능하다










