'''
csv, excel file read / write
 - 칼럼 단위로 작성된 파일 유형

cmd에서 외부 라이브러리 설치
 pip install 패키지명
 pandas를 cmd로 깔음
 파이참은 자체 가상환경에 깔아야하므로 file/settings/project:workspace/interpreter에서
 깔고자 하는 패키지를 깔아야 함
'''
import pandas as pd  # as 별칭
import os
print(os.getcwd())

# 1. csv 읽기
spam_data = pd.read_csv("./chap07_FileIO/data/spam_data.csv", header=None, encoding='ms949')
print(spam_data.info())  # R의 STR과 유사
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 5 entries, 0 to 4   # 관측치
Data columns (total 2 columns)  # 칼럼(칼럼명 없으면 기본이름인 0, 1 숫자로)
'''
print(spam_data)  # 5행 2열

# 2. x, y 변수 선택
target = spam_data[0]  # DF[컬럼명]
texts = spam_data[1]   # DF[컬럼명]
print(target)
print(texts)
# 행번호와 함께 출력됨  # 저래보여도 벡터임

# 3. target -> dummy
target = [1 if x == 'spam' else 0 for x in target]
print(target)  # [0, 1, 0, 1, 0]  아마 모델의 y변수가 되겠지

# 4. text 전처리
def clean_text(texts):
    from re import sub  # gsub() 유사함
    # 2. 숫자 제거
    texts_re2 = sub('[0-9]', '', texts)
    texts_re3 = sub('[a-z]', '', texts_re2)
    # 3. 문장 부호 제거
    punc_str = '[,.<>/?;:!@#$%^&*()]'
    text_re4 = sub(punc_str, '', texts_re3)
    # 4. 공백 제거
    text_re5 = ' '.join(text_re4.split())
    return text_re5

clean_texts = [clean_text(text) for text in texts]
print('텍스트 전처리 후')
print(clean_texts)

###########################################
### bmi.csv
###########################################
bmi = pd.read_csv("./chap07_FileIO/data/bmi.csv", encoding='utf-8')
print(bmi.info())
print(bmi.head())  # 앞 5개 R과 유사하내
print(bmi.tail())  # 뒤 5개

# 벡터화 방법은 인덱스, .칼럼 두 가지가 있내
height = bmi['height']  # DF['칼럼명']
weight = bmi['weight']
label = bmi.label       # DF.칼럼명  # 얘는 문자타입
print(len(height))
print(len(weight))
print(len(label))
# 멀쩡하다면 2만개를 가져왔겠지

print('키 평균 :', height.mean())
print('몸무게 평균 :', weight.mean())
#  키 평균 : 164.9379
#  몸무게 평균 : 62.40995

# max() / min() 얘내도 바로 적용 가능하다
max_h = max(height)
max_w = max(weight)
print('길쭉이 :', max_h)
print('뚱뚱이 :', max_w)
#  길쭉이 : 190
#  뚱뚱이 : 85
height_nor = height / max_h  # 이런식으로 정규화가 가능하지  # 픽셀 정규화도 이런식으로 함
weight_nor = weight / max_w
print(height_nor.mean())  # 0.8680942105263159
print(weight_nor.mean())  # 0.734234705882353


# 범주형 변수 : label
lab_cnt = label.value_counts()  # 범주형에 대한 빈도수  R의 table()과 유사하지
print(lab_cnt)
'''
normal    7677
fat       7425
thin      4898
'''

# 2. 엑셀 읽기
'''
pip install xlrd : 엑셀리드
'''
import xlrd

excel = pd.ExcelFile("./chap07_FileIO/data/sam_kospi.xlsx")
print(excel)
kospi = excel.parse('sam_kospi')  # 파씽하다의 파스임 : 읽어올 하단의 시트탭을 정함
print(kospi)
print(kospi.info())
### 지금까지는 read만 해봤지

# 3. csv file save
# 저 엑셀에 들어갈 파생변수를 만들겠다
kospi['Diff'] = kospi.High - kospi.Low
print(kospi.info())  # 내가 의도한 Diff 축이 추가됨

# csv file 저장
kospi.to_csv("./chap07_FileIO/data/kospi_df.csv", index=None, encoding='utf-8')
# 행번호는 저장안한다
# 원래 엑셀이었는데 csv로 저장했지

kospi_df = pd.read_csv("./chap07_FileIO/data/kospi_df.csv", encoding='utf-8')
print(kospi_df.info())
print(kospi_df.head())

