from flask import Flask, render_template
from jobplus.config import configs


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(configs.get(config))

    # 未添加数据库的初始化

    @app.route('/')
    def index():
        return render_template("base.html")


    return app
