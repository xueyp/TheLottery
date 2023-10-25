from .exts import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String

class Dball(db.Model):
    __tablename__ = 'dball'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    r1: Mapped[int]  = mapped_column(Integer)
    r2: Mapped[int]  = mapped_column(Integer)
    r3: Mapped[int]  = mapped_column(Integer)
    r4: Mapped[int]  = mapped_column(Integer)
    r5: Mapped[int]  = mapped_column(Integer)
    r6: Mapped[int]  = mapped_column(Integer)
    b: Mapped[int]  = mapped_column(Integer)

    def getScatterData():
      x=[]
      y=[]
      balls = Dball.query.order_by(Dball.id.desc()).all()
      for b in balls:
          x.append(b.r1+b.r2+b.r3+b.r4+b.r5+b.r6)
          y.append(b.b)
      return [x,y]


    def __repr__(self):
        return f"<Dball(id,r1,r2,r3,r4,r5,r6,b)>"
