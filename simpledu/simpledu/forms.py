from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import Length, Email, EqualTo, Required
from simpledu.models import db, User, Course
from wtforms import ValidationError
import re
from flask import flash

class RegisterForm(FlaskForm):
    username = StringField('用户名', validators=[Required(), Length(3, 24, message='长度大于3小于24')])
    email = StringField('邮箱', validators=[Required(), Email()])
    password = PasswordField('密码', validators=[Required(), Length(6, 24)])
    repeat_password = PasswordField('重复密码', validators=[Required(), EqualTo('password')])
    submit = SubmitField('提交')

    def create_user(self):
        user=User()
        user.username = self.username.data
        user.email = self.email.data
        user.password = self.password.data
        db.session.add(user)
        db.session.commit()
        return user

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('用户名已存在')
        a = re.findall('[^a-zA-A0-9]', field.data)
        if len(a) > 0:
            flash('非法字符', 'success')
            raise ValidationError('非法字符')
    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱已存在')

class LoginForm(FlaskForm):
#    email = StringField('邮箱', validators=[Required(), Email()])
    username = StringField('用户名', validators=[Required(), Length(3, 24)])
    password = PasswordField('密码', validators=[Required(), Length(6, 24)])
    remember_me = BooleanField('记住我')
    submit = SubmitField('提交')

#    def validate_email(self, field):
#        if field.data and not User.query.filter_by(email=field.data).first():
#            raise ValidationError('邮箱未注册')

    def validate_username(self, field):
        if field.data and not User.query.filter_by(username=field.data).first():
            raise ValidarionError('用户名未注册')
    def validate_password(self, field):
#        user = User.query.filter_by(email=self.email.data).first()
        user = User.query.filter_by(username=self.username.data).first()
        if user and not user.check_password(field.data):
            raise ValidationError('密码错误')
