# -*- coding: utf-8 -*-

"""

    CrawlerProxyService.celary.config
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    stamaimer 12/08/16

"""

from datetime import timedelta

CELERYBEAT_SCHEDULE = \
{
    'poll':
    {
        'task': 'celary.task.poll',
        'schedule': timedelta(hours=1),
        'args': ()
    },
}

CELERY_ACCEPT_CONTENT = ['pickle', 'json', 'msgpack', 'yaml']