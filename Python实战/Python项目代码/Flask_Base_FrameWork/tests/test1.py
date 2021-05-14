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
    print(url_for('foo_view1'))  # /foo
    print(url_for('bufar'))  # /bar
    # url_for('bar_view') will raise werkzeug.routing.BuildError
    # print(url_for('bar_view'))  # 端点bar_view是没有定义的
