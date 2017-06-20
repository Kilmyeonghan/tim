def button3_click():
    import urllib.request
    from xml.dom.minidom import parse, parseString
    import tkinter.messagebox
    global num3
    g_Tk_son3 = Tk()
    g_Tk_son3.title("통합대기 환경지수 나쁨이상 조회")
    g_Tk_son3.geometry('400x600+900+130')
    TempFont = font.Font(g_Tk_son3, size=17, weight='bold', family='Consolas')
    MainText = Label(g_Tk_son3, font=TempFont, text="통합대기 환경지수 나쁨이상 조회")
    MainText.pack()
    MainText.place(x=14, y=60)
    TempFont2 = font.Font(g_Tk_son3, size=8,  weight='bold', family='Consolas')
    #BodyText = Label(g_Tk_son3, font=TempFont2, text="통합대기 환경 지수 : 대기오염도 측정치를 국민이 쉽게 \n알 수 있도록 하고 대기오염으로부터 피해를 예방하기 위한 행동지침을 \n국민에게 제시하기 위하여 대기 오염도에 따른 인체 영향 및 체감 오염도를 고려하여 \n개발된 대기오염도 표현방식")
    #BodyText.pack()
    #BodyText.place(x=14, y=60)

    #index = 1
    #i = 0

    key = "d0%2BHv5pgp8GmP51m%2B3RWr80O1QDyrg%2FLo%2BMoJt1UlLpUiSzcNxzqIbFNBemjEfFR9jmasbOlM8aO%2FIyaYNHX7A%3D%3D"
    url = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getUnityAirEnvrnIdexSnstiveAboveMsrstnList?pageNo=1&numOfRows=10&ServiceKey=" + key

    data = urllib.request.urlopen(url).read()
    f = open("nabbem.xml", "wb")
    f.write(data)
    f.close()

    doc = parse("nabbem.xml")
    stationName = doc.getElementsByTagName("stationName")
    addr = doc.getElementsByTagName("addr")
    num3 = stationName.length
    if num3 == 0:
        tkinter.messagebox.showwarning("알림","정보가 최신화 되지 않았습니다.")
    else:
        station = []
        add = []
        index = 0
        while index < num3:
            tmp1 = str(stationName[index].firstChild.data)
            tmp2 = str(addr[index].firstChild.data)
            station.append(tmp1)
            add.append(tmp2)
            index += 1

    def InitBottmText():
        TempFont = font.Font(g_Tk_son3, size=10, weight='bold', family='Consolas')
        BottomText = Label(g_Tk_son3, font=TempFont, text="미세먼지v0.1")
        BottomText.pack()
        BottomText.place(x=310, y=580)

    def InitRenderText():
        global RenderText

        RenderTextScrollbar = Scrollbar(g_Tk_son3)
        RenderTextScrollbar.pack()
        RenderTextScrollbar.place(x=375, y=200)

        TempFont = font.Font(g_Tk_son3, size=10, family='Consolas')
        RenderText = Text(g_Tk_son3, width=49, height=30, borderwidth=12, relief='ridge',
                          yscrollcommand=RenderTextScrollbar.set)
        RenderText.pack()
        RenderText.place(x=10, y=157)
        RenderTextScrollbar.config(command=RenderText.yview)
        RenderTextScrollbar.pack(side=RIGHT, fill=BOTH)
        RenderText.insert(INSERT, "---------------통합대기 환경 지수---------------")
        RenderText.insert(INSERT,
                          "대기오염도 측정치를 국민이 쉽게 알 수 있도록 하고 대기오염으로부터 피해를 예방하기 위한 행동지침을 국민에게 제시하기 위하여 대기 오염도에 따른 인체 영향 및 체감 오염도를 고려하여 개발된 대기오염도 표현방식\n\n")

        for i in range(num3):
            RenderText.insert(INSERT, "\n(")
            RenderText.insert(INSERT, i + 1)
            RenderText.insert(INSERT, ")")
            RenderText.insert(INSERT, "도로명 : ")
            RenderText.insert(INSERT, station[i])
            RenderText.insert(INSERT, "\n   ")
            RenderText.insert(INSERT, "주소 : ")
            RenderText.insert(INSERT, add[i])
            RenderText.insert(INSERT, "\n\n")
            i += 1
        RenderText.configure(state='disabled')

    InitRenderText()
    InitBottmText()
