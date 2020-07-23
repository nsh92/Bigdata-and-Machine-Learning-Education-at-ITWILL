'''
문6) 다음과 같은 조건으로 모듈을 추가하고, 결과를 확인하시오.
   모듈 위치 : package_test 패키지
   모듈명 : module02.py
   함수 정의 : 사칙연산 수행 함수 (Add, Sub, Mul, Div)
   모듈 import : 방법2) 적용
   사칙연산 함수 호출하여 결과 확인
  
    <<출력 결과 예>>
  x = 10; y = 5 일 때
  Add= 15
  Sub= 5
  Mul= 50
  Div= 2.0
'''

from package_test.module02 import Add
from package_test.module02 import Sub
from package_test.module02 import Mul
from package_test.module02 import Div

x, y = 10, 5
add = Add(x, y)
sub = Sub(x, y)
mul = Mul(x, y)
div = Div(x, y)
print("x = {}; y = {} 일 때".format(x, y))
print("Add=", add)
print("Sub=", sub)
print("Mul=", mul)
print("Div=", div)