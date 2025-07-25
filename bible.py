#파일에 성경 구절 저장 후 리스트로 한 줄씩 옮기기 / 랜덤으로 출력
#캔버스 띄우고 버튼 생성

import tkinter
import random

#성경 구절 입력 및 저장
def bibleWrite():
    outFile = open('sentence.txt', 'a')
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
    if randomBible!='':
        chosen = random.choice(randomBible)
        print(chosen)
    else:
        print('파일이 비어있습니다.')    

#좌표출력기
def mouseMove(event):
    x=event.x
    y=event.y

    labelMouse.config(text=str(x)+', '+str(y))
    labelMouse.place(x=743,y=567)

#GUI => 이미지 찾아서 캔버스로 변경 예정
root = tkinter.Tk()
root.title('성경 구절')
root.geometry('800x600')

#라벨
titleLabel = tkinter.Label(root, text='오늘의 성경 구절', font=('pretendard',40))
titleLabel.place(x=220,y=100)

senLabel = tkinter.Label(root, text='', font=('pretendard',10))
senLabel.place(x=100,y=300)

#좌표출력기
root.bind('<Motion>', mouseMove)
labelMouse = tkinter.Label(root, text=', ', font=('맑은고딕',10))

def btn_click():
    print('돌리쟈!')
    bibleChoose()

#버튼
Btn = tkinter.Button(root, text='Click', font=('pretendard', 25), command=btn_click)
Btn.place(x=350,y=150)

root.mainloop()