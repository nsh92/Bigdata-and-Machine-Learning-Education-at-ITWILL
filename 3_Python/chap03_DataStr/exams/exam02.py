'''
step02 문제

문1) message에서 'spam' 원소는 1 'ham' 원소는 0으로 dummy 변수를 생성하시오.

      
  <출력결과>      
[1, 0, 1, 0, 1]   


문2) message에서 'spam' 원소만 추출하여 spam_list에 추가하시오. (얘가 더 쉬움)

      
  <출력결과>      
['spam', 'spam', 'spam']   

'''

message = ['spam', 'ham', 'spam', 'ham', 'spam']

#문1)
dummy = [1 if i == 'spam' else 0 for i in message]
print(dummy)

#문2)
spam_list = [i for i in message if i == 'spam']
print(spam_list)