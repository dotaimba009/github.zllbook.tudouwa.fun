'''
1. 版本号管理
2. 初始化日志
3. 初始化邮件
'''

from .app import create_app
from flask_mail import Mail

__version__ = "9.0.0-beta"


def setup_logging():
    return 0


setup_logging()
mail = Mail()
