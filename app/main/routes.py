from flask import session, redirect, url_for, render_template, request, jsonify
from . import main
from .forms import LoginForm
from .functions import San_Functions
from werkzeug.security import generate_password_hash, \
     check_password_hash
from .db import sanDb
mysql = sanDb()
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
    return render_template('index.html', form=form)

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

@main.route("/portfolio")
def portfolio():
    return render_template('portfolio.html',page = 'Portfolio')

@main.route("/portfolio-detail")
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
        San_Functions.update_profile(request)

    profile_data = San_Functions.get_user(1)
    return render_template('admin/profile.html',data = profile_data,page = 'profile')

@main.route("/admin/login/", methods = ['GET', 'POST'])
def login():
    # session['secret_key'] = 'sandeep@bangarh'
    if request.method == 'POST':
        result = request.form
        # print(result)
        # return jsonify(result['email'])
        conn = mysql.connect()
        cursor = conn.cursor()
        results = []
        query = "SELECT * from users WHERE email = %s"
        param = (result['email'])
        cursor.execute(query,param)
        columns = [desc[0] for desc in cursor.description]
        print(columns);
        for row in cursor:
            fin_row = dict(zip(columns, row))
            if check_password_hash(fin_row['password'],result['password']):
                session['userid'] = fin_row['id']
                session['name'] = fin_row['name']
                session['email'] = fin_row['email']
                print('logged in')
                return redirect(url_for('main.admin'))
            else:
                print('wrong email or password')
                return redirect(url_for('main.login'))
        cursor.close()
        return jsonify(result)

    else:
        # print(generate_password_hash('bangarh309@#'))
        return render_template('/admin/login.html',page = 'login')