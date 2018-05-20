# *_*coding:utf-8 *_*

from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms import TextAreaField,IntegerField
from wtforms.validators import Length,Email,EqualTo,Required,URL,NumberRange
from wtforms import ValidationError
from jobplus.models import User,JobInfo,ComInfo,db


class CompanyForm(FlaskForm):
    com_name = StringField('企业名称',validators=[Required(),Length(3,24)])
    com_email = StringField('邮箱',validators=[Required(),Email()])
    #password = StringField('密码',)
    com_location = StringField('地址',validators=[Required(),Length(1,24)])
    com_logo = StringField('logo链接',validators=[Required(),URL()])
    com_web = StringField('网站链接',validators=[Required(),URL()])
    com_desc_less = StringField('一句话简介',validators=[Required(),Length(3,48)])
    com_desc_more = StringField('详细介绍',validators=[Required(),Length(3,256)])
    submit = SubmitField('提交')
    
    def set_details(self,company):
        
        # 将表单数据填入数据库映射类对象
        self.populate_obj(company)
        
        db.session.add(company)
        db.session.commit()
        return company

    # 需要验证邮箱唯一性？(需要再添加)


class UserForm(FlaskForm):
    realname = StringField('姓名',validators=[Required(),Length(1,24)])
    email = StringField('邮箱',validators=[Required(),Email()])
    password = PasswordField('密码')
    # 手机号需补充验证
    phone = StringField('手机号',validators=[Required()])
    exp = StringField('工作经验',validators=[Length(0,24)])
    # 简历先用url代替
    resume = StringField('简历',validators=[Required(),URL()])
    submit = SubmitField('提交')

    def set_info(self,user):
        password = user.password
        self.populate_obj(user)
        if not self.password:
            user.password=password
        db.session.add(user)
        db.session.commit()
        return user


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
