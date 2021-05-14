from flask import Flask


class BaseHttpServer(Flask):
    """A custom Flask app for BaseHttpServer"""

    def __init__(self, *args, **kwargs):
        # 继承 flask 的init方法
        super(BaseHttpServer, self).__init__(__name__, *args, **kwargs)
        # ...
        print('做一些Flask的初始化动作')


def create_app():
    from . import (
        mail,
        food_manage,
    )
    from .metrics import request as request_metrics
    app = BaseHttpServer()
    request_metrics.init_app(app)
    mail.init_app(app)
    food_manage.init_app(app)
    return app
