# -*- coding: utf-8 -*-

"""

    CrawlerProxyService.celary.task
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    stamaimer 12/08/16

"""

from sqlalchemy.exc import IntegrityError
from requests.exceptions import RequestException

from app.model.proxy_site import ProxySite
from app.model.proxy_ip import ProxyIP
from app.model import db

from celary import celery
from util import retrieve

import re
import requests


# regex = re.compile("(\d+(?:\.\d+){3})(?::)(\d{2,4})")
# regex = re.compile("(\d+(?:\.\d+){3})(?::?)(?:</td.+?>)(\d{2,4})")


def get_addr(src, regex):

    regex = re.compile(regex)

    addrs = re.findall(regex, src)

    addrs = [':'.join(addr) for addr in set(addrs)]

    for addr in addrs:

        print addr

        try:

            response = requests.get("http://www.163.com", timeout=1, proxies={"http": addr})

            print response.elapsed.total_seconds()

        except RequestException:

            print "pass {addr}".format(addr=addr)

            continue

        proxy_ip = ProxyIP(addr, response.elapsed.total_seconds())

        try:

            db.session.merge(proxy_ip)

        except IntegrityError:

            db.session.rollback()


@celery.task
def poll():

    proxy_sites = ProxySite.query.all()

    for proxy_site in proxy_sites:

        url = proxy_site.url

        regex = proxy_site.regex

        try:

            src = retrieve(url)

        except requests.ConnectionError:

            continue

        get_addr(src, regex)

