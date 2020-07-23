# 텍스트 전처리
texts = ['AFAB54747,asabag?', 'abTTa $$;a12:2424.', 'uysfsfA,A124&***$?']
print(len(texts), type(texts)) # 3 <class 'list'>

from re import sub # gsub() 유사함
# from package.module import class or function
# from module import class or function

# 1. 소문자 변경
print('소문자 변경')
# texts 자체는 리스트이지 스트링이 아니다. 스트링은 그 안의 개별 원소들이다
for text in texts:
    print(text.lower())
# 혹은
texts_re = [text.lower() for text in texts]
print('texts_re1', texts_re)

# 2. 숫자 제거
text_re2 = [sub('[0-9]', '', text)  for text in texts_re]
print('text_re2 :', text_re2)
# 영어를 지우고 싶으면 [a-z]로

# 3. 문장 부호 제거
# [0-9]와 같이 인공적으로 패턴을 만들자
punc_str = '[.,;:?!$*&]'
text_re3 = [sub(punc_str, '', text) for text in text_re2]
print('text_re3 :', text_re3)

# 4. 특수 문자 제거
# 3번에서 다 함, 똑같음

# 5. 공백 제거 : 'abtta a' -> split을 쓰면 'abtta', 'a' -> 그래서 ''.join('abtta', 'a')
text_re5 = [''.join(text.split()) for text in text_re3]
print('text_re5 :', text_re5)

