import pandas as pd

election = pd.read_csv('C:/ITWILL/4_Python-II/data/election_2012.csv', encoding='ms949')
print(election.info())
'''
cand_id : 대선 후보자 id
cand_nm : 대선 후보자 이름
contbr_nm : 후원자 이름 
contbr_occupation : 후원자 직업군 
contb_receipt_amt : 후원금 
'''

# DF 객체 생성 
name = ['cand_nm', 'contbr_occupation', 'contb_receipt_amt'] 
# subset 생성 
election_df = pd.DataFrame(election, columns= name)
print(election_df.info())
print(election_df.head())
print(election_df.tail())


# 중복되지 않은 대선 후보자 추출 
unique_name = election_df['cand_nm'].unique()
print(len(unique_name)) 
print(unique_name) 

# 중복되지 않은 후원자 직업군 추출 
unique_occ =  election_df['contbr_occupation'].unique()
print(len(unique_occ)) 
print(unique_occ)

#############################################
#  Obama, Barack vs Romney, Mitt 후보자 분석 
#############################################

# 1. 두 후보자 관측치만 추출 : isin()
two_cand_nm=election_df[election_df.cand_nm.isin(['Obama, Barack','Romney, Mitt'])]
print(two_cand_nm.head())
print(two_cand_nm.tail())
print(len(two_cand_nm)) # 700975
'''
문1) two_cand_nm 변수를 대상으로 피벗테이블 생성하기 
    <조건1> 교차셀 칼럼 : 후원금, 열 칼럼 : 대선 후보자,
             행 칼럼 : 후원자 직업군, 적용함수 : sum
    <조건2> 피벗테이블 앞부분 5줄 확인

문2) 피벗테이블 대상 필터링 : 2백만달러 이상 후원금 대상 (행합))
'''
# 문1
two_cand_nm.info()
two_pi = pd.pivot_table(two_cand_nm, values='contb_receipt_amt',
                        index='contbr_occupation',
                        columns='cand_nm',
                        aggfunc='sum')
two_pi.head()

# 문2
two_pi_sum = two_pi[two_pi.sum(axis=1) >= 2000000]
two_pi_sum
'''
cand_nm                                 Obama, Barack  Romney, Mitt
contbr_occupation                                                  
ATTORNEY                                  11126932.97    5302578.82
CEO                                        2069784.79     353310.92
CONSULTANT                                 2459812.71    1404576.94
EXECUTIVE                                  1355161.05    2230653.79
HOMEMAKER                                  4243394.30    8037250.86
INFORMATION REQUESTED                      4849801.96           NaN
INFORMATION REQUESTED PER BEST EFFORTS            NaN   11173374.84
INVESTOR                                    884133.00    1494725.12
LAWYER                                     3159391.87       7705.20
PHYSICIAN                                  3732387.44    1332996.34
PRESIDENT                                  1878009.95    2403439.77
PROFESSOR                                  2163571.08     160362.12
RETIRED                                   25270507.23   11266949.23

'''

# 4장 넘파이 후 문제 추가 []속 논리식
# 문) 두 후보자 모두 200만 달러 이상의 후원금을 후원한 직업군을 골라랑
import numpy as np
two_pi_sum2 = two_pi[np.logical_and(two_pi['Obama, Barack']>=2000000, two_pi['Romney, Mitt']>=2000000)]
two_pi_sum2

# 두 후보자 중 한 명이 200만 달러 이상 직업군 
two_pi_sum3 = two_pi[np.logical_or(two_pi['Obama, Barack']>=2000000, two_pi['Romney, Mitt']>=2000000)]
two_pi_sum3




