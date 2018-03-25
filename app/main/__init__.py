# -*- coding: utf-8 -*-

"""

    CrawlerProxyService.app.main
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    stamaimer 12/07/16

"""

from flask import Blueprint

# from celary.task import poll


main = Blueprint("main", __name__)


# @main.route('/', methods=["GET"])
# def index():
#
#     r = poll.delay()
#
#     return r.state, 200


