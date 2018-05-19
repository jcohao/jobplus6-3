from flask import Flask, render_template
from jobplus.config import configs
from jobplus.models import db

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(configs.get(config))
    
    # 数据库的初始化
    db.init_app(app)


    @app.route('/')
    def index():
        return 'Index'


    return app
