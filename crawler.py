import requests
from bs4 import BeautifulSoup

def crawler(max_pages):
    page  = 1
    while page < max_pages:
        url = 'http://creativeworks.tistory.com/' + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, 'lxml')
        for link in soup.select('h2'):

        print(soup)

if __name__ == '__main__':
    crawler(4)