import requests
from bs4 import BeautifulSoup

class dataObject:
    def __init__(self, line_num, sub_sta_nm, ride_pasgr_num, alight_pasgr_num): #생성자 호출
        self.line_num = line_num
        self.sub_sta_nm = sub_sta_nm
        self.ride_pasgr_num = ride_pasgr_num
        self.alight_pasger_num = alight_pasgr_num

#url = "http://openapi.seoul.go.kr:8088/4b44596977686172363670566c7358/xml/CardSubwayStatsNew/1/5/20151101"
data = [] #list형 data 변수
r = requests.get("http://openapi.seoul.go.kr:8088/4b44596977686172363670566c7358/xml/CardSubwayStatsNew/1/5/20151101") # r 변수에 requests.get 메소드 호출, 인자로 url 전잘
html = r.text
soup = BeautifulSoup(html, 'html.parser')
codenumber = soup.find_all('row')

for i in range(0, len(codenumber)):

    data.append(dataObject(codenumber[i].line_num.text,
                           codenumber[i].sub_sta_nm.text,
                           int(codenumber[i].ride_pasgr_num.text),
                           codenumber[i].alight_pasgr_num.text))

data.sort(key = lambda object : object.ride_pasgr_num, reverse = True)

for i in range(0, 10):
    print(data[i].line_num)
    print(data[i].sub_sta_nm)
    print(data[i].ride_pasgr_num)
    print(data[i].alight_pasger_num)
    print("----------------------------")