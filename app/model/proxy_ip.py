# -*- coding: utf-8 -*-

"""

    CrawlerProxyService.app.model.proxy_ip
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    stamaimer 12/07/16

"""

from app.model import db


class ProxyIP(db.Model):

    __tablename__ = "proxy_ip"

    id = db.Column(db.Integer(), primary_key=1)

    ip_port = db.Column(db.String(20), unique=1, nullable=0)

    quality = db.Column(db.String(20))

    def __init__(self, ip_port="", quality=""):

        self.ip_port = ip_port

        self.quality = quality

    def __repr__(self):

        return self.ip_port

    def to_json(self):

        proxy_ip = dict()

        proxy_ip["ip_port"] = self.ip_port

        proxy_ip["quality"] = self.quality

        return proxy_ip
