import threading
from sqlalchemy.orm import Session
import concurrent.futures
import time
import csv
import random
from sqlalchemy import Integer
from thelottery import spider as spider
from thelottery import log
from db.models import Dball
from db.lotterydb_init import *

balls = []

def obtainOne(id: int):
    log.logger.info('start obtain:' + str(id))
    result = spider.getBallsByID(id)
    if result != None and len(result) > 0:
        balls.append(result)
        time.sleep(random.random())  #0-1秒随机间隔
        #log.logger.info('obtained:' + str(result))
        return result
    return None


def obtainRange(startid: int, endid: int) -> None:
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        for i in range(startid, endid):
            executor.submit(obtainOne, i)
           # time.sleep(1)


def obtainByYear(year: int) -> None:
    for i in range(1, 160, 10): #每年最多开奖365/7*3次，所以160足够
        id = year * 1000 + i
        obtainRange(id, id + 10)

"""
    for i in range(2023, 2024):
        log.logger.info('start obtain year:' + str(i))
        obtainByYear(i)
        log.logger.info('start write csv file:' + str(i))
        basepath = 'data/'
        with open(basepath + str(i) + '.csv', 'w') as file:
            writer = csv.writer(file)
            for row in balls:
                writer.writerow(row)
        log.logger.info('stop write csv file:' + str(i))
"""
if __name__ == '__main__':
    for i in range(2003,2024):
        obtainByYear(i)
    log.logger.info('start write db')
    for row in balls:
        b = Dball(id=row[0], r1=row[1],r2= row[2],r3= row[3], r4=row[4], r5=row[5], r6=row[6],b=row[7])
        log.logger.info('insert Dball:'+str(b))
        with Session(engine) as session:
            session.add(b)
            session.commit()

    log.logger.info('stop write db')
