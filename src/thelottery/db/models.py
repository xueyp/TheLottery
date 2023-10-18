from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from sqlalchemy import Column, Integer, String

class Dball(Base):
    __tablename__='dball'
    id = Column(Integer,primary_key=True,autoincrement=False)
    r1 = Column(Integer)
    r2 = Column(Integer)
    r3 = Column(Integer)
    r4 = Column(Integer)
    r5 = Column(Integer)
    r6 = Column(Integer)
    b = Column(Integer)

    def __repr__(self):
        return f"Dball(id,r1,r2,r3,r4,r5,r6,b)"
