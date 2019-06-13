import requests
from bs4 import BeautifulSoup
from wordcloud import WordCloud
import matplotlib.pyplot as plt

sta_list = []
dic ={}
class dataObject:
    def __init__(self, line_num, sub_sta_nm, ride_pasgr_num, alight_pasgr_num): #생성자 호출
        self.line_num = line_num
        self.sub_sta_nm = sub_sta_nm
        self.ride_pasgr_num = ride_pasgr_num
        self.alight_pasger_num = alight_pasgr_num



data = []
r = requests.get("http://openapi.seoul.go.kr:8088/4b44596977686172363670566c7358/xml/CardSubwayStatsNew/1/604/20190101"
                 )
html = r.text
soup = BeautifulSoup(html, 'html.parser')
codenumber = soup.find_all('row')

for i in range(0, len(codenumber)):

    data.append(dataObject(codenumber[i].line_num.text,
                           codenumber[i].sub_sta_nm.text,
                           int(codenumber[i].ride_pasgr_num.text),
                           codenumber[i].alight_pasgr_num.text))

data.sort(key = lambda object : object.ride_pasgr_num, reverse = True)

for i in range(0, len(codenumber)):
    print(data[i].line_num)
    print(data[i].sub_sta_nm)
    sta_list.append(data[i].sub_sta_nm)
    print(data[i].ride_pasgr_num)
    print(data[i].alight_pasger_num)
    print("----------------------------")

def MakeToDcit():
    for i in range(0,len(codenumber)):
        dic[str(data[i].sub_sta_nm)] = float(data[i].ride_pasgr_num)

MakeToDcit()


#station = " ".join(sta_list) #list에 있는 값을 공백을 기준으로 문자열로 변환

wc = WordCloud(font_path='/Users/harenkei/PycharmProjects/SeoulAPI_parsing/BMHANNA_11yrs_.ttf',
               background_color='black', width=1920, height=1080).generate_from_frequencies(dic)

plt.imshow(wc)
plt.axis("off")
plt.show()