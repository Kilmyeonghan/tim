# -*- coding: cp949 -*-
loopFlag = 1
from internetbook import *
from xml.etree.ElementTree import *


#### Menu  implementation
def printMenu():
    print("\n농축수산물 시세 (xml version)")
    print("========Menu==========")
    print("원하는 날짜 시세정보 가져오기: g")
    print("원하는 품목 시세정보 가져오기: e")
    print("메일 보내기:i")
    print("프로그램 종료:   q")
    print("========Menu==========")


def launcherFunction(menu):
    if menu == 'q':
        QuitBookMgr()
    elif menu == 'g':
        MP = str(input('날짜를 입력하세요(yyyymmdd) :'))
        ret = getMPDataFromISBN(MP)
        count = 0
        for item in ret:
            print(item)
            count += 1
            if (count % 6 == 0):
                print(" ")
                print()
                # AddBook(ret)
    elif menu == 'e':
        TH = str(input('품목을 검색하세요 :'))
        ret = getTHkDataFromISBN(TH)
        count = 0
        for item in ret:
            print(item)
            count += 1
            if (count % 6 == 0):
                print(" ")
                print()
    elif menu == 'i':
        sendMain()
    else:
        print("error : unknow menu key")


def QuitBookMgr():
    global loopFlag
    loopFlag = 0
    BooksFree()


##### run #####
while (loopFlag > 0):
    printMenu()
    menuKey = str(input('select menu :'))
    launcherFunction(menuKey)
else:
    print("Thank you! Good Bye")
