'''
문2) weatherAUS.csv 데이터셋을 이용하여 다음 단계를 해결하시오.
   <단계1> 지역(Location)별 빈도수 구하기
     사용 함수 : value_counts()
     
   <단계2> 2개 칼럼(Location과  RainToday) -> DF 전체 칼럼 그룹화
     사용 함수 : groupby()
   <단계3> 그룹화 객체를 대상으로 평균 구하기   
                                  MinTemp    MaxTemp  ...    Temp3pm    RISK_MM
    Location      RainToday                        ...                      
    Adelaide      No         13.340847  24.313011  ...  22.917576   0.927778
                  Yes        11.426263  17.780402  ...  16.484422   3.426667
    Albany        No         13.433688  21.001590  ...  19.294128   1.488339
                  Yes        11.560593  17.345763  ...  15.878723   4.282627
                  
   <단계4> 그룹화 결과를 대상으로 테이블 형식으로 변경 
     사용 함수 : size().unstack()
    <<출력 결과>>
     RainToday          No  Yes
     Location                  
     Adelaide          661  199
     Albany            566  236
     Albury            615  169
     AliceSprings      693   99
     BadgerysCreek     596  158
     Ballarat          586  223
     Bendigo           658  153 
          : 
   <단계5> 단계4의 결과를 대상으로 가로막대 누적형 차트 그리기
'''
import pandas as pd
import matplotlib.pyplot as plt
weather = pd.read_csv('C:/ITWILL/4_Python-II/data/weatherAUS.csv')
weather.info()
weather['Location'].unique()

loca = pd.value_counts(weather['Location'])

wea_grp = weather.groupby(['Location', 'RainToday'])

wea_grp_mean = wea_grp.mean()

wea_size = wea_grp.size().unstack()

wea_size.plot(kind='barh',
              title='날씨 빈도수',
              stacked=True)
plt.show()
