from flask import Blueprint, render_template
index = Blueprint('index', __name__)

# http://127.0.0.1:8081
@index.route('/')
def home():
    res = dict(
        name="有勇氣的牛排"
    )
    return render_template('index.html', result=res)
