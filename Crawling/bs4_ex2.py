import bs4

#Requests 이용해 html을 읽고 beautifulSoap을 이용해 분석
with open('bs4_tutorial.html', 'r', encoding='UTF-8') as f:
    text=f.read()

soup=bs4.BeautifulSoup(text, 'html.parser')

#find_all()명령을 이용해 모든 tag 조회 가능
print(soup.find_all('p'))
print(soup.find_all('div'))

#find_all()명령의 class이름을 넣으면 class이름을 가진 tag만 모두 조회
print(soup.find_all('p', 'location'))
print(soup.find_all('p', 'is-small'))
print(soup.find_all('p', 'has-text-grey'))
print(soup.find_all('p', 'is-small has-text-grey'))
print(soup.find_all('div', 'media-content'))

#find_all()명령에서 class이외의 속성은 속성 이름과 값을 조건으로 조회 가능
print(soup.find_all('div', id='content'))
print(soup.find_all('a', target='_blank'))
print(soup.find_all('a', target='_blank', href='http://www.ictinnovation.kr/notice.asp'))

#find()명령 결과에 다시 find, find_all등 bs4명령 수행 가능
soup.find('div', 'card').find('div', 'card-content').find_all('p')

