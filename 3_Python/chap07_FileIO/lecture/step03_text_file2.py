'''
우편번호 검색
zipcode에서 맨 마지막에 위치하는 숫자 : 걍 행번호 : 무시하기로
tab키로 구분되어 있음
135-806	서울	강남구	개포1동 경남아파트		1
[우편번호]tab[도/시]tab[구]tab[동]tab[아파트]
135-807	서울	강남구	개포1동 우성3차아파트	(1∼6동)	2
[우편번호]tab[도/시]tab[구]tab[동]tab[아파트]tab[세부주소]
'''
import os
print(os.getcwd())  # C:\ITWILL\3_Python-I\workspace

try:
    file = open("./chap07_FileIO/data/zipcode.txt", encoding="utf-8")
    line = file.readline()
    print(line)               # 한 줄 전체
    print(line.split('\t'))   # 한 줄에서 토큰 단위로 쪼갤려고함

except Exception as e:
    print("예외발생 :", e)
finally:
    print("~~ 종료 ~~")
# 한 줄 단위로 확인하고 넘어감
#############################################

try:
    dong = input("동을 입력하세요 :")
    file = open("./chap07_FileIO/data/zipcode.txt", encoding="utf-8")
    line = file.readline()     # 우선 첫 줄부터 읽음

    while line:   # null
        addr = line.split(sep='\t')
        if addr[3].startswith(dong):
            print('['+addr[0]+']', addr[1], addr[2], addr[3], addr[4])
        line = file.readline()  # 두번째 ~ n번째 줄 주소 읽음

except Exception as e:
    print("예외발생 :", e)
finally:
    file.close()
    print("~~ 종료 ~~")



















