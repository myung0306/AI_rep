import requests
import bs4

#Requests 이용해 html을 읽고 beautifulSoap을 이용해 분석
headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
url='https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=100&sid2=264'
result=requests.get(url, headers=headers)

if result.status_code!=200:
    raise Exception('error:', result.status_code)

soup=bs4.BeautifulSoup(result.text, 'html.parser')


