# flake8: NOQA
from .base import *

DEBUG = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'my_blog',
        'HOST': '127.0.0.1',
        'USER': 'lmz',  # 只有本地访问权限
        "PASSWORD": 'lmz1995',
        'TEST': {
            "name": "my_blog_test",
        }
    }
}
