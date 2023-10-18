from sqlalchemy import MetaData,create_engine,Table,Column,Integer,String
from thelottery import log
engine = create_engine('sqlite:///dball.sqlite',echo=True)

conn = engine.connect()
metadata = MetaData()

dball = Table('dball', metadata,
              Column('Id', Integer(),primary_key=True),
              Column('r1', Integer()),
              Column('r2', Integer()),
              Column('r3', Integer()),
              Column('r4', Integer()),
              Column('r5', Integer()),
              Column('r6', Integer()),
              Column('b', Integer()),
              )

if __name__ =="__main__":
    metadata.create_all(engine)
    log.logger.info(repr(dball))

