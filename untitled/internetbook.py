# -*- coding: cp949 -*-
from xmlbook import *
from http.client import HTTPConnection
from http.server import BaseHTTPRequestHandler, HTTPServer

##global
conn = None
# regKey = '73ee2bc65b*******8b927fc6cd79a97'
regKey = 'v9RnVt%2FWkwThUlBO%2B4k4S%2FTVRH9SCu9w00R2GjWWEhhArSmvJLEAfP4dgYI0v3c5o%2FlbF9yKZY5f51V3wJShFQ%3D%3D'
# OpenAPI 접속 정보 information
server = "apis.data.go.kr"

# smtp 정보
host = "smtp.gmail.com"  # Gmail SMTP 서버 주소.
port = "587"


def userURIBuilder(server, **user):
    str = "http://" + server + "/B552895/LocalGovPriceInfoService/getItemPriceResearchSearch" + "?"
    for key in user.keys():
        str += key + "=" + user[key] + "&"
    return str


def connectOpenAPIServer():
    global conn, server
    conn = HTTPConnection(server)


def getMPDataFromISBN(MP):
    global server, regKey, conn
    if conn == None:
        connectOpenAPIServer()
    uri = userURIBuilder(server, serviceKey=regKey, examin_de=MP)
    conn.request("GET", uri)

    req = conn.getresponse()
    if int(req.status) == 200:
        print("업데이트 완료!!!")
        return SearchfoodTitle(req.read().decode('utf-8'), MP)
        # return extractBookData(req.read().decode('utf-8'))
    else:
        print("OpenAPI request has been failed!! please retry")
        return None


def SearchfoodTitle(strxml, keyword):
    from xml.etree import ElementTree
    retlist = []
    try:
        tree = ElementTree.fromstring(strxml)
    except Exception:
        print("Element Tree parsing Error : maybe the xml document is not corrected.")
        return None
    # get Book Element
    bookElements = tree.getiterator("body")  # return list type
    for data in bookElements:
        for d in data:
            for item in d:
                strDay = item.find("examin_de")
                strTitle = item.find("prdlst_nm")
                strsubTitle = item.find("prdlst_detail_nm")
                strwei = item.find("stndrd")
                strcost = item.find("examin_amt")
                strgrad = item.find("grad")
                # if (strTitle.text.find(keyword) >= 0):
                retlist.append((strDay.text))
                retlist.append((strTitle.text))
                retlist.append((strsubTitle.text))
                retlist.append((strwei.text))
                retlist.append((strcost.text))
                retlist.append((strgrad.text))
    return retlist


def sendMain(date,recipientAddr):
    global host, port
    html = ""
    title="농수축산물"
    senderAddr = "rlfaudgks@gmail.com"
    passwd = "kmh961028"

    html = MakeHtmlDoc(getMPDataFromISBN(date))

    import mysmtplib
    # MIMEMultipart의 MIME을 생성합니다.
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    # Message container를 생성합니다.
    msg = MIMEMultipart('alternative')

    # set message
    msg['Subject'] = title
    msg['From'] = senderAddr
    msg['To'] = recipientAddr

    #msgPart = MIMEText(msgtext, 'plain')
    bookPart = MIMEText(html, 'html', _charset='UTF-8')

    # 메세지에 생성한 MIME 문서를 첨부합니다.
    #msg.attach(msgPart)
    msg.attach(bookPart)

    print("connect smtp server ... ")
    s = mysmtplib.MySMTP(host, port)
    # s.set_debuglevel(1)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(senderAddr, passwd)  # 로긴을 합니다.
    s.sendmail(senderAddr, [recipientAddr], msg.as_string())
    s.close()

    print("Mail sending complete!!!")


class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        from urllib.parse import urlparse
        import sys

        parts = urlparse(self.path)
        keyword, value = parts.query.split('=', 1)

        if keyword == "title":
            html = MakeHtmlDoc(SearchBookTitle(value))  # keyword에 해당하는 책을 검색해서 HTML로 전환합니다.
            ##헤더 부분을 작성.
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(html.encode('utf-8'))  # 본분( body ) 부분을 출력 합니다.
        else:
            self.send_error(400, ' bad requst : please check the your url')  # 잘 못된 요청라는 에러를 응답한다.


def checkConnection():
    global conn
    if conn == None:
        print("Error : connection is fail")
        return False
    return True