# coding:utf-8

from flask import Blueprint,render_template
from flask import redirect,url_for,flash
from jobplus.forms import UserForm
from jobplus.models import User
from flask_login import current_user,  login_required

user = Blueprint('user',__name__,url_prefix='/user')


@user.route('/')
#login_required
def index():
    return render_template('user/index.html')

@user.route('/profile',methods=['GET','POST'])
def setinfo():
    # id需要从login中获取
    #user = current_user
    usr_id=1
    usr = User.query.get_or_404(usr_id)
    form = UserForm(obj=usr)
    if form.validate_on_submit():
        form.set_info(usr)
        flash('修改信息成功!','success')
        return redirect(url_for('user.index'))
    return render_template('user/set_info.html',form=form)
