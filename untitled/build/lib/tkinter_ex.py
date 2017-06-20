from tkinter import *
from tkinter import font
from internetbook import*
import tkinter.messagebox
g_Tk = Tk()
g_Tk.geometry("400x600+750+200")
DataList = []
ab=[]
def InitTopText():#제목
    TempFont = font.Font(g_Tk, size=20, weight='bold', family = 'Consolas')
    MainText = Label(g_Tk, font = TempFont, text="  현명한 소비자 되기")
    MainText.pack()
    MainText.place(x=20)

def InitText():#날짜
    TempFont1 = font.Font(g_Tk, size=15, weight='bold', family = 'Consolas')
    MainText1 = Label(g_Tk, font = TempFont1, text="날짜:")
    MainText1.pack()
    MainText1.place(x=10,  y= 60)

def InitemailText():#이메일
    TempFont1 = font.Font(g_Tk, size=15, weight='bold', family = 'Consolas')
    MainText1 = Label(g_Tk, font = TempFont1, text="이메일:")
    MainText1.pack()
    MainText1.place(x=10,  y= 530)

def InitemailButton():#이메일 보내기 버튼
     emailFont = font.Font(g_Tk, size=12, weight='bold', family='Consolas')
     emailButton = Button(g_Tk, font=emailFont, text="보내기", command=mailSend)
     emailButton.pack()
     emailButton.place(x=320, y=530)

def InitInputLabel():#날짜 입력창
    global InputLabel
    TempFont = font.Font(g_Tk, size=15, weight='bold', family = 'Consolas')
    InputLabel = Entry(g_Tk, font = TempFont, width = 20, borderwidth = 12, relief = 'ridge')
    InputLabel.pack()
    InputLabel.place(x=70, y=50)

def emailInputLabel():#이메일 입력창
    global InputLabel1
    TempFont = font.Font(g_Tk, size=15, weight='bold', family = 'Consolas')
    InputLabel1 = Entry(g_Tk, font = TempFont, width = 18, borderwidth = 12, relief = 'ridge')
    InputLabel1.pack()
    InputLabel1.place(x=90, y=520)


def InitSearchButton():#검색버튼
    TempFont = font.Font(g_Tk, size=12, weight='bold', family = 'Consolas')
    SearchButton = Button(g_Tk, font = TempFont, text="검색",  command=SearchButtonAction)
    SearchButton.pack()
    SearchButton.place(x=330, y=60)


def SearchButtonAction():
    RenderText.configure(state='normal')
    tag = InputLabel.get()
    RenderText.delete(0.0, END)  # ?댁쟾 異쒕젰 ?띿뒪??紐⑤몢 ??젣
    DataList=getMPDataFromISBN(tag)
    #RenderText.configure(state='disabled')
    a=1
    for i in range(0,len(DataList),6):
        RenderText.insert(INSERT, "[")
        RenderText.insert(INSERT, a)
        RenderText.insert(INSERT, "] ")
        RenderText.insert(INSERT, "\n")
        RenderText.insert(INSERT, "날짜: ")
        RenderText.insert(INSERT, DataList[i])
        RenderText.insert(INSERT, "\n")
        RenderText.insert(INSERT, "품목: ")
        RenderText.insert(INSERT, DataList[i + 1])
        RenderText.insert(INSERT, "\n")
        RenderText.insert(INSERT, "종류: ")
        RenderText.insert(INSERT, DataList[i + 2])
        RenderText.insert(INSERT, "\n")
        RenderText.insert(INSERT, "KG: ")
        RenderText.insert(INSERT, DataList[i + 3])
        RenderText.insert(INSERT, "\n")
        RenderText.insert(INSERT, "키로별 가격: ")
        RenderText.insert(INSERT, DataList[i + 4])
        RenderText.insert(INSERT, "\n")
        RenderText.insert(INSERT, "등급: ")
        RenderText.insert(INSERT, DataList[i + 5])
        RenderText.insert(INSERT, "\n\n")
        a=a+1



def mailSend():

     send=InputLabel1.get()
     send1=InputLabel.get()
     sendMain(send1,send)



#밑에창------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def InitRenderText():
    global RenderText

    RenderTextScrollbar = Scrollbar(g_Tk)
    RenderTextScrollbar.pack()
    RenderTextScrollbar.place(x=375, y=200)

    TempFont = font.Font(g_Tk, size=10, family='Consolas')
    RenderText = Text(g_Tk, width=49, height=27, borderwidth=12, relief='ridge', yscrollcommand=RenderTextScrollbar.set)
    RenderText.pack()
    RenderText.place(x=10, y=110)
    RenderTextScrollbar.config(command=RenderText.yview)
    RenderTextScrollbar.pack(side=RIGHT, fill=BOTH)

    RenderText.configure(state='disabled')


InitTopText()
InitText()
InitemailText()
InitemailButton()
InitInputLabel()
emailInputLabel()
InitSearchButton()
InitRenderText()
#InitSendEmailButton()
#InitSortListBox()
#InitSortButton()

g_Tk.mainloop()