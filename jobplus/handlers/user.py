# coding:utf-8

from flask import Blueprint, render_template
from flask import redirect, url_for, flash
from jobplus.forms import UserForm, UploadForm
from jobplus.models import User
from jobplus.app import files
from flask_login import current_user, login_required

user = Blueprint('user', __name__, url_prefix='/user')


@user.route('/')
@login_required
def index():
    return render_template('user/index.html')


@user.route('/profile', methods=['GET', 'POST'])
@login_required
def setinfo():
    # 从login中获取当前用户
    usr = current_user
    form = UserForm(obj=usr)
    if form.validate_on_submit():
        form.set_info(usr)
        flash('修改信息成功!', 'success')
        return redirect(url_for('user.index'))
    return render_template('user/set_info.html', form=form)

@user.route('/upload/<int:user_id>', methods=['GET', 'POST'])
@login_required
def upload(user_id):
    form = UploadForm()
    file_name = str(user_id) + '.'
    if form.validate_on_submit():
        filename = files.save(form.file.data, name=file_name)
        file_url = files.url(filename)
    else:
        file_url = None
    return render_template('user/file_upload.html', form=form, url=file_url)
