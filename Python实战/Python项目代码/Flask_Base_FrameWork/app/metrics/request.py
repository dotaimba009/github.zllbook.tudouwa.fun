import logging
import time
from flask import g, request
from collections import namedtuple

metrics_logger = logging.getLogger("metrics")


def record_request_start_time():
    '''
    g：global
    1. g对象是专门用来保存用户的数据的。
    2. g对象在一次请求中的所有的代码的地方，都是可以使用的。
    '''
    g.start_time = time.time()


def calculate_metrics(response):
    if "start_time" not in g:
        return response

    request_duration = (time.time() - g.start_time) * 1000
    queries_duration = g.get("queries_duration", 0.0)
    queries_count = g.get("queries_count", 0.0)
    endpoint = (request.endpoint or "unknown").replace(".", "-")

    metrics_logger.info("method=%s \
                        path=%s \
                        endpoint=%s \
                        status=%s \
                        content_type=%s \
                        content_length=%d \
                        duration=%.2f \
                        query_count=%d \
                        query_duration=%.2f",
                        request.method,
                        request.path,
                        endpoint,
                        response.status_code,
                        response.content_type,
                        response.content_length or -1,
                        request_duration,
                        queries_count,
                        queries_duration)
    return response


MockResponse = namedtuple(
    "MockResponse", ["status_code", "content_type", "content_length"]
)


def calculate_metrics_on_exception(error):
    if error is not None:
        print('calculate_metrics_on_exception=', error)
        calculate_metrics(MockResponse(500, "?", -1))


def init_app(app):
    '''
    app.before_request() 处理路由规则对应的 view_function 执行执行的函数，执行顺序是先绑定先执行，
                        并且先执行 flask app的 before_request，再处理 blueprint 的 before_request。
                        注意：每一次请求到来后，都会先执行它，如果没有执行到 abort(400)

    app.errorhandler() 被触发的前提是 view_function 中抛出了错误，并且错误码能够匹配上注册的 errorhandler 的错误码
                        @app.errorhandler(500)
                        def error_handler(err):
                            print('I am in error_handler')
                            raise err

    app.after_request() 会在请求得到响应后返回给用户前被调用（请求已经被app.route装饰的函数响应过了，已经形成了response），
                        被触发的前提是没有异常抛出，或者异常被 errorhandler 接住并处理，
                        after_request 执行的顺序是先绑定后执行。
                        flask有一个插件叫 flask-compress，
                        是对响应结果进行压缩的，它就是用after_request的这个机制，在response返回前对数据进行了压缩，
                        如果你有别的想要操作的事情，同样可以使用after_request来完成。

    app.teardown_request() teardown_request 没有固定的执行位置. 因为他直接和请求上下文环境挂钩，
                        只有在请求上下文被 pop 出请求栈的时候才会触发，所以即使之前有抛出错误的时候也都会被执行,
                        执行完后返回 response.
                        执行 teardown_request 的时候也是先绑定的后执行

    总结：这几种装饰器装饰方法执行先后为 before_request -> errorhandler -> after_request,
    teardown_request 在将当前请求 pop 出请求栈的时候执行，如下图所示：
    -------------------------------
    -       before_request        -
    -------------------------------
                |                 |
    -------------------------     |
    -       view_function   -     |
    -------------------------     |
      |         |           |     |
      |   ----------------  |     |
      |   - errorhandler -  |     |
      |   ----------------  |     |
      |         |        |  |     |
    ------------------   |  |     |
    -  after_request -   |  |     |
    ------------------   |  |     |
                |        |  |     |
    -------------------------------
    -      teardown_request       -
    -------------------------------
    '''
    app.before_request(record_request_start_time)
    app.after_request(calculate_metrics)
    app.teardown_request(calculate_metrics_on_exception)
