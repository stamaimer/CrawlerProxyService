# -*- coding: utf-8 -*-

"""

    CrawlerProxyService.app
    ~~~~~~~~~~~~~~~~~~~~~~~

    stamaimer 12/07/16

"""

from flask import Flask


def create_app(config_name):

    app = Flask(__name__, instance_relative_config=1)

    app.config.from_object(config_name)
    app.config.from_pyfile("config.py")

    from model import db

    db.init_app(app)

    from admin import admin

    admin.init_app(app)

    return app
