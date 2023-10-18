import requests
import json
from bs4 import BeautifulSoup
from thelottery import log

headers = {
    'User-Agent':
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0",
    'Host': 'kaijiang.78500.cn'
}


#data ={'kjData':'2023026'}
def getBallsByID(idd: int):
    response = requests.get(url='https://kaijiang.78500.cn/ssq/' + str(idd) +
                            '/',headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    result=[]
    #print(soup.prettify())
    kjjg = soup.find('ul', attrs={'class': 'kjh'})
    if kjjg != None:
        rbs = [
            i.get_text() for i in kjjg.find_all('li', attrs={'class': 'rb_kj'})
        ]
        bbs = kjjg.find('li', attrs={'class': 'b_kj'}).get_text() if kjjg.find('li', attrs={'class': 'b_kj'}) != None else None
        if bbs!=None:
            result.append(idd)
            for i in rbs:
                result.append(int(i))
            result.append(int(bbs))
            log.logger.info(str(result))
        return result
    return None


def main():
    getBallsByID(2023001)


if __name__ == '__main__':
    getBallsByID(2023001)
