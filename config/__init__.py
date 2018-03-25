# -*- coding: utf-8 -*-

"""

    CrawlerProxyService.config
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    stamaimer 12/07/16

"""


class Config(object):

    # configuration of flask

    HOST = "0.0.0.0"

    PORT = 10086

    SQLALCHEMY_ECHO = 0

    SQLALCHEMY_COMMIT_ON_TEARDOWN = 1

    SQLALCHEMY_TRACK_MODIFICATIONS = 1


from development import DevelopmentConfig
from production import ProductionConfig
from staging import StagingConfig
