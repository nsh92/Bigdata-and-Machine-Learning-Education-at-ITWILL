'''
문4) 다음 texts 객체를 대상으로 단계별로 텍스트를 전처리하시오. 


 <텍스트 전처리 후 결과> 
['우리나라 대한민국 우리나라 만세', '비아그라 정력 최고', '나는 대한민국 사람', '보험료 원에 평생 보장 마감 임박', '나는 홍길동']
'''

# 전처리 전 텍스트
texts = [' 우리나라    대한민국, 우리나라%$ 만세', '비아그&라 500GRAM 정력 최고!', '나는 대한민국 사람', '보험료 15000원에 평생 보장 마감 임박', '나는 홍길동']


from re import sub

print('전처리 전 : ', texts)

# 1. 영문자 제거
text1 = [sub('[A-Z]', '', text) for text in texts]
print(text1)

# 2. 숫자 제거 
text2 = [sub('[0-9]', '', text) for text in text1]
print(text2)

# 3. 문장부호 제거 
booho = '[<>?,.;:\!@#$%^&*()]'
text3 = [sub(booho, '', text) for text in text2]
print(text3)

# 6. 공백 제거(2칸 이상 공백 -> 1칸 공백)

text4 = [' '.join(text.split()) for text in text3]
print(text4)