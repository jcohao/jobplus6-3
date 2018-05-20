# coding:utf-8

from flask import Blueprint, render_template,flash
from flask import redirect,url_for
from jobplus.forms import CompanyForm

company = Blueprint('company', __name__, url_prefix='/company')

@company.route('/')
def index():

    return render_template('company/index.html')


@company.route('/profile',methods=['GET','POST'])
def setdetail():
    form = CompanyForm()
    if form.validate_on_submit():
        form.set_details()
        flash('更新信息成功!','success')
        return redirect(url_for('company.index'))
    return render_template('company/set_details.html',form=form)

