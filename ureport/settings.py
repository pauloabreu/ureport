# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

import os
import dj_database_url
import sentry_sdk

from decouple import config
from sentry_sdk.integrations.django import DjangoIntegration
from ureport.settings_common import *

DEBUG = config('DEBUG', default=False, cast=bool)
TEMPLATE_DEBUG = DEBUG

API_BOUNDARY_CACHE_TIME = 30
API_GROUP_CACHE_TIME = 30
API_RESULT_CACHE_TIME = 30
API_CONTACT_RESULT_CACHE_TIME = 30
API_CONTACTS_CACHE_TIME = 30
API_FLOWS_CACHE_TIME = 30

EMPTY_SUBDOMAIN_HOST = config('EMPTY_SUBDOMAIN_HOST', 'https://ureport.in')
HOSTNAME = config('HOSTNAME', 'ureport.in')

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=lambda v: [
                       s.strip() for s in v.split(',')])

SESSION_COOKIE_DOMAIN = config('SESSION_COOKIE_DOMAIN', 'ureport.in')
SESSION_COOKIE_SECURE = False

ANONYMOUS_USER_ID = -1

ADMINS = config('ADMINS',
                default='Ilhasoft|contato@ilhasoft.com.br',
                cast=lambda v: [
                    (
                        s.strip().split('|')[0],
                        s.strip().split('|')[1],
                    ) for s in v.split(',')] if v else [])
MANAGERS = ADMINS

TIME_ZONE = config('TIME_ZONE', default='America/Sao_Paulo')
USER_TIME_ZONE = config('USER_TIME_ZONE', default='America/Sao_Paulo')

EMAIL_HOST = config('EMAIL_HOST', default='localhost')
EMAIL_PORT = config('EMAIL_PORT', default=587, cast=int)
EMAIL_HOST_USER = config('EMAIL_HOST_USER', 'contato@ilhasoft.com.br')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='')
EMAIL_USE_TLS = config('EMAIL_USE_TLS', default=True, cast=bool)

sentry_sdk.init(
    dsn=config('RAVEN_CONFIG', default=''),
    integrations=[DjangoIntegration()]
)

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID', default='')
AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY', default='')
AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME', default='')

AWS_S3_SECURE_URLS = False
AWS_QUERYSTRING_AUTH = False
AWS_S3_FILE_OVERWRITE = False

MEDIA_URL = config('MEDIA_URL', default='https://ureport.ilhasoft.mobi/media/')
SITE_API_HOST = config('SITE_API_HOST', default='https://rapidpro.ilhasoft.mobi')
API_ENDPOINT = config('SITE_API_HOST', default='https://rapidpro.ilhasoft.mobi')

DATABASES = {}
DATABASES['default'] = dj_database_url.parse(config('DEFAULT_DATABASE'))
DATABASES['default']['CONN_MAX_AGE'] = 60

MIDDLEWARE = MIDDLEWARE + ('whitenoise.middleware.WhiteNoiseMiddleware',)
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'HTTPS')

REDIS_HOST = config('REDIS_HOST')
REDIS_DATABASE = config('REDIS_DATABASE', default='1')

BROKER_URL = 'redis://{}:6379/{}'.format(REDIS_HOST, REDIS_DATABASE)

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': BROKER_URL,
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}

CELERY_RESULT_BACKEND = BROKER_URL
CELERY_ALWAYS_EAGER = config('CELERY_ALWAYS_EAGER', default=False, cast=bool)
CELERY_EAGER_PROPAGATES_EXCEPTIONS = config('CELERY_EAGER_PROPAGATES_EXCEPTIONS', default=True, cast=bool)

COMPRESS_ENABLED = config('COMPRESS_ENABLED', default=True, cast=bool)
COMPRESS_OFFLINE = config('COMPRESS_OFFLINE', default=True, cast=bool)
COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter', 'compressor.filters.cssmin.CSSMinFilter']
COMPRESS_JS_FILTERS = ['compressor.filters.jsmin.JSMinFilter']
COMPRESS_OFFLINE_CONTEXT = dict(STATIC_URL=STATIC_URL, base_template='frame.html', debug=False, testing=False)

