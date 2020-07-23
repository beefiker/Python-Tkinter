import pygame
from pygame import mixer
from tkinter import *
from tkinter import messagebox
from tkinter.font import *

# pygame.init()
mixer.init()

# 음악 재생 순서를 위한 변수
playNum=0 

# 노래 일시정지 및 해제를 위한 변수 선언
currentPlaying = False  
nowPaused = False       
nowPlaying = False

# 노래가 끝났을 때 다음 곡을 들려주기 위한 유저이벤트 설정
MUSIC_END = pygame.USEREVENT+1
pygame.mixer.music.set_endevent(MUSIC_END)
            
def play():
    # 함수 내에서 전역변수를 사용하기 위해 global 선언하여 스코프를 확대
    global nowPlaying, nowPaused, currentPlaying, playNum
    
    if currentPlaying == False:
        musicpath='music/'
        lyricpath='lyric/'
        if playNum==0:
            musicpath += playlist[0]                    # 배열을 사용한 위젯의 경로, 이미지, 텍스트 설정
            musicimgLabel.config(image=photo[0])
            musictitleLabel.config(text=playlist[0])
            lyricpath += playlist[0]+'.txt'
        elif playNum==1:
            musicpath += playlist[1]
            musicimgLabel.config(image=photo[1])
            musictitleLabel.config(text=playlist[1])
            lyricpath += playlist[1]+'.txt'
        elif playNum==2:
            musicpath += playlist[2]
            musicimgLabel.config(image=photo[2])
            musictitleLabel.config(text=playlist[2])
            lyricpath += playlist[2]+'.txt'
        elif playNum==3:
            musicpath += playlist[3]
            musicimgLabel.config(image=photo[3])
            musictitleLabel.config(text=playlist[3])
            lyricpath += playlist[3]+'.txt'
        elif playNum==4:
            musicpath += playlist[4]
            musicimgLabel.config(image=photo[4])
            musictitleLabel.config(text=playlist[4])
            lyricpath += playlist[4]+'.txt'
        elif playNum==5:
            musicpath += playlist[5]
            musicimgLabel.config(image=photo[5])
            musictitleLabel.config(text=playlist[5])
            lyricpath += playlist[5]+'.txt'
        elif playNum==6:
            musicpath += playlist[6]
            musicimgLabel.config(image=photo[6])
            musictitleLabel.config(text=playlist[6])
            lyricpath += playlist[6]+'.txt'
        elif playNum==7:
            musicpath += playlist[7]
            musicimgLabel.config(image=photo[7])
            musictitleLabel.config(text=playlist[7])
            lyricpath += playlist[7]+'.txt'
        elif playNum==8:
            musicpath += playlist[8]
            musicimgLabel.config(image=photo[8])
            musictitleLabel.config(text=playlist[8])
            lyricpath += playlist[8]+'.txt'
        
        musicpath += '.mp3'
        f = open(lyricpath, 'r')
        line = f.read()
        musicInfo.insert('1.0',line)
        mixer.music.load(musicpath)
        mixer.music.play()
        currentPlaying = True   # nowPlaying과 nowPaused만을 이용해 일시정지 및 해제를 하기 위해 기본적인 루트를 빠져나오게 함 
        
        btnPlay.config(image=pausePhoto)
        nowPlaying = True  # 할거 다하면 현재 상태인 nowPlaying을 True로 업데이트
        
#        while nowPlaying == True: # 음악이 끝나면 다음노래 자동재생. ( 오류없이 실행되지만 렉이 걸려서 주석처리 )
#            for event in pygame.event.get():
#                if event.type == MUSIC_END:
#                    skip()
        
    elif nowPlaying == True: # 현재 음악이 재생 중 일때 (음악 일시정지를 위한 조건체크)
        mixer.music.pause()
        nowPaused = True
        nowPlaying = False
        btnPlay.config(image=playPhoto)
        
    elif nowPlaying == False and nowPaused == True: # 현재 음악이 일시정지 상태 (음악 일시정지 해제를 위한 조건체크)
        mixer.music.unpause()
        nowPlaying = True
        btnPlay.config(image=pausePhoto)
    
