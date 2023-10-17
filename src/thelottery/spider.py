import requests
import json
from bs4 import BeautifulSoup

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0",
          'Host':'kaijiang.78500.cn'}
#data ={'kjData':'2023026'}
def getBallsByID(idd):
    response=requests.get(url='https://kaijiang.78500.cn/ssq/'+idd+'/',headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    #print(soup.prettify())
    kjjg=soup.find('ul',attrs={'class':'kjh'})
    results= [[i.get_text() for i in kjjg.find_all('li',attrs={'class':'rb_kj'})],
    kjjg.find('li',attrs={'class':'b_kj'}).get_text()]
    print(results)
    return results

def main():
    getBallsByID('2023001')

if __name__ == '__main__':
    getBallsByID('2023026')
