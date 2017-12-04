from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_script import Manager
from datetime import datetime
from flask_wtf import FlaskForm as Form
from wtforms import StringField, SubmitField, TextAreaField, FormField
from wtforms.validators import Required, Email, DataRequired
from flask_sqlalchemy import SQLAlchemy
# from flask_login import login_required  #保护路由
import os
from flask_migrate import Migrate, MigrateCommand
from flask_script import Shell
from flask_mail import Mail
import config

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
manager = Manager(app)
app.config.from_object(config)
app.config['MAIL_SERVER'] = 'smtp.qq.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TIS'] = True
app.config['MAIL_USERNAME'] = '502168573@qq.com'
app.config['MAIL_PASSWORD'] = 'qq199403254014'
app.config['SECRET_KEY'] = 'hard to guess string'
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
# app.config['SQLALCHEMY_DATABASE_URI'] = \
# 'mysql://root:password@localhost:3306/mytest'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
moment = Moment(app)
#  数据库迁移
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


# 初始化数据库连接:

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role')

    def __repr__(self):
        return '<Role %r>' % self.name


"""数据库初始化"""


class Safe(db.Model):
    __tablename__ = 'safe'
    id = db.Column(db.Integer, primary_key=True)
    order_num = db.Column(db.String(64), unique=True)
    main_num = db.Column(db.String(64), unique=True)
    sec_num = db.Column(db.String(64), unique=True)
    control_num = db.Column(db.String(64), unique=True)

    def __repr__(self):
        return '<Safe %r>' % self.order_num


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' % self.username

# class Learnnote(db.Model):
#     __tablename__ = 'learnnote'
#     id = db.Column(db.Integer, primary_key=True, auto_increment=True)
#     creater = db.Column(db.String(30),)
#     text = db.Column(db.Text,)


class NameForm(Form):
    name = StringField("你的名字？", validators=[Required()])
    role = StringField("角色", validators=[Required()])
    submit = SubmitField('登陆')


class Safe_form(Form):
    order_num = StringField("订单号：", validators=[Required()])
    main_num = StringField("主安全气囊：", validators=[Required()])
    sec_num = StringField("副安全气囊：", validators=[Required()])
    control_num = StringField("控制器：", validators=[Required()])
    submit = SubmitField('提交')


class PostForm(Form):
    title = StringField('标题', [DataRequired()])
    to_addr = StringField('收件人地址：')
    text = TextAreaField('内容', [DataRequired()])
    submit = SubmitField('发送')


# @app.route('/secret')
# @login_required
# def secret():
#   return 'Only authenticated users are allowed!'

''' 邮件功能错误'''


@app.route('/email', methods=['GET', 'POST'])
def my_email():
    from email.mime.text import MIMEText
    import smtplib

    form = PostForm()

    if form.validate_on_submit():
        msg = MIMEText(form.text.data, 'plain', 'utf-8')  # plain 参数纯文本
        from_addr = '502168573@qq.com'
        password = 'qq199403254014'
        to_addr = form.to_addr.data
        smtp_server = 'smtp.qq.com'  # 邮件传输服务器
        server = smtplib.SMTP(smtp_server, 25)  # SMTP 默认端口号25
        server.set_debuglevel(1)
        server.login(from_addr, password)
        server.sendmail(from_addr, [to_addr], msg.as_string())
        server.quit()
        flash("发送成功！")
        return render_template(redirect('email'))
    return render_template('email.html', form=form)


@app.route('/myfirst', methods=['GET', 'POST'])
def myfirst():
    form = Safe_form()
    if form.validate_on_submit():
        order_num = Safe.query.filter_by(order_num=form.order_num.data).first()
        if not order_num:
            num = Safe(order_num=form.order_num.data, main_num=form.main_num.data,
                       sec_num=form.sec_num.data, control_num=form.control_num.data)
            db.session.add(num)
            db.session.commit()
            session['order_num'] = form.order_num.data
            session['main_num'] = form.main_num.data
            session['sec_num'] = form.sec_num.data
            session['control_num'] = form.control_num.data
            form.order_num.data = ''
            form.main_num.data = ''
            form.sec_num.data = ''
            form.control_num.data = ''
        else:
            flash('输入订单重复，请重新输入')
            return redirect(url_for('myfirst'))

    return render_template('myfirst.html', form=form)


''' 表格数据传入数据库 查询数据库'''


@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if not user:
            user1 = User(username=form.name.data)
            db.session.add(user1)
            db.session.commit()
            session['known'] = False
        else:
            session['known'] = True
        session['name'] = form.name.data
        session['role'] = form.role.data
        print(User.query.filter_by(username=form.name.data).all())
        print(session['role'])
        return redirect(url_for('user', name=session['name'],
                                role=session['role']))
    return render_template('index.html', form=form)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/user-<name>-<role>')
def user(name, role):
    user_info = {
        'name': name,
        'role': role,
        'k': session.get('known')
    }
    print(user_info['k'])
    return render_template('user.html', **user_info)


'''百度Echarts demo '''


@app.route('/pyecharts')
def found():
    return render_template('pyecharts.html', myechart=scatter3d())


def scatter3d():
    from pyecharts import Scatter3D, Page, Bar
    import random, time, threading
    page = Page()
    attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    v1 = [5, 20, 36, 10, 75, 90]
    v2 = [10, 25, 8, 60, 20, 80]
    bar = Bar("3D柱状图示例")
    bar.add('商家A', attr, v1)
    bar.add('商家B', attr, v2)
    page.add(bar)
    data = [[random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)] for _ in range(80)]
    range_color = ['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf',
                   '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
    scatter3D = Scatter3D("3D 散点图 demo", width=1200, height=600)
    scatter3D.add("", data, is_visualmap=True, visual_range_color=range_color)
    page.add(scatter3D)
    return page.render_embed()


@app.route('/contact')
def login(users_info):
    return render_template('infomation.html')

 # 程序上下文
 # def make_shell_context():
 # return dict(app=app,User=User, db=db, Role=Role, Safe=Safe)
 # manager.add_command("shell", Shell(make_shell_context()))


if __name__ == '__main__':
    manager.run()
