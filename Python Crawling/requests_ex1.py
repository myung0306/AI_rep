import requests

def naver_new():
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    url='https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=100&sid2=264'
    result=requests.get(url, headers=headers)
    if result.status_code==200:
        with open('naver_new.html', 'w') as f:
            f.write(result.text)
            print("Success")

def daum_new():        
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    url='https://news.daum.net/'
    result=requests.get(url, headers=headers)
    if result.status_code==200:
        with open('daum_new.html', 'w', encoding='UTF-8') as f:
            f.write(result.text)
            print("Success")

if __name__=="__main__":
    naver_new()
    daum_new()

