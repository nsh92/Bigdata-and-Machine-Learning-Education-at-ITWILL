'''
패키지(package) = 폴더 유사함
 - 유사한 모듈 파일을 저장하는 공간
모듈(module) = 파일 유사함
 - 파이썬 파일(*.py)
클래스, 함수
 - 모듈에 포함되는 단위
'''
# 먼저 파이썬패키지 따로 열어서 모듈 하나 만들어놓음
# from 패키지명.모듈명 import 클래스 or 함수
# 끌어다 쓸 파이썬패키지는 최상위 폴더에 넣는 게 편함

from package_test.module01 import Sub
from package_test.module01 import Adder

sub = Sub(10, 20)
print('sub = ', sub.calc())

print('add = ', Adder(10, 30))




