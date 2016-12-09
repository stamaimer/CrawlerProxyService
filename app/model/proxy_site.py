# -*- coding: utf-8 -*-

"""

    CrawlerProxyService.app.model.proxy_site
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    stamaimer 12/07/16

"""

from app.model import db


class ProxySite(db.Model):

    __tablename__ = "proxy_site"

    id = db.Column(db.Integer(), primary_key=1)

    url = db.Column(db.String(255))

    regex = db.Column(db.String(255))

    def __init__(self, url="", regex=""):

        self.url = url

        self.regex = regex

    def __repr__(self):

        return self.url

    def to_json(self):

        proxy_site = dict()

        proxy_site["url"] = self.url

        proxy_site["regex"] = self.regex

        return proxy_site
