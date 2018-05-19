# *_*coding:utf-8 *_*

from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,ValidationError
from wtforms import TextAreaField,IntegerField
from wtforms.validators import Length,Email,EqualTo,Required,URL,NumberRange
from wtforms import ValidationError
from jobplus.models import User,JobInfo,ComInfo,db


class CompanyForm(FlaskForm):
    com_name = StringField('企业名称',validators=[Required(),Length(3,24)])
    com_email = StringField('邮箱',validators=[Required(),Email()])
    #password = StringField('密码',)
    com_location = StringField('地址',validators=[Required(),Length(3,24)])
    com_logo = StringField('logo链接',validators=[Required(),URL()])
    com_web = StringField('网站链接',validators=[Required(),URL()])
    com_desc_less = StringField('一句话简介',validators=[Required(),Length(3,48)])
    com_desc_more = StringField('详细介绍',validators=[Required(),Length(3,256)])
    submit = SubmitField('提交')
    def set_details(self):
        company = ComInfo()
        
        # 增加用户登录系统后，此处需要修改为当前用户的id，或者去掉
        company.com_id=1
        company.com_name = self.com_name.data
        company.com_email = self.com_email.data
        company.com_location = self.com_location.data
        company.com_logo = self.com_logo.data
        company.com_web = self.com_web.data
        company.com_desc_less = self.com_desc_less.data
        company.com_desc_more = self.com_desc_more.data
        
        db.session.add(company)
        db.session.commit()
        return company

    # 需要验证邮箱唯一性？

class RegisterForm(FlaskForm):
    username = StringField('用户名', validators=[Required(), Length(3, 24)])
    email = StringField('邮箱', validators=[Required(), Email()])
    password = PasswordField('密码', validators=[Required(), Length(6, 24)])
    repeat_password = PasswordField('确认密码', validators=[Required(), EqualTo('password')])
    submit = SubmitField('提交')

  
    def create_user(self):
        user = User()
        user.username = self.username.data
        user.email = self.email.data
        user.password = self.password.data
        db.session.add(user)
        db.session.commit()
        return user

    
class LoginForm(FlaskForm):
    email = StringField('邮箱', validators=[Required(), Email()])
    password = PasswordField('密码', validators=[Required(), Length(6, 24)])
    remember_me = BooleanField('记住我')
    submit = SubmitField('提交')
