'''
함수의 가변인수
 - 한 개의 가인수로 여러 개의 실인수를 받는 인수
 형식) def 함수명(*인수)
'''

# 1. 튜플형으로 받는 가변인수
def func1(name, *names):
    print(name)
    print(names)

func1('홍길동', '이순신', '유관순')
# 홍길동
# ('이순신', '유관순')  가변인수 자리 : 열거형으로, 튜플로 받음

# 패키지.모듈 임포트
## 방법1) import. 패키지 모듈
import scatter.scatter_module
### 실행
scatter.scatter_module import.Avg

## 방법2) 함수말고 클래스가 더 있다면 옆에 더 나열하면 됨
from scatter.scatter_module import Avg, var_std
### 실행
Avg()

datas = [2,3,5,6,7,8.5]
avg1 = scatter.scatter_module.Avg(datas)
avg2 = Avg(datas)
print(avg1)  # 5.25
print(avg2)  # 5.25

var, std = var_std(datas)
print(var)   # 5.957
print(std)

# 밖의 모듈을 갖다 쓰는 방법임
# 가능하다면 직관적으로 쓸 수 있는 방법2가 덜 번거롭지

## 함수에서 리턴은 일종의 종료구문임(exit)
def statis(func, *data):
    if func == 'sum':
        return sum(data)
    elif func == 'avg':
        return Avg(data)
    elif func == 'var':
        return var_std(data)
    elif func == 'std':
        return var_std(data)
    else:
        return '그런 거 없다'

print('sum = ', statis('sum', 1,2,3,4,5))
print('avg = ', statis('avg', 1,2,3,4,5))
var, _ = statis('var', 1,2,3,4,5)  # _ : 값은 받아도 사용하지 않겠다 표시
print('var =', var)
_, std = statis('std', 1,2,3,4,5)
print('std =', std)


# 2. dict형 가변인수
def person(w, h, **other):
    print('w=', w)
    print('h=', h)
    print(other)

person(65, 175, name = '홍길동', age = 35)
# w= 65
# h= 175
# {'name': '홍길동', 'age': 35}  : dict
## * 1개 : 튜플, 2개 : dict


# 실인수를 넘어 객체를 보내보자
# 3. 함수를 인수로 받기
def square(x):
    return x**2

def my_func(func, datas):
    result = [func(d) for d in datas]
    return result

datas = [1,2,3,4,5]
print(my_func(square, datas))  # (함수, 데이터셋)
# [1, 4, 9, 16, 25]
