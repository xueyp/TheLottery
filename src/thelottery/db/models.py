from .exts import db

class Dball(db.Model):
    __tablename__ = 'dball'
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    r1 = db.Column(db.Integer)
    r2 = db.Column(db.Integer)
    r3 = db.Column(db.Integer)
    r4 = db.Column(db.Integer)
    r5 = db.Column(db.Integer)
    r6 = db.Column(db.Integer)
    b = db.Column(db.Integer)

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
