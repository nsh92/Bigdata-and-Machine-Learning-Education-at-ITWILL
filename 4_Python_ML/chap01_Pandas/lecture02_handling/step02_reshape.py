# -*- coding: utf-8 -*-
"""
DataFrame 모양 변경
"""
import pandas as pd
buy = pd.read_csv('C:/ITWILL/4_Python-II/data/buy_data.csv')
buy.info()
type(buy) # pandas.core.frame.DataFrame 2차원이다
buy.shape # (22, 3) : 2차원
buy

# 1. row -> column (wide -> long)
buy_long = buy.stack()
buy_long.shape # (66,) : 1차원
buy_long

# 2. column -> row(long -> wide)
buy_wide = buy_long.unstack()
buy_wide.shape # (22, 3) : 원래대로
buy_wide

# 3. 전치행렬 : t(), -> .T
wide_t = buy_wide.T 
wide_t.shape        # (3, 22) 행 열이 뒤바뀜

# 4. 중복 행 제거
buy_df = buy.drop_duplicates()
buy_df.shape        # (20, 3) 2개의 행이 지워



