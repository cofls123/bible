#파일에 성경 구절 저장 후 리스트로 한 줄씩 옮기기 / 랜덤으로 출력
#캔버스 띄우고 버튼 생성

import tkinter
import random

#함수0: 좌표출력기
def mouseMove(event):
    x=event.x
    y=event.y

    labelMouse.config(text=str(x)+', '+str(y))
    labelMouse.place(x=10,y=10)

#함수1: 성경 구절 입력 및 저장
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

#함수2: 랜덤 출력
def bibleChoose():
    global chosen
    inFile = open('sentence.txt', 'r')
    randomBible = [line.strip() for line in inFile.readlines()]
    inFile.close()
    if randomBible!='':
        chosen = random.choice(randomBible)
    else:
        print('파일이 비어있습니다.')    

#함수3: 문장 수정 / 버튼1
def btn_click():
    global chosen
    bibleChoose()
    senLabel.config(text=chosen)

#함수4: 성경구절 추가 / 버튼2
def addBtn_click():
    bibleWrite()

#캔버스
root = tkinter.Tk()
root.title('성경 구절')
canvas = tkinter.Canvas(root, width=720, height=404)
canvas.pack()
bgimg = tkinter.PhotoImage(file='sun.png')
canvas.create_image(360,202,image=bgimg)

#라벨
titleLabel = tkinter.Label(root, text='오늘의 성경 구절', font=('pretendard',30), bg='#afeedf')
titleLabel.place(x=220,y=100)

senLabel = tkinter.Label(root, text='', font=('pretendard Bold',11), wraplength=539, bg='#afeedf')
senLabel.place(x=100,y=280)

#버튼
Btn = tkinter.Button(root, text='Click', font=('pretendard', 25), bg='#afeedf', command=btn_click)
Btn.place(x=310,y=180)

addBtn = tkinter.Button(root, text='Add Bible', font='pretendard',bg="#e4d9a4", command=addBtn_click)
addBtn.place(x=20,y=20)

#좌표출력기
#root.bind('<Motion>', mouseMove)
#labelMouse = tkinter.Label(root, text=', ', font=('맑은고딕',10))

root.mainloop()