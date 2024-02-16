import socket
from tkinter import *
from threading import Thread
import random
from PIL import ImageTk,Image

# pip install pillow

screen_width=None
screen_height=None

server=None
port=None
ip_address=None

playerName=None

canvas1=None
canvas2=None
NameEntry=None
nameWindow=None
gameWindow=None

leftBoxes=[]
rightBoxes=[]
finishBoxes=None

playerType=None
playerTurn=None

player1Name='joining....'
player2Name="joining....."

player1Lable=None
player2Label=None
player1Score=0
player2Score=0

player1Scorelabel=None
player2Scorelabel=None

dice=None
rollButton=None
resetButton=None
winingMessgae=None


def welcomeScreen():
    global NameEntry,nameWindow,canvas1,playerName
    
    nameWindow=Tk()
    nameWindow.title("welcome")
    nameWindow.attributes('-fullscreen',True)
    
    screen_width=nameWindow.winfo_screenwidth()
    screen_height=nameWindow.winfo_screenheight()
    
    canvas1=Canvas(nameWindow,width=500,height=500)
    canvas1.pack(fill="both",expand=True)
    
    bg=ImageTk.PhotoImage(file='background.png')
    canvas1.create_image(0,0,image=bg,anchor="nw")
    canvas1.create_text(screen_width/2,screen_height/5,text="ENTER YOUR NAME", font=("Chalkboard SE",70),fill="white")
    
    NameEntry=Entry(nameWindow,width=15,justify="center",font=("Chalkboard SE",50),bd=5,bg="white")
    NameEntry.place(x=screen_width/2-230,y=screen_height/2-100)
    
    button=Button(nameWindow,text="Save",font=("Chalkboard SE",20),width=12,height=1,bg="green",bd=1)
    button.place(x=screen_width/2-100,y=screen_height/2-50)
    
    print(screen_width,screen_height)
    nameWindow.mainloop()

def leftBoard():
    global gameWindow
    global leftBoxes
    global screen_height

    xPos = 10
    for box in range(0,11):
        if(box == 0):
            boxLabel = Label(gameWindow, font=("Helvetica",30), width=1, height=1, relief='ridge', borderwidth=0, bg="red")
            boxLabel.place(x=xPos, y=screen_height/2 - 88)
            leftBoxes.append(boxLabel)
            xPos +=30
        else:
            boxLabel = Label(gameWindow, font=("Helvetica",55), width=1, height=1, relief='ridge', borderwidth=0, bg="white")
            boxLabel.place(x=xPos, y=screen_height/2- 100)
            leftBoxes.append(boxLabel)
            xPos +=55


def rightBoard():
    global gameWindow
    global rightBoxes
    global screen_height

    xPos = 700
    for box in range(0,11):
        if(box == 10):
            boxLabel = Label(gameWindow, font=("Helvetica",30), width=1, height=1, relief='ridge', borderwidth=0, bg="yellow")
            boxLabel.place(x=xPos, y=screen_height/2-88)
            rightBoxes.append(boxLabel)
            xPos +=30
        else:
            boxLabel = Label(gameWindow, font=("Helvetica",55), width=1, height=1, relief='ridge', borderwidth=0, bg="white")
            boxLabel.place(x=xPos, y=screen_height/2 - 100)
            rightBoxes.append(boxLabel)
            xPos +=55


def finishingBox():
    global gameWindow
    global finishingBox
    global screen_width
    global screen_height

    finishingBox = Label(gameWindow, text="Home", font=("Chalkboard SE", 22), width=5, height=0, borderwidth=0, bg="green", fg="white")
    finishingBox.place(x=screen_width/2 - 38, y=screen_height/2 -80)
    
            
def gameScreen():
    global playerName,screen_height,screen_width,canvas2,player1Lable,player2Label,player1Score,player2Score,player1Scorelabel,player2Scorelabel
    global gameWindow,player1Name,player2Name,rollButton,resetButton,winingMessgae,dice
    
    gameWindow=Tk()
    gameWindow.title("Game")
    gameWindow.attributes('-fullscreen',True)
    
    
    screen_width= gameWindow.winfo_screenwidth()
    screen_height=gameWindow.winfo_screenheight()
    
    canvas2=Canvas(gameWindow,width=500,height=500)
    canvas2.pack(fill="both",expand=True)
    
        
    bg=ImageTk.PhotoImage(file='background.png')
    canvas2.create_image(0,0,image=bg,anchor="nw")
    canvas2.create_text(screen_width/2,screen_height/5-100,text="LUDO LADDER GAME", font=("Chalkboard SE",70),fill="white")
    
     # Declaring Wining Message
    winingMessage = canvas2.create_text(screen_width/2 + 10, screen_height/2 + 250, text = "win..", font=("Chalkboard SE",100), fill='#fff176')


    # Creating Reset Button
    resetButton =  Button(gameWindow,text="Reset Game", fg='black', font=("Chalkboard SE", 15), bg="grey", width=20, height=5)



    leftBoard()
    rightBoard()
    finishingBox()

    global rollButton
    rollButton = Button(gameWindow,text="Roll Dice", fg='black', font=("Chalkboard SE", 15), bg="grey",width=20, height=5)
    if(playerType == 'player1' and playerTurn):
        rollButton.place(x=screen_width / 2 - 80, y=screen_height/2  + 250)
    else:
        rollButton.pack_forget()

    global playerTurn
    global playerType
    global playerName
    # Additional Activity
    global player1Name
    global player2Name
    global player1Label
    global player2Label
    global player1Score
    global player2Score
    global player1ScoreLabel
    global player2ScoreLabel



   
    # Creating Dice with value 1
    dice = canvas2.create_text(screen_width/2 + 10, screen_height/2 + 100, text = "\u2680", font=("Chalkboard SE",250), fill="white")

    # Creating name board
    player1Label = canvas2.create_text(400,  screen_height/2 + 100, text = player1Name, font=("Chalkboard SE",80), fill='#fff176' )
    player2Label = canvas2.create_text(screen_width - 300, screen_height/2 + 100, text = player2Name, font=("Chalkboard SE",80), 
                                       fill='#fff176' )

    # Creating Score Board
    player1ScoreLabel = canvas2.create_text(400,  screen_height/2 - 160, text = player1Score, font=("Chalkboard SE",80), fill='#fff176' )
    player2ScoreLabel = canvas2.create_text(screen_width - 300, screen_height/2 - 160, text = player2Score, font=("Chalkboard SE",80), fill='#fff176' )


    gameWindow.resizable(True, True)
    gameWindow.mainloop()
    
    gameWindow.mainloop()
    

gameScreen()