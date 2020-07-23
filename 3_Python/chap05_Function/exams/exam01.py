'''
문1) Start counter 문제  

height : 3 <- 키보드 입력 
*
**
***
start 개수 : 6 
'''

# 함수 정의
def StarCount(height):

    s_cnt = 0 # 별 개수 카운트
    s_cnt = ((height+1) * (height+1-1)) / 2



    return s_cnt

# 키보드 입력
height = int(input('height : ')) # 층 수 입력

# 함수 호출 및 start 개수 출력
print('star 개수 : %d'%StarCount(height))

## 교수님 코딩
def StarCount1(height):
    s_cnt = 0  # 별 개수 카운트
    for i in range(height):
        print('*'*(i+1))
        s_cnt += (i+1)
    return s_cnt

height = int(input('height : ')) # 층 수 입력
print('star 개수 : %d'%StarCount1(height))