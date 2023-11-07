import requests
import bs4

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
url = 'https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=100&sid2=264'
result = requests.get(url, headers=headers)

if result.status_code!=200:
    raise Exception('error:', result.status_code)

soup=bs4.BeautifulSoup(result.text, 'html.parser')
print(len(soup.find_all('ul', 'type06_headline')))


for li in soup.find('ul', 'type06_headline').find_all('li'):
    photo=li.find('dl').find('dt', 'photo')
    if photo:
        img=photo.find('a').find('img')
        img_desc=img.get('alt')
        img_url=img.get('src')
    else:
        img_desc=None
        img_url=None
    content=photo.find_next_sibling('dt') if photo else li.find('dl').find('dt')
    new_title=content.find('a').text.strip()
    new_url=content.find('a').get('href')
print('*'*50)
print(img_desc)
print(img_url)
print(new_title)
print(new_url)