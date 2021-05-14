# Python flask 实用知识点的理解

## Flask路由是如何工作的

> 原文：https://www.jianshu.com/p/808917d76b51

flask框架（及以*Werkzeug*类库为基础构建的应用）的程序理念是把URL地址映射到运行的业务逻辑上(最典型的就是视图函数)，例如：

```
@app.route('/greeting/<name>')
def give_greeting(name):
    return 'Hello, {0}!'.format(name)
    
add_url_rule 函数实现了同样的目的，只不过没有使用装饰器，因此，下面的程序是等价的：
# 抬头没有使用路由装饰器，我们在最后用另一种方法添加路由.
def give_greeting(name):
    return 'Hello, {0}!'.format(name)
    
# add_url_rule()中3个参数依次是rule、view_func、endpoint.
app.add_url_rule('/greeting/<name>', 'give_greeting', give_greeting)
```

1. Flask 捕捉到 URL 地址后的流程是 `URL --> endpoint --> view_function`
2. URL（http://xxxx/greeting/xxx）映射到端点(endpoint) "give_greeting " 上，指向端点 "give_greeting" 的请求被视图函数 "give_greeting" 处理。
3. 端点(endpoint)是程序中一组逻辑处理单元的ID，该ID对应的代码决定了对此ID请求应该作出何种响应，通常端点与视图函数同名，但也可修改。
4. 端点通常用作反向查询URL地址。例如，把一个视图关联到另一个视图（或从站点的一处连接到另一处），直接实用 `url_for()` 即可，例如：

```
@app.route('/')
def index():
    print url_for('give_greeting', name='Mark') # 打印出 '/greeting/Mark' ，其中 'give_greeting' 为端点名

@app.route('/greeting/<name>')
def give_greeting(name):
    return 'Hello, {0}!'.format(name)
    
这样做我们可以随意改变应用中的URL地址，却不用修改与之关联的资源的代码。
```

​	为何要先把URL映射到端点上，再通过端点映射到视图函数上：采用这种方法能够使程序更高、更快、更强。例如蓝本。蓝本允许我们把应用分割为一个个小的部分，现在admin蓝本中含有超级管理员级的资源，user蓝本中则含有用户一级的资源。蓝本允许咱们把应用分割为一个个以命名空间区分的小部分。

```
# admin.py
admin = Blueprint('admin', __name__)

@admin.route('/greeting')
def greeting():
    return 'Hello, administrative user!'

# user.py
user = Blueprint('user', __name__)
@user.route('/greeting')
def greeting():
    return 'Hello, lowly normal user!'
    
# main.py
from flask import Flask, Blueprint
from admin import admin
from user import user

app = Flask(__name__)
app.register_blueprint(admin, url_prefix='admin')
app.register_blueprint(user, url_prefix='user')

print url_for('admin.greeting') # Prints '/admin/greeting'
print url_for('user.greeting') # Prints '/user/greeting'
```

测试：

```
from flask import Flask, url_for

app = Flask(__name__)

# We can use url_for('foo_view') for reverse-lookups in templates or view functions
@app.route('/foo')
def foo_view():
    pass

# We now specify the custom endpoint named 'bufar'. url_for('bar_view') will fail!
@app.route('/bar', endpoint='bufar')
def bar_view():
    pass

with app.test_request_context('/'):
    print (url_for('foo_view'))  #/foo
    print (url_for('bufar'))  #/bar
    # url_for('bar_view') will raise werkzeug.routing.BuildError
    print (url_for('bar_view'))  #端点bar_view是没有定义的
```



