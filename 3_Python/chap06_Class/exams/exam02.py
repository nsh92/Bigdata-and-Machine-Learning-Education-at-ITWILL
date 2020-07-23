'''
 문) 동적 멤버 변수 생성으로 다음과 같은 산포도를 구하는 클래스를 정의하시오.
 
class Scattering :         
        
        생성자 : 객체 + 동적 멤버 생성
        
        분산 함수(var_func)
        
        표준편차 함수(std_func) 
        
        
   << 출력 결과 >>
 분산 : 7.466666666666666
 표준편차 :  2.7325202042558927
'''

from statistics import mean
from math import sqrt


class Scattering:
    #생성자 : 객체 + 동적멤버
    def __init__(self, x):
        self.num = x  # 동적멤버 변수 생성

    # 분산 함수(var_func)
    def var_func(self):
        mu = mean(self.num)  # 평균계산
        diff = [(i - mu)**2 for i in self.num]
        # 동적 멤버변수 생성
        self.var = sum(diff) / (len(self.num) - 1)

    # 표준편차 함수(std_func)
    def std_func(self):
        # 동적 멤버변수 생성
        self.std = sqrt(self.var)

# object 생성
x = [5, 9, 1, 7, 4, 6]
scatter = Scattering(x)
scatter.var_func() # 분산 계산
print('분산 :', scatter.var)
scatter.std_func() # 표준편차 계산
print('표준편차 :', scatter.std)



