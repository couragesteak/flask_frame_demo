from flask import Flask
from flask import render_template
from flask import request
from flask_cors import CORS
import os

app = Flask(
    __name__,
    template_folder='template', # 定义html文件位置
    static_url_path='/',		# 定义静态资源路由路径
    static_folder='resource'    # 定义静态资源文件夹
)

# app.config['SECRET_KEY'] = os.urandom(24)  # 生成随机数种子，用于产生SessionID
app.secret_key = os.urandom(24)  # 用于加密会话数据

# 允许跨域请求
CORS(app, supports_credentials=True)

from src.main.controller.index import index
from src.main.controller.login import m_login
from src.main.controller.test import m_test

app.register_blueprint(index)
app.register_blueprint(m_login)
app.register_blueprint(m_test)


# 定义404错误页面
@app.errorhandler(404)
def not_found(e):
    return render_template('error_404.html')


# 定义500错误页面
@app.errorhandler(500)
def internal_error():
    return render_template('error_500.html')


# 定义全局拦截器，实现自动登录
@app.before_request
def before():
    url = request.path
    print(url)

    # 路由 白名单
    pass_list = ['/', '/login', '/logout', '/vcode', '/ecode', '/register']

    if url in pass_list \
            or url.endswith('.ico') or url.endswith('.js') or url.endswith('.css') \
            or url.endswith('.jpg') or url.endswith('.ttf') or url.endswith('.svg') \
            or url.endswith('.woff') or url.endswith('.woff2') or url.endswith('.map') \
            or url.endswith('.mapL2Dwidget') or url.endswith('/label') \
            or url.startswith('/article/') or url.startswith('/search/'):

        pass
    else:
        print('路由不在白名单 需要登录')
        username = request.cookies.get('username')
        password = request.cookies.get('password')

        print(username, password)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081, debug=True)
