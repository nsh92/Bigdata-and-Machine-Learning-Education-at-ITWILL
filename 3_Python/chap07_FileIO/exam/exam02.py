'''
문제2) 서울 지역을 대상으로 '동' 이름만 추출하여 다음과 같이 출력하시오.
  단계1 : 'ooo동' 문자열 추출 : 예) '개포1동 경남아파트' -> '개포1동'
  단계2 : 중복되지 않은 전체 '동' 개수 출력 : list -> set -> list
  
  <출력 예시>  
서울시 전체 동 개수 =  797
'''

try:
    file = open("./chap07_FileIO/data/zipcode.txt", encoding="utf-8")
    lines = file.readline() # 첫줄 읽기 
    dong = [] # 서울시 동 저장 list
    dongs = []
    while lines:
        addr = lines.split(sep='\t')
        if addr[1] == '서울':
            dong = addr[3].split()
            dongs.append(dong[0])
        lines = file.readline()
    dong1 = list(set(dongs))

    print("서울특별시 전체 동의 개수 =", len(dong1))
    print(dong1)


except Exception as e :
    print('예외발생 :', e)
    
    
    
