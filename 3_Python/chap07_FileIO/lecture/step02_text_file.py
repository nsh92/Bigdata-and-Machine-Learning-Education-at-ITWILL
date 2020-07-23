'''
텍스트 파일 입출력
형식)
    open(file, mode = 'r'읽기전용(기본값), 'w'쓰기용, 'a'추가용)
'''


import os  # 파일 경로 모듈
print('현재 경로 : ', os.getcwd())  # 현재 경로 :  C:\ITWILL\3_Python-I\workspace
# 경로 설정에서 /랑 \\ 혼용 가능
try:
    # 파일 열기 : 절대 경로
    file = open(os.getcwd() + '/chap07_FileIO/data/ftest.txt')
    print(file.read())  # 파일 사용
    file.close()        # 파일 종료 근대 일반적으로 얘는 finally에 감
except FileNotFoundError as e:
    print('예외 정보 : ', e)
finally:
    pass


try:
    # 파일 열기 : 상대 경로, 앞에 쩜('현재 디렉토리'표시)이 포인트
    # .. 쩜쩜 : 상위 디렉토리 표시
    file = open('./chap07_FileIO/data/ftest.txt')
    print(file.read())
    file.close()
except FileNotFoundError as e:
    print('예외 정보 : ', e)
finally:
    pass


# 2. 파일 쓰기
try:
    file2 = open('./chap07_FileIO/data/ftest2.txt', mode='w')
    file2.write("my first text~~")
    file2.close()
except FileNotFoundError as e:
    print('예외 정보 : ', e)
finally:
    pass

## 파일 쓰기에서 내용 추가
try:
    file3 = open('./chap07_FileIO/data/ftest2.txt', mode='a')
    file3.write("\nmy second text~~")
    file3.close()
except FileNotFoundError as e:
    print('예외 정보 : ', e)
finally:
    pass

'''
file.read() : 전체 문서 한 번에 읽기(통체로 읽음)
file.readline() : 전체 문서에서 한 줄만 읽기
file.readlines() : 전체 문서를 줄 단위로 읽기
'''

# 4. readline()
try:
    file4 = open('./chap07_FileIO/data/ftest2.txt')
    row = file4.readline()
    print('row : ', row)
    file4.close()
except FileNotFoundError as e:
    print('예외 정보 : ', e)
finally:
    pass

# 5. readlines() : 전체 문장을 줄단위 읽기
try:
    file5 = open('./chap07_FileIO/data/ftest2.txt')
    rows = file5.readlines()
    print('rows : ', rows)    # rows :  ['my first text~~\n', 'my second text~~'] 모든 문장을 줄단위 원소의 리스트로 반환함
    file5.close()

    for row in rows:
        for sent in row.split('\n'):
            if sent:
                print(sent)
    # string.strip() : 문장 '끝' 불용어(공백 \n \t 기타) 제거
    print('strip 함수')
    for row in rows:
        print(row.strip())  # 같은 효과임 : 이중 포문보다 이게 나을 수 있다

    str_text = "agsgs234\n \t\r"
    print('str_text :', str_text.strip())

except FileNotFoundError as e:
    print('예외 정보 : ', e)
finally:
    pass


try:
    print('리드라인')
    file5 = open('./chap07_FileIO/data/ftest2.txt')
    for i in range(4):
        row = file5.readline()
        print('row :' + str(i+1), row.strip())
    file5.close()
except FileNotFoundError as e:
    print('예외 정보 : ', e)
finally:
    pass



## with블록이 더 편할 수 있다
try:
    with open("./chap07_FileIO/data/ftext3.txt", mode='w', encoding="utf-8") as file6:
        file6.write("파이썬 파일 작성 연습")
        file6.write("\n파이썬 파일 작성 연습2")
        # 파일 종료 지정을 할 필요가 없음

    with open("./chap07_FileIO/data/ftext3.txt", mode='r', encoding="utf-8") as file7:
        print(file7.read())

except FileNotFoundError as e:
    print('예외 정보 : ', e)
finally:
    print("~~종료~~")











