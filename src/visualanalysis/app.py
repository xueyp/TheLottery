import io
import os
from flask import Flask, render_template, request, url_for, redirect
import thelottery
from thelottery.db.exts import db
from thelottery.db.models import Dball
from blueprints.front import front_blueprint
from blueprints.example import example_blueprint

basedir = os.path.abspath(os.path.dirname(__file__))
dbdir = os.path.join(basedir, "../..")

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    dbdir, "dball.sqlite"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

# 把db与app绑定
db.init_app(app)


# 注册蓝图
app.register_blueprint(front_blueprint)
app.register_blueprint(example_blueprint)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
