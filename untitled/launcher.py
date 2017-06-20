# -*- coding: cp949 -*-
loopFlag = 1
from internetbook import *
from xml.etree.ElementTree import *


#### Menu  implementation
def printMenu():
    print("\n������깰 �ü� (xml version)")
    print("========Menu==========")
    print("���ϴ� ��¥ �ü����� ��������: g")
    print("���ϴ� ǰ�� �ü����� ��������: e")
    print("���� ������:i")
    print("���α׷� ����:   q")
    print("========Menu==========")


def launcherFunction(menu):
    if menu == 'q':
        QuitBookMgr()
    elif menu == 'g':
        MP = str(input('��¥�� �Է��ϼ���(yyyymmdd) :'))
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
        TH = str(input('ǰ���� �˻��ϼ��� :'))
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
