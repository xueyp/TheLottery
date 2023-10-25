import threading
import datetime
import concurrent.futures
import time
import csv
import random
from sqlalchemy import Integer
from thelottery import spider as spider
from thelottery import log
from thelottery.db.models import Dball
from thelottery.db.lotterydb_init import *
from thelottery.db.exts import db

balls = []


def obtainOne(id: int):
    log.logger.info('start obtain:' + str(id))
    result = spider.getBallsByID(id)
    if result != None and len(result) > 0:
        balls.append(result)
        time.sleep(random.random())  # 0-1秒随机间隔
        # log.logger.info('obtained:' + str(result))
        return result
    return None


def obtainRange(startid: int, endid: int) -> None:
    startyear = int(str(startid)[:4])
    endyear = int(str(endid)[:4])
    startno = int(str(startid)[4:])
    endno = int(str(endid)[4:])
    log.logger.info("obtainRange:startid:"+str(startyear) +
                    str(startno)+" endid:"+str(endyear)+str(endno))
    for year in range(startyear, endyear+1):
           if startyear != year:
                startno = 1
           for no in range(startno, 161):
                with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
                    executor.submit(obtainOne, year*1000+no)
                    # time.sleep(1)


def obtainByYear(year: int) -> None:
    for i in range(1, 160, 10):  # 每年最多开奖365/7*3次，所以160足够
        id = year * 1000 + i
        obtainRange(id, id + 10)


def getLast():
    last = None
    last = db.session.execute(db.select(Dball).order_by(Dball.id.desc())).scalars().first()
    print(str(last))
    db.session.commit()
    return last


def obtainFromLastID():
    startid = getLast().id+1 #从下一条记录开始取
    year= datetime.date.today().year
    endid = int(year)*1000+160
    log.logger.info('the last ID is:'+str(startid)+" the end ID is:"+str(endid))
    if startid != None:
        obtainRange(startid, endid)

def saveToCVS():
        log.logger.info('start write csv file:' + str(i))
        basepath = 'data/'
        with open(basepath + str(i) + '.csv', 'w') as file:
            writer = csv.writer(file)
            for row in balls:
                writer.writerow(row)
        log.logger.info('stop write csv file:' + str(i))

def saveToSqlite():
    log.logger.info('start write db')
    for row in balls:
        b = Dball(id=row[0], r1=row[1], r2=row[2], r3=row[3],
                  r4=row[4], r5=row[5], r6=row[6], b=row[7])
        log.logger.info('insert Dball:'+str(b))
        db.session.add(b)
        db.session.commit()

    log.logger.info('stop write db')


if __name__ == '__main__':
    obtainFromLastID()
    saveToSqlite()
