import requests
from bs4 import BeautifulSoup
def urlcontent(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
    }
    r = requests.get(url, headers=headers, proxies={
                          "http": "http://0.0.0.0:8888"}).text
    
    soup = BeautifulSoup(r, "html.parser")
    return soup