PREVIOUS_ORG_SITES = [
    dict(
        name="Burkina Faso",
        host="https://burkinafaso.ureport.in",
        flag="https://dl-ureport.s3.amazonaws.com/images/U-Report_Burkina_Faso_Landing_Page_Icon.png",
        is_static=False,
    ),
    dict(
        name="Burundi",
        host="https://burundi.ureport.in",
        flag="https://dl-ureport.s3.amazonaws.com/images/flag_bi.png",
        is_static=False,
    ),
    dict(
        name="Cameroon",
        host="https://cameroon.ureport.in",
        flag="https://dl-ureport.s3.amazonaws.com/images/flag_cm.png",
        is_static=False,
    ),
    dict(
        name="Republique Centrafricaine",
        host="https://centrafrique.ureport.in",
        flag="https://dl-ureport.s3.amazonaws.com/images/flag_cf.png",
        is_static=False,
    ),
    dict(
        name="Chile",
        host="https://chile.ureport.in/",
        flag="https://dl-ureport.s3.amazonaws.com/images/U-Report_Chile_Landing_Page_Icon_2.png",
        is_static=False,
    ),
    dict(
        name="Guinea",
        host="https://guinea.ureport.in",
        flag="https://dl-ureport.s3.amazonaws.com/images/U-Report_Guinea_Landing_Page_Icon.png",
        is_static=False,
    ),
    dict(
        name="Indonesia",
        host="https://indonesia.ureport.in",
        flag="https://dl-ureport.s3.amazonaws.com/images/U-Report_Indonesia_Landing_Page_Icon.png",
        is_static=False,
    ),
    dict(
        name="Liberia",
        host="https://liberia.ureport.in",
        flag="https://dl-ureport.s3.amazonaws.com/images/flag_lr.png",
        is_static=False,
    ),
    dict(
        name="Malawi",
        host="https://www.ureport.mw",
        flag="https://dl-ureport.s3.amazonaws.com/images/Malawi_Web_Deployment-01.png",
        is_static=False,
    ),
    dict(
        name="Malaysia",
        host="https://malaysia.ureport.in",
        flag="https://dl-ureport.s3.amazonaws.com/images/Malaysia_Web_Deployment-01.png",
        is_static=False,
    ),
    dict(
        name="Mali",
        host="https://mali.ureport.in",
        flag="https://dl-ureport.s3.amazonaws.com/images/flag_ml.png",
        is_static=False,
    ),
    dict(
        name="Mexico",
        host="https://mexico.ureport.in",
        flag="https://dl-ureport.s3.amazonaws.com/images/U-Report_Mexico_Landing_Page_Icon.png",
        is_static=False,
    ),
    dict(
        name="Mozambique",
        host="https://mozambique.ureport.in",
        flag="https://dl-ureport.s3.amazonaws.com/images/U-Report_Mozambique_Landing_Page_Icon.png",
        is_static=False,
    ),
    dict(
        name="Nigeria",
        host="https://nigeria.ureport.in",
        flag="https://dl-ureport.s3.amazonaws.com/images/flag_ng.png",
        is_static=False,
    ),
    dict(
        name="Pakistan",
        host="https://ureport.pk",
        flag="https://dl-ureport.s3.amazonaws.com/images/U-Report_Pakistan_Landing_Page_Icon.png",
        is_static=False,
    ),
    dict(
        name="Senegal",
        host="https://senegal.ureport.in",
        flag="https://dl-ureport.s3.amazonaws.com/images/U-Report_Senegal_Landing_Page_Icon.png",
        is_static=False,
    ),
    dict(
        name="Sierra Leone",
        host="https://sierraleone.ureport.in",
        flag="https://dl-ureport.s3.amazonaws.com/images/flag_sl.png",
        is_static=False,
    ),
    dict(
        name="Swaziland",
        host="https://swaziland.ureport.in",
        flag="https://dl-ureport.s3.amazonaws.com/images/flag_sz.png",
        is_static=False,
    ),
    dict(
        name="Uganda",
        host="https://ureport.ug",
        flag="https://dl-ureport.s3.amazonaws.com/images/U-Report_Uganda_Landing_Page_Icon.png",
        is_static=False,
    ),
    dict(
        name="Ukraine",
        host="https://ukraine.ureport.in",
        flag="https://dl-ureport.s3.amazonaws.com/images/U-Report_Ukraine_Landing_Page_Icon.png",
        is_static=False,
    ),
    dict(
        name="Vietnam",
        host="https://vietnam.ureport.in",
        flag="https://dl-ureport.s3.amazonaws.com/images/Vietnam_Web_Deployment-01.png",
        is_static=False,
    ),
    dict(
        name="Zambia",
        host="https://www.zambiaureport.org/home",
        flag="https://s3.amazonaws.com/ureport-app/images/flag_zm.png",
        is_static=False,
    ),
    dict(
        name="Zimbabwe",
        host="https://zimbabwe.ureport.in",
        flag="https://dl-ureport.s3.amazonaws.com/images/flag_zw.png",
        is_static=False,
    ),
    dict(
        name="India",
        host="https://india.ureport.in",
        flag="https://dl-ureport.s3.amazonaws.com/images/U-Report_India_Landing_Page_Icon.png",
        is_static=False,
    ),
    dict(
        name="Myanmar",
        host="https://myanmar.ureport.in",
        flag="https://s3.amazonaws.com/ureport-app/images/U-Report+Myanmar_Landing+Page+Icon.png",
        is_static=False,
    ),
    dict(
        name="Papua New Guinea",
        host="https://png.ureport.in",
        flag="https://dl-ureport.s3.amazonaws.com/images/U-Report_Papua_New_Guinea_Landing_Page_Icon_1_PNG.png",
        is_static=False,
    ),
    dict(
        name="Cote dIvoire",
        host="https://cotedivoire.ureport.in/",
        flag="https://dl-ureport.s3.amazonaws.com/images/U-Report_Cote_dIvoire_Landing_Page_Icon.png",
        is_static=False,
    ),
    dict(
        name="Tunisie",
        host="https://tunisie.ureport.in/",
        flag="https://dl-ureport.s3.amazonaws.com/images/U-Report_Tunisia_Landing_Page_Icon.png",
        is_static=False,
    ),
    dict(
        name="Tanzania",
        host="https://tanzania.ureport.in/",
        flag="https://dl-ureport.s3.amazonaws.com/images/Tanzania_Web_Deployment-01_flag1.png",
        is_static=False,
    ),
    dict(
        name="Nepal",
        host="https://nepal.ureport.in/",
        flag="https://dl-ureport.s3.amazonaws.com/images/U-Report_Nepal_Landing_Page_Icon.png",
        is_static=False,
    ),
    dict(
        name="Tchad",
        host="https://tchad.ureport.in/",
        flag="https://dl-ureport.s3.amazonaws.com/images/Chad_flag.png",
        is_static=False,
    ),
    dict(
        name="South Africa",
        host="https://sa.ureport.in/",
        flag="https://dl-ureport.s3.amazonaws.com/images/U-Report_South_Africa_Landing_Page_Icon.png",
        is_static=False,
    )
]
