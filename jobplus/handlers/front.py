from flask import Blueprint, render_template

front = Blueprint('front', __name__)

# 首页路由函数
@front.route('/')
def index():
    return render_template('index.html')
