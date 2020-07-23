'''
중첩함수 -> 클래스
'''

class Account:  # outer -> class
    # balance = 0  # 잔액(balance) : outer변수 -> 멤버 변수

    # 생성자
    def __init__(self, bal):
        self.balance = bal  # 멤버 변수 초기화 : 위 밸런스 => 0 필요없음

    # inner -> 멤버 메소드 : 인수 자리에 self
    def getBalance(self):  # 잔액확인(getter)
        return self.balance

    def deposit(self, money):  # 입금하기(setter)
        if money < 0:
            print("금액을 확인하세요")
        else:
            # nonlocal balance
            self.balance += money

    def withdraw(self, money):  # 출금하기(setter)
        # nonlocal balance
        if self.balance < money:
            print("잔액이 부족합니다.")
        else:
            self.balance -= money

acc = Account(1000)
print('잔액 = ', acc.getBalance())
acc.deposit(20000)
print('잔액 = ', acc.getBalance())
acc.withdraw(5000)
print('잔액 = ', acc.getBalance())

'''
1. 예금주(accName), 계좌번호(accNo) 동적 멤버 변수 추가하기
   -> 예금주 : 홍길동, 계좌번호 : 012-125-41520
2. getBalance() 메소드를 이용하여 잔액, 예금주, 계좌번호 출력
'''

class Account:
    def __init__(self, bal, name, no):
        self.balance = bal
        self.accName = name
        self.accNo = no

    def getBalance(self):
        return self.balance, self.accName, self.accNo

    def deposit(self, money):
        if money < 0:
            print("금액을 확인하세요")
        else:
            self.balance += money

    def withdraw(self, money):
        if self.balance < money:
            print("잔액이 부족합니다.")
        else:
            self.balance -= money


acc = Account(1000, "홍길동", "012-125-41520")
bal, name, No = acc.getBalance()
print('잔액 = {}, 예금주 = {}, 계좌번호 = {}'.format(bal, name, No))



