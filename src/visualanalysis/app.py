import io
from flask import Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import os
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
import matplotlib.pyplot as plt
import numpy as np

from io import BytesIO
import base64
from sqlalchemy.sql import func

basedir = os.path.abspath(os.path.dirname(__file__))
dbdir = os.path.join(basedir, '../..')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(
    dbdir, 'dball.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)


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

    def __repr__(self):
        return f"<Dball(id,r1,r2,r3,r4,r5,r6,b)>"
def getScatterData():
    x=[]
    y=[]
    balls = Dball.query.order_by(Dball.id.desc()).all()
    for b in balls:
        x.append(b.r1+b.r2+b.r3+b.r4+b.r5+b.r6)
        y.append(b.b)
    return [x,y]


@app.route('/')
def index():
    balls = Dball.query.order_by(Dball.id.desc()).all()
    return render_template('index.html', balls=balls)


@app.route('/example')
def plot_png():
    [x,y]=getScatterData()
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    axis.scatter(x,y,c='b')
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


@app.route('/scatter')
def plot_scatter():
    [x,y]=getScatterData()
    #plt.rcParams['figure.dpi'] = 100  # 分辨率
    #plt.rcParams['savefig.dpi'] = 100  # 图片像素
    plt.rcParams['figure.figsize'] = (8.0, 4.0)  # 设置figure_size尺寸800x400
    plt.scatter(x,y,c='b')
    # figure 保存为二进制文件
    buffer = BytesIO()
    plt.savefig(buffer)
    plot_data = buffer.getvalue()
    # 将matplotlib图片转换为HTML
    imb = base64.b64encode(plot_data)  # 对plot_data进行编码
    ims = imb.decode()
    imd = "data:image/png;base64," + ims
    return render_template('matplot.html', img=imd)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
