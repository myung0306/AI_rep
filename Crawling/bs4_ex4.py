import requests
import bs4

def crawl_naver_new_ex1(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    result = requests.get(url, headers=headers)

    if result.status_code!=200:
        raise Exception('error:', result.status_code)

    soup=bs4.BeautifulSoup(result.text, 'html.parser')
    print(len(soup.find_all('ul', 'type06_headline')))
    print(len(soup.find('ul', 'type06_headline').find_all('li')))

    new_data=[]
    for li in soup.find('ul', 'type06_headline').find_all('li'):
        photo=li.find('dl').find('dt', 'photo')
        if photo:
            img=photo.find('a').find('img')
            img_desc=img.get('alt')
            img_url=img.get('src')
        else:
            img_desc=None
            img_url=None
        """
        content=photo.find_next_sibling('dt') if photo else li.find('dl').find('dt')
        new_title=content.find('a').text.strip()
        new_url=content.find('a').get('href') 
        """   
        content=photo.find_next_sibling('dt')
        if photo:
            new_title=content.find('a').text.strip()
            new_url=content.find('a').get('href') 
            new_data.append((img_desc, img_url, new_title, new_url)) 
        else:
            li.find('dl').find('dt')

    for li in soup.find('ul', 'type06').find_all('li'):
        photo = li.find('dl').find('dt', 'photo')
        if photo:
            img = photo.find('a').find('img')
            img_desc = img.get('alt')
            img_url = img.get('src')
        else:
            img_desc = None
            img_url = None
        content = photo.find_next_sibling('dt') if photo else li.find('dl').find('dt')
        news_title = content.find('a').text.strip()
        news_url = content.find('a').get('href')
        new_data.append((img_desc, img_url, news_title, news_url))
    return new_data

def crawl_naver_new_ex2(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    result = requests.get(url, headers=headers)
    if result.status_code != 200:
        raise Exception('error:', result.status_code)

    soup = bs4.BeautifulSoup(result.text, 'html.parser')

    new_data = []
    for li in soup.find('ul', 'type06_headline').find_all('li'):
        photo = li.find('dl').find('dt', 'photo')
        if photo:
            img = photo.find('a').find('img')
            img_desc = img.get('alt')
            img_url = img.get('src')
        else:
            img_desc = None
            img_url = None
        content = photo.find_next_sibling('dt') if photo else li.find('dl').find('dt')
        news_title = content.find('a').text.strip()
        news_url = content.find('a').get('href')
        new_data.append((img_desc, img_url, news_title, news_url))

    for li in soup.find('ul', 'type06').find_all('li'):
        photo = li.find('dl').find('dt', 'photo')
        if photo:
            img = photo.find('a').find('img')
            img_desc = img.get('alt')
            img_url = img.get('src')
        else:
            img_desc = None
            img_url = None
        content = photo.find_next_sibling('dt') if photo else li.find('dl').find('dt')
        news_title = content.find('a').text.strip()
        news_url = content.find('a').get('href')
        new_data.append((img_desc, img_url, news_title, news_url))

    current = soup.find('div', 'paging').find('strong')
    next_page = current.find_next_sibling('a')
    return new_data, next_page.text if next_page else None

if __name__=="__main__":
    crawl_naver_new_ex1('https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=100&sid2=264')
    url = 'https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=100&sid2=264&page={}'
    page = '1'
    while True:
        new_data, page = crawl_naver_new_ex2(url.format(page))
        print(new_data)
        if not page:
            break
        
