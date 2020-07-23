'''
변수(Variable)
 - 형식) 변수명 = 값 or 수식 or 변수명
 - 자료를 저장하는 메모리 이름
 - type 선언이 없음(R과 동일)
'''

# 1.  변수와 자료
var1 = "Hello python"
var2 = 'Hello python' # '나 "나 다 스트링취급함
print'(var1) # Line skip
print(var2)
print(type(var1)) # 자료형 반환
print(type(var1), type(var2)) # 같은 문장에 두 자료를 보여줌

var1 = 100
print(var1, type(var1)) # 100 <class 'int'>

var3 = 150.25
print(var3, type(var3)) # float 실수

var4 = True
print(var4, type(var4)) # 'bool' : 부울리언 자료형

# 2. 변수명 작성 규칙 # 강의자료 11p 참고
_num10 = 10
_NUM10 = 20
print(_num10, _NUM10)
print(id(_num10), id(_NUM10))
# 점은 사용하지 못한다, 특수문자는 언더바 사용가능하다, 대소문자 구분한다 : 증거 : 아이디가 다르다

# 키워드 확인
import keyword # 모듈을 임포트한다 # R의 라이브러리 유사
py_keword = keyword.kwlist
print("파이썬 키워드 : ", py_keword) # 약속된 키워드가 주루룩
print("len =", len(py_keword)) # 35 : 약속된 키워드의 수 : 얘내들은 변수명으로 못 씀

# 낙타체
korScore = 90 # 변수 = 상수
matScore = 85
engScore = 75
tot = korScore + matScore + engScore # 변수 = 수식
print("tot =", tot)


# 3. 참조변수 : 메모리 객체(value)를 참조하는 주소를 저장하는 변수
x = 150 # 150이 아닌, 150이라는 객체의 주소를 x가 가짐
y = 45.23
y2 = y # 변수 복제 ( : 실질적으로 복제되는 건 주소다)
x2 = 150
print(x,y,y2,x2)                        # 변수의 내용 출력
print(id(x), id(y), id(y2), id(x2))     # 변수의 주소 출력
# 유니크한 주소는 2개 뿐
# y는 복제를 했으니 저러고, x를 보아하니 기존에 있는 똑같은 객체를 만들면
# 효율성을 위하여 추가적으로 메모리를 만들어내지 않는다는 것을





