# -*- coding: utf-8 -*-
"""
konlpy : 한글 형태소 분석을 제공하는 패키지
pip install konlpy
"""
import konlpy
from konlpy.tag import Kkma # class
kkma = Kkma() # 생성자 -> 객체 생성

# 문단 -> 문장
para = "나는 홍길동입니다. 나이는 23세 입니다. 대한민국 만세 입니다."
ex_sent = kkma.sentences(para)
ex_sent
# ['나는 홍길동입니다.', '나이는 23세 입니다.', '대한민국 만세 입니다.']
len(ex_sent) # 3

# 문장 -> 단어(명사)
ex_nouns = kkma.nouns(para)
ex_nouns
# ['나', '홍길동', '나이', '23', '23세', '세', '대한', '대한민국', '민국', '만세']
# data의 형태소txt 참고

# 문단 -> 품사(형태소)
ex_pos = kkma.pos(para)
ex_pos # [(형태소, 품사), ...]
type(ex_pos) # list

# 내가 필요한 품사만 쓸래
nouns = []
for word, wclass in ex_pos:
    if wclass == 'NNG' or wclass == 'NNP' or wclass == 'NP':
        nouns.append(word)
nouns # ['나', '홍길동', '나이', '대한민국', '만세']

