def skip():
    global currentPlaying
    global nowPlaying
    global playNum;
    currentPlaying = False  # 기본적인 루트 재설정
    nowPlaying = True
    playNum=playNum+1
    if playNum > len(playlist)-1:
        playNum = 0
    play()

def prev():
    global currentPlaying
    global nowPlaying
    global playNum;
    currentPlaying = False  # 기본적인 루트 재설정
    nowPlaying = True
    playNum=playNum-1
    if playNum < 0:
        playNum = len(playlist)-1
    play()

def White(event,color="white"): # event와 color를 파라미터로 세팅하여 캔버스에 자그마한 원을 마우스의x축,y축에 따라 생성. color 파라미터의 기본값은 "하양"
    x1,y1 = (event.x - 2),(event.y - 2)
    x2,y2 = (event.x + 2),(event.y + 2)
    canvas.create_oval(x1,y1,x2,y2,fill=color,outline="")
def Black(event,color="black"): 
    x1,y1 = (event.x - 2),(event.y - 2)
    x2,y2 = (event.x + 2),(event.y + 2)
    canvas.create_oval(x1,y1,x2,y2,fill=color,outline="")    
def Red(event,color="red"):
    x1,y1 = (event.x - 2),(event.y - 2)
    x2,y2 = (event.x + 2),(event.y + 2)
    canvas.create_oval(x1,y1,x2,y2,fill=color,outline="")
def Orange(event,color="orange"):
    x1,y1 = (event.x - 2),(event.y - 2)
    x2,y2 = (event.x + 2),(event.y + 2)
    canvas.create_oval(x1,y1,x2,y2,fill=color,outline="")
def Yellow(event,color="yellow"):
    x1,y1 = (event.x - 2),(event.y - 2)
    x2,y2 = (event.x + 2),(event.y + 2)
    canvas.create_oval(x1,y1,x2,y2,fill=color,outline="")
def Green(event,color="green"):
    x1,y1 = (event.x - 2),(event.y - 2)
    x2,y2 = (event.x + 2),(event.y + 2)
    canvas.create_oval(x1,y1,x2,y2,fill=color,outline="")
def Blue(event,color="blue"):
    x1,y1 = (event.x - 2),(event.y - 2)
    x2,y2 = (event.x + 2),(event.y + 2)
    canvas.create_oval(x1,y1,x2,y2,fill=color,outline="")
def Purple(event,color="purple"):
    x1,y1 = (event.x - 2),(event.y - 2)
    x2,y2 = (event.x + 2),(event.y + 2)
    canvas.create_oval(x1,y1,x2,y2,fill=color,outline="")
def erase(event,color="#242424"):
    x1,y1 = (event.x - 8),(event.y - 8)
    x2,y2 = (event.x + 8),(event.y + 8)
    canvas.create_oval(x1,y1,x2,y2,fill=color,outline="")
    
def changeColor(Color): # 브러쉬 색상을 변환하기 위한 함수
    canvas.bind("<B1-Motion>", Color) # 함수명을 arg로 받아 바인드를 쉽게 할 수 있도록 구현함

def clearAll(): # 캔버스의 모든 것들을 삭제하기 위한 함수
    canvas.delete("all")

screen = Tk()
screen.title("2016122006 이재영 기말프로젝트")
screen.geometry('500x550')
screen.resizable(True,False) # "가로"로만 늘릴 수 있도록 설정
playlist=['C jamm - Pokerface','블랙핑크 - Hit you with that','블루','XCX','LONELY DIVER','nafla - 아이스커피','nafla - 좋은 아침이야','nafla - 태워']
photo=[None]*len(playlist)

for i in range(len(playlist)):      # for반복문을 활용하여 PhotoImage 설정
    photopath='photo/'+playlist[i]+'.png'
    photo[i]=PhotoImage(file=photopath).subsample(3)    # 사진의 크기가 너무 커서 subsample을 이용해 축소하여 대입

