import bs4

#Requests 이용해 html을 읽고 beautifulSoap을 이용해 분석
with open('bs4_tutorial.html', 'r', encoding='UTF-8') as f:
    text=f.read()

soup=bs4.BeautifulSoup(text, 'html.parser')

#find_parent : 임의의 tag의 부모 tag를 찾을 수 있음
print(soup.find('time'))
print(soup.find('time').find_parent('p'))
print(soup.find('time').find_parent('p', 'has-text-grey'))
print(soup.find('time').find_parent('div'))
print(soup.find('time').find_parents('div'))

#find_next_sibling : tag의 동일 계층에 있는 다음 tag조회
print(soup.find('p'))
print(soup.find('p').find_next_sibling('p'))
print(soup.find_all('a'))
print(soup.find('a'))
print(soup.find('a').find_next_sibling('a'))
print(soup.find('a').find_next_siblings('a'))

#find_previous_sibling : tag의 동일 계층에 있는 이전 tag조회
print(soup.find_all('p'))
print(soup.find('p', 'is-small'))
print(soup.find('p', 'is-small').find_previous_sibling('p'))

print(soup.find_all('a'))
print(soup.find('a', href='http://www.ictinnovation.kr/publicity.asp'))
print(soup.find('a', href='http://www.ictinnovation.kr/publicity.asp').find_previous_sibling('a'))
print(soup.find('a', href='http://www.ictinnovation.kr/publicity.asp').find_previous_siblings('a'))

#find_next : 다음 tag를 검색
print(soup.find('p'))
print(soup.find('p').find_next())
print(soup.find('p').find_next().find_next())
print(soup.find('p').find_next().find_next().find_next())
print(soup.find('p').find_next().find_next().find_next().find_next())
print(soup.find('p').find_all_next())

#find_previous : 이전 tag를 검색
print(soup.find('p', 'is-small'))
print(soup.find('p', 'is-small').find_previous())
print(soup.find('p', 'is-small').find_previous().find_previous())
print(soup.find('p', 'is-small').find_previous().find_previous().find_previous())
print(soup.find('p', 'is-small').find_previous().find_previous().find_previous().find_previous())
print(soup.find('p', 'is-small').find_all_previous())

#Information : text멤버 변수로 text조회 가능
print(soup.find('h2'))
print(soup.find('h2').text)
print(soup.find('h2').get('class'))
print(soup.find('img'))
print(soup.find('img').get('alt'))
print(soup.find('img').get('src'))