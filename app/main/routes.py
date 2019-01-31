from flask import session, redirect, url_for, render_template, request, jsonify
from . import main
from .forms import LoginForm
from .functions import San_Functions
from .mongofunctions import San_MongoFunctions
from werkzeug.security import generate_password_hash, \
     check_password_hash
from .db import sanDb
mysql = sanDb()
func_ins = San_Functions();
mongofunc_ins = San_MongoFunctions();
@main.route('/', methods=['GET', 'POST'])
def index():
    """Login form to enter a room."""
    form = LoginForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        session['room'] = form.room.data
        return redirect(url_for('.chat'))
    elif request.method == 'GET':
        form.name.data = session.get('name', '')
        form.room.data = session.get('room', '')
    projects = mongofunc_ins.get_Projects(1)
    return render_template('index.html', form=form,projects=projects)

@main.route('/enter_room', methods=['GET', 'POST'])
def enter_room():
    """Login form to enter a room."""
    form = LoginForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        session['room'] = form.room.data
        return redirect(url_for('.chat'))
    elif request.method == 'GET':
        form.name.data = session.get('name', '')
        form.room.data = session.get('room', '')
    return render_template('chat.html', form=form)
# @main.route("/")
# def main():
#     return render_template('index.html',page = 'Home')
# print(generate_password_hash('sandeep@bangarh'))
@main.route("/about")
def about():
    return render_template('about.html',page = 'About')


@main.route("/admin/logout")
def logout():
    return render_template('/admin/login.html',page = 'Login')

@main.route("/portfolio")
def portfolio():
    return render_template('portfolio.html',page = 'Portfolio')

@main.route("/projects")
def projects():
    return render_template('projects.html',page = 'Projects')

@main.route("/portfolio_detail")
def portfolio_detail():
    return render_template('portfolio-details.html',page = 'Portfolio Detail')

@main.route('/chat')
def chat():
    """Chat room. The user's name and room must be stored in
    the session."""
    name = session.get('name', '')
    room = session.get('room', '')
    if name == '' or room == '':
        return redirect(url_for('.index'))
    return render_template('admin/chat.html', name=name, room=room)

# admin section
@main.route("/admin/")
def admin():
    if 'userid' in session:
        return render_template('/admin/dashboard.html',page = 'dashboard')
    return redirect("/admin/login/", code = 'login')

@main.route("/admin/profile", methods = ['GET', 'POST'])
def profile():
    if request.method == 'POST':
        func_ins.update_profile(request)

    profile_data = func_ins.get_user(1)
    return render_template('admin/profile.html',data = profile_data,page = 'profile')

@main.route("/admin/portfolio_list", methods = ['GET', 'POST'])
def portfolio_list():
    if request.method == 'POST':
        if request.form['edit_id']:
            func_ins.updatePortfolio(request)
        else :
            func_ins.addPortfolio(request)

    portfolio = func_ins.get_portfolio(1)
    return render_template('admin/portfolio.html',data = portfolio,page = 'portfolio')

@main.route("/admin/projects_list", methods = ['GET', 'POST'])
def projects_list():
    project_detail = ''
    if request.method == 'POST':
        if request.form['edit_id']:
            mongofunc_ins.updateProject(request)
        else :
            mongofunc_ins.addProject(request)
    if request.args.get('edit_id'):
        project_detail = mongofunc_ins.get_Projects(1,request.args.get('edit_id'))
    projects = mongofunc_ins.get_Projects(1)
    return render_template('admin/projects.html',data = projects,project_detail = project_detail,page = 'projects')

@main.route("/admin/login/", methods = ['GET', 'POST'])
def login():
    # session['secret_key'] = 'sandeep@bangarh'
    if request.method == 'POST':
        res = mongofunc_ins.login(request)
        if res == 1 :
            print('logged in')
            return redirect(url_for('main.admin'))
        else :
            print('wrong email or password')
            return redirect(url_for('main.login'))

    else:
        # print(generate_password_hash('bangarh309@#'))
        return render_template('/admin/login.html',page = 'login')
