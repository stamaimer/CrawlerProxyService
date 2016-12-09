# -*- coding: utf-8 -*-

"""

    CrawlerProxyService.celary.util
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    stamaimer 12/08/16

"""

import requests
import requests_cache

from fake_useragent import UserAgent


# requests_cache.install_cache()


def retrieve(url, headers=None):

    if not headers:

        headers = dict()

    headers["user-agent"] = UserAgent().random

    print headers, url

    response = requests.get(url, headers=headers)

    if "referer" in headers:

        return response

    string = response.text

    with open("test.html", "w") as temp:

        temp.write(string.encode("utf-8"))

    return string