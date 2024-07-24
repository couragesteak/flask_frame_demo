from flask import Blueprint, render_template, request, jsonify, abort, redirect, url_for

m_test = Blueprint('test', __name__)


# 參數測試
# http://127.0.0.1:8081/param_test
@m_test.route('/param_test', methods=['GET', 'POST'])
def param_test():
    # 获取当前请求的方法类型
    method = request.method

    data = dict(
        nickname="有勇氣的牛排",
        url="https://www.couragesteak.com/",
    )

    # 根据不同的请求方法获取参数
    if method == 'GET':
        id = request.args.get('id', None)  # 从GET请求中获取参数
        data['id'] = id
        return render_template('test_param.html', data=data)

    elif method == 'POST':
        id = request.form.get('id', None)  # 从POST请求中获取参数
        data['id'] = id
    else:
        param = 'No valid method'

    return jsonify(data)


# 触发404错误的函数
# http://127.0.0.1:8081/trigger_404
@m_test.route('/trigger_404')
def trigger_404():
    abort(404)


# 触发500错误的函数
# http://127.0.0.1:8081/trigger_500
@m_test.route('/trigger_500')
def trigger_500():
    abort(500)


# 带参数的重定向路由
# http://127.0.0.1:8081/redirect_with_param
@m_test.route('/redirect_with_param')
def redirect_with_param():
    result = dict(
        name="有勇氣的牛排"
    )
    # return redirect(url_for('param_test'))
    return redirect('/')
