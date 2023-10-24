from flask import Blueprint
from flask import Flask, render_template, request, url_for, redirect
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
from sqlalchemy.sql import func
from thelottery.db.models import Dball

example_blueprint = Blueprint("example", __name__, template_folder="templates",url_prefix="/example")

@example_blueprint.route('/')
def plot_png():
    [x,y]=Dball.getScatterData()
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    axis.scatter(x,y,c='b')
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')