musicFrame = Frame(bg='#222831')
titlef = Font(family='에스코어 드림 4 Regular',size=11) # 폰트는 폴더에 설치할 수 있도록 otf파일을 준비해두었습니다.
lyricf = Font(family='에스코어 드림 3 Light',size=10)

playPhoto = PhotoImage(file='photo/play.png')
pausePhoto = PhotoImage(file='photo/pause.png')
nextPhoto = PhotoImage(file='photo/next.png')
prevPhoto = PhotoImage(file='photo/prev.png')

btnPrev = Button(musicFrame, image = prevPhoto, command=prev, bg='#222831', fg='#00adb5', bd=0) # 음악플레이어 이전 곡 재생버튼
btnNext = Button(musicFrame, image = nextPhoto, command=skip, bg='#222831', fg='#00adb5', bd=0) # 음악플레이어 다음 곡 재생버튼
btnPlay = Button(musicFrame, image = playPhoto, command=play, bg='#222831', fg='#00adb5', bd=0) # 음악플레이어 재생버튼

musicimgLabel = Label(musicFrame, image=photo[0], width=100, height=120)
musictitleLabel = Label(musicFrame, text='', width=200, height=2, font=titlef, bg='#222831', fg='#fff591')

musicInfo = Text(musicFrame, width=25, height=4, bg='#222831', fg='#00adb5', font=lyricf, bd=0)
scroll_y = Scrollbar(musicFrame, orient='vertical', command=musicInfo.yview)
scroll_y.pack(side="right", fill=Y) 
musicimgLabel.pack(side='left', anchor=NW)

btnPrev.pack(side='left', fill=Y)
btnPlay.pack(side='left', fill=Y)
btnNext.pack(side='left', fill=Y)

musictitleLabel.pack(fill=X, expand=YES)
musicInfo.pack()
musicInfo.configure(yscrollcommand=scroll_y.set) 
musicFrame.pack(fill=X)

NoteFrame = Frame(bg='#242424')
colorPickerFont = Font(size=15)
canvas=Canvas(NoteFrame, width=400, height=380, bg='#242424', bd= 0, highlightthickness = 0)


colorPen=["redPen","orangePen","yellowPen","greenPen","bluePen","purplePen","whitePen","blackPen"]

color=[None]*len(colorPen)

for i in range(len(colorPen)):      # for반복문을 활용하여 colorPicker에 쓰일 PhotoImage 생성
    colorpath='photo/'+colorPen[i]+'.png'
    color[i]=PhotoImage(file=colorpath)

colors=[lambda: changeColor(Red),lambda: changeColor(Orange),lambda: changeColor(Yellow),lambda: changeColor(Green),lambda: changeColor(Blue),
        lambda: changeColor(Purple),lambda: changeColor(White),lambda: changeColor(Black)] # 함수명들을 배열로 정렬

colorPicker = [None]*len(colorPen)

# 위에 생성한 배열을 이용해 for문으로 위젯생성
for i in range(len(colorPen)):
    colorPicker[i] = Button(NoteFrame, image=color[i], bg='#242424', bd = 0, command=colors[i], font=colorPickerFont)    

clearPhoto = PhotoImage(file='photo/delete.png')
eraserPhoto = PhotoImage(file='photo/eraser.png')
eraser = Button(NoteFrame, image=eraserPhoto,fg="black", bg='#242424', bd = 0, command=lambda: changeColor(erase), font=colorPickerFont)
canvasClear = Button(NoteFrame, image=clearPhoto, bg='#242424', bd = 0, command=clearAll)

canvas.pack(fill=BOTH)

# for문으로 colorPicker 배열 크기만큼 pack
for i in range(len(colorPen)):
    colorPicker[i].pack(side='left',expand=YES)

eraser.pack(side='left',expand=YES)
canvasClear.pack(side='right',expand=YES)

changeColor(White) # 기본 드로잉 색상(하양)을 설정
NoteFrame.pack(fill=BOTH, expand=True)

mainloop()
