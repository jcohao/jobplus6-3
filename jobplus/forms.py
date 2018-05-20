# *_*coding:utf-8 *_*
import re
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, ValidationError
from wtforms.validators import Length, Email, EqualTo, Required
from jobplus.models import db, User


class RegisterForm(FlaskForm):
    username = StringField('用户名', validators=[Required(message='* 用户名不能为空'), Length(3, 24, message='用户名长度要在3～24个字符之间')])
    email = StringField('邮箱', validators=[Required(message='* 邮箱不能为空'), Email(message='邮箱名不合法')])
    password = PasswordField('密码', validators=[Required(message='* 密码不能为空'), Length(6, 24, message='密码长度要在6～24个字符之间')])
    repeat_password = PasswordField('确认密码', validators=[Required(message='* 密码不能为空'), EqualTo('password', message='两次填写的密码不一致')])
    submit = SubmitField('提交')

  
    def create_user(self):
        user = User()
        user.username = self.username.data
        user.email = self.email.data
        user.password = self.password.data
        db.session.add(user)
        db.session.commit()
        return user

    def validate_username(self, field):
        """ 验证用户名是否已存在 """
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('该用户名已注册')


    def validate_email(self, field):
        """ 验证用户邮箱是否已存在 """
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('该邮箱已注册')


    
class LoginForm(FlaskForm):
    username_or_email = StringField('用户名/邮箱', validators=[Required(message='* 用户名/邮箱不能为空')])
    password = PasswordField('密码', validators=[Required(message='* 密码不能为空'), Length(6, 24)])
    remember_me = BooleanField('记住我')
    submit = SubmitField('提交')

    def validate_username_or_email(self, field):
        """ 验证是否为合法的邮箱名或用户 """
        pattern = '\w[-\w.+]*@([A-Za-z0-9][-A-Za-z0-9]+.)+[A-Za-z]{2,14}'
        if re.match(pattern, field.data):
            if not User.query.filter_by(email=field.data).first():
                raise ValidationError('该邮箱未注册')
        else:
            if not User.query.filter_by(username=field.data).first():
                raise ValidationError('该用户不存在')

    def validate_password(self, field):
        user = User.query.filter_by(email=self.username_or_email.data).first()
        if not user:
            user = User.query.filter_by(username=self.username_or_email.data).first()
        if user and not user.check_password(field.data):
            raise ValidationError('密码错误')
