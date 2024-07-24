from flask import Blueprint, render_template, make_response, session, request, url_for

from my_init import logger
from src.main.util.util_img_code import ImageCode

m_login = Blueprint('login', __name__)


# 获取验证码图片
# http://127.0.0.1:8081/vcode
@m_login.route('/vcode')
def vcode():
    logger.info('--------vcode-------')
    code, bstring = ImageCode().get_code()
    response = make_response(bstring)
    response.headers['Content-Type'] = 'image/jpeg'
    # print(code)

    # 将session存放到session中
    session['vcode'] = code.lower()

    return response


# http://127.0.0.1:8081/login
@m_login.route('/login', methods=['GET', 'POST'])
def login():
    # 获取当前请求的方法类型
    method = request.method
    res = dict(
        name="有勇氣的牛排"
    )
    return render_template('login.html', result=res)


# 退出登录
@m_login.route('/logout')
def logout():
    # 清空Session, 页面跳转
    session.clear()
    # session.pop('username', None)  # 清除会话中的用户名

    response = make_response('注销并重定向', 302)
    response.headers['Location'] = url_for('index.home')
    response.headers['Location'] = '/'
    response.delete_cookie('username')
    response.set_cookie('password', '', max_age=0)



    # return redirect('/')
    return response
