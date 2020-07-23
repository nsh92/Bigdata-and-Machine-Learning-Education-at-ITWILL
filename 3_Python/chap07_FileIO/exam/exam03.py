'''
문) emp.csv 파일을 읽어와서 다음 출력 예시와 같이 처리하시오. 
 
       <<출력 예시>>
관측치 길이 :  5
전체 평균 급여 : 370.0
==============================
최저 급여 : 150, 이름 : 홍길동
최고 급여 : 500, 이름 : 강감찬
==============================
'''
import pandas as pd
import statistics as mean
# 1. file read
emp = pd.read_csv('./chap07_FileIO/data/emp.csv', encoding='utf-8')
print(emp.info())

print('관측치 길이 :', len(emp))
pay = emp.Pay
name = emp.Name
print('전체 사원 평균 급여 :', pay.mean())
min_pay = pay.min()
max_pay = pay.max()
print('==============================')
for i, p in enumerate(pay):  # index, data 따로 따로 값을 리턴 받을 수 있다
    if p == min_pay:
        print(f"최저 급여 : {p}, 이름 : {name[i]}")
    if p == max_pay:
        print(f"최고 급여 : {p}, 이름 : {name[i]}")
print('==============================')

# np 모듈 기억하기