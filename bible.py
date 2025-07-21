#파일에 성경 구절 저장 후 리스트로 한 줄씩 옮기기 / 랜덤으로 출력
#캔버스 띄우고 버튼 생성

import tkinter
import random

#성경 구절 입력하고 파일 저장
def bibleWrite():
    outFile = open('sentence.txt', 'w')
    while True:
        outStr = input('성경 구절 추가 : ')
        if outStr != '':
            outFile.write(outStr+'\n')
            print('-----중간 저장 완료-----')
        else:
            print('-----최종 저장 완료-----')
            break            
    outFile.close()

#랜덤 출력
def bibleChoose():
    inFile = open('sentence.txt', 'r')
    randomBible = [line.strip() for line in inFile.readlines()]
    inFile.close()
    if randomBible:
        chosen = random.choice(randomBible)
        print(chosen)
    else:
        print('파일이 비어있습니다.')    

bibleWrite()
bibleChoose()