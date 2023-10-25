from thelottery import log
import os
import click
from flask import Flask
from flask.cli import with_appcontext
from flask_sqlalchemy import SQLAlchemy

from .exts import db


if __name__ =="__main__":
    db.drop_all()
    db.create_all()
    log.logger.info(repr(dball))

