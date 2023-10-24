from flask import Blueprint
from flask import Flask, render_template, request, url_for, redirect
from flask import Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import io
import os

from io import BytesIO
import base64
from thelottery.db.models import Dball

front_blueprint = Blueprint("front", __name__, url_prefix="/")


@front_blueprint.route('/index')
def index():
    balls = Dball.query.order_by(Dball.id.desc()).all()
    #balls = [Dball(id=2023001, r1=1, r2=2, r3=3, r4=4, r5=5, r6=6, b=7)]
    return render_template('index.html', balls=balls)

@front_blueprint.route('/scatter1')
def plot_scatter():
    [x, y] = Dball.getScatterData()
    #plt.rcParams['figure.dpi'] = 100  # 分辨率
    #plt.rcParams['savefig.dpi'] = 100  # 图片像素
    plt.rcParams['figure.figsize'] = (8.0, 4.0)  # 设置figure_size尺寸800x400
    plt.scatter(x, y, c='b')
    # figure 保存为二进制文件
    buffer = BytesIO()
    plt.savefig(buffer)
    plot_data = buffer.getvalue()
    # 将matplotlib图片转换为HTML
    imb = base64.b64encode(plot_data)  # 对plot_data进行编码
    ims = imb.decode()
    imd = "data:image/png;base64," + ims
    return render_template('matplot.html', img=imd)

@front_blueprint.route('/hello')
def say_hello():
    return 'hello'
