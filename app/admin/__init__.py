# -*- coding: utf-8 -*-

"""

    CrawlerProxyService.app.admin
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    stamaimer 12/07/16

"""

from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from app.model import db
from app.model.proxy_ip import ProxyIP
from app.model.proxy_site import ProxySite


admin = Admin(name="CrawlerProxyService Dashboard", template_mode="bootstrap3")

admin.add_view(ModelView(ProxyIP, db.session))
admin.add_view(ModelView(ProxySite, db.session))
