from django.contrib.staticfiles.storage import staticfiles_storage
from django.template.defaultfilters import date, length, safe, default
from django.urls import reverse

from jinja2 import Environment

def environment(**options):
    # 1.创建Environment实例
    env = Environment(**options)

    # 2.指定（更新）jinja2的函数支线django的指定过滤器
    env.globals.update({
        'static': staticfiles_storage.url,
        'url': reverse,
        'date':date,
        'length':length,
        'safe':safe,
        'default':default,
    })

    # 3.将自定义的过滤器添加到环境中
    env.filters['do_listreverse'] = do_listreverse

    # 4.返回Environment实例
    return env

def do_listreverse(li,le,la):
    if li=='B' and le=='B' and la=='B':
        return '哈哈'
    else:
        return li,le,la

