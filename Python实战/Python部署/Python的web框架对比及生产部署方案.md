# Python Web框架对比

## Django

特点：大而全，自带的功能特别特别多，有时候过于笨重

## Flask

特点：小而精，自带的功能特别特别少，第三方模块特别特别多，比较依赖与第三方开发者

flask自带一个服务器，主要用在开发环境，处理能力比较有限。不建议将flask直接部署在生产环境，因为flask直接用于生产环境无论是处理高并发还是鲁棒性都有所欠缺，一般会配合WGSI容器来进行生产环境的部署。Flask应用对象实质上是一个WSGI应用

## 异步框架 Sanic

> 在Web开发的过程中，我们最大的敌人不是用户，而是阻塞。异步可以有效地解决网络 I/O 阻塞，文件 I/O 阻塞。
>
> Python在3.4 引入了 asyncio 库，3.6新增了关键字 `async`和`await`，此后，异步框架迅速发展了起来，性能上能和Node.js比肩，除非是CPU密集型任务，否则没有理由不适用异步框架。

Sanic 可用于生产环境，拥有完善的 中文用户指南 和 API 文档，官方承认的文档，由翻译者进行翻译贡献，由 Sanic 官方团队进行发布。

# Python Web生产部署

**1. Web服务器：** Nginx、Apache用于处理和响应HTTP请求

**2. WSGI容器：** uWsgi、Gunicorn

> Web框架（Flask）和Web服务器（Nginx）之间的通信，需要一套双方都遵守的接口协议。而WSGI协议就是用来统一这两者的接口的（WSGI是为Python语言定义的Web服务器和Web应用程序或框架之间的一种简单而通用的接口）
>
> Gunicorn和uWSGI是常用的WSGI容器，Gunicorn直接用命令启动，不需要编写配置文件，相对uWSGI要容易很多。
>
> Gunicorn是一个unix上被广泛使用的高性能的Python WSGI UNIX HTTP Server。和大多数的web框架兼容，并具有实现简单，轻量级，高性能等特点。gunicorn是支持wsgi协议的http服务器，gevent只是它支持的模式之一，是为了解决django、flask这些web框架自带wsgi server性能低下的问题。自带的webserver更多的是测试用途，线上发布时，最好使用高性能的wsgi server或者是联合nginx做uwsgi。
>

## Gunicorn 部署 flask 服务（小项目推荐使用）

### 安装

```
pip install flask
pip install gunicorn
pip install gevent -i https://pypi.douban.com/simple/
```
### 编写flask
```
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello, World!' 
```
### 使用 Gunicorn 部署 falsk
```
-w 4 指预定义的工作进程数为4	-b 0.0.0.0:8888 指绑定地址和端口	
-k gevent
	多个工作模式：
        同步Worker：sync 默认模式，也就是一次只处理一个请求
        异步Worker：通过Eventlet、Gevent实现的异步模式
        异步IO Worker：目前支持gthread和gaiohttp两种类型
     工作进程类型包括: sync(default)、eventlet、gevent、tornado、gthread、gaiohttp
     
hello是flask的启动python文件，app则是flask应用程序实例
///////////////////////
命令行启动：
gunicorn -w 4 -b 127.0.0.1:5000 hello:app
gunicorn -w 1 -b 0.0.0.0:5000 main:app
--daemon：后台运行
gunicorn -w 1 -b 0.0.0.0:5000 main:app --daemon

gunicorn -w 1 -k gevent --worker-connections 10 -b 0.0.0.0:5000 main:app
官方解释greenlet是轻量级的并行编程，gevent就是利用greenlet实现的基于协程（coroutine）的python的网络library，通过使用greenlet提供了一个在libev事件循环顶部的高级别并发API。即gevent是对greenlet的高级封装。
```

## Nginx + Gunicorn + Flask部署（大项目推荐使用）

