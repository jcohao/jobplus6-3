from flask import Flask, render_template
from jobplus.config import configs
from jobplus.models import db, User
from flask_login import LoginManager

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(configs.get(config))

    register_extensions(app)
    register_blueprints(app)

    return app


# 注册蓝图的函数
def register_blueprints(app):
    from .handlers import front, jobs, company, admin
    app.register_blueprint(front)
    app.register_blueprint(jobs)
    app.register_blueprint(company)
    app.register_blueprint(admin)

# 用于将Flask扩展注册到app
def register_extensions(app):
    # 数据库初始化
    db.init_app(app)

    # 创建登录组件
    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def user_loader(id):
        return User.query.get(id)

    login_manager.login_view = 'front.login'

