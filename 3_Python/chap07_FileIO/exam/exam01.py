#문제1) ftest.txt 파일을 읽어서 다음과 같이 줄 수와 단어를 카운트 하시오. 

'''
문단 내용 
['programming is fun', 'very fun!', 'have a good time', 'mouse is input device', 'keyboard is input device', 'computer']
문단 수 :  6

단어 내용 
['programming', 'is', 'fun', 'very', 'fun!', 'have', 'a', 'good', 'time', 'mouse', 'is', 'input', 'device', 'keyboard', 'is', 'input', 'device', 'computer']
단어 수 :  22
'''
import os
print(os.getcwd())
file = open("./chap07_FileIO/data/ftest.txt", mode = 'r')
print(file.read())


try:
    file = open("./chap07_FileIO/data/ftest.txt", mode='r')
    rows = file.readlines()
    sents = []
    for row in rows:
        sents.append(row.strip())
    words = []
    for row in rows:
        for word in row.split(' '):
            words.append(word.strip())
    print('문장내용')
    print(sents)
    print('문장 수 :', len(sents))
    print('단어내용')
    print(words)
    print('단어 수 :', len(words))


except Exception as e:
    print('예외발생 :', e)

finally:
    print('~~종료~~')







