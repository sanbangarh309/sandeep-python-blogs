from .db import sanDb
from werkzeug.security import generate_password_hash, \
check_password_hash
from werkzeug.utils import secure_filename
import os
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
mysql = sanDb()
conn = mysql.connect()
class San_Functions:
    def __init__(self):
        self.name = 'name'

    def login(self,request):
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

    def get_user(self,id):
        cursor = conn.cursor()
        cursor.execute("SELECT * from users WHERE id = %s",(1))
        columns = [desc[0] for desc in cursor.description]
        for row in cursor:
            fin_row = dict(zip(columns, row))
            return fin_row
        cursor.close()

    def get_portfolio(self,id):
        cursor = conn.cursor()
        final_arr = []
        cursor.execute("SELECT * from portfolios WHERE user_id = %s",(id))
        columns = [desc[0] for desc in cursor.description]
        for row in cursor:
            fin_row = dict(zip(columns, row))
            final_arr.push(fin_row)
        cursor.close()
        return final_arr

    def addPortfolio(self,request):
        cursor = conn.cursor()
        colomns = []
        values = []
        image = self.upload_file(request)
        if image :
            colomns.push('image');
            values.push("'"+image+"'");
        if request.form['name'] :
            colomns.push('name');
            values.push("'"+request.form['name']+"'");
        if request.form['user_id'] :
            colomns.push('user_id');
            values.push("'"+request.form['user_id']+"'");
        if request.form['project_id'] :
            colomns.push('project_id');
            values.push("'"+request.form['project_id']+"'");
        if request.form['about'] :
            colomns.push('about');
            values.push("'"+request.form['about']+"'");
        query = query.rstrip(',')
        cols = ",".join(colomns)
        cols = cols.rstrip(',')
        vals = ",".join(values)
        vals = vals.rstrip(',')

        sql = "INSERT INTO portfolios ("+cols+") VALUES("+vals+")"
        print(sql);
        # cursor.execute(query)
        conn.commit()
        cursor.close()

    def get_Projects(self,id,projectid=''):
        cursor = conn.cursor()
        final_arr = []
        if projectid:
            cursor.execute("SELECT * from projects WHERE id = %s",(projectid))
            columns = [desc[0] for desc in cursor.description]
            for row in cursor:
                fin_row = dict(zip(columns, row))
                return fin_row
        else :
            cursor.execute("SELECT * from projects WHERE user_id = %s",(id))
            columns = [desc[0] for desc in cursor.description]
            for row in cursor:
                fin_row = dict(zip(columns, row))
                final_arr.append(fin_row)
        cursor.close()
        return final_arr

    def addProject(self,request):
        cursor = conn.cursor()
        colomns = []
        values = []
        self.type = 'projects'
        image = self.upload_file(request)
        if image :
            colomns.append('image');
            values.append("'"+image+"'");
        if request.form['name'] :
            colomns.append('name');
            values.append("'"+request.form['name']+"'");
        if request.form['user_id'] :
            colomns.append('user_id');
            values.append("'"+request.form['user_id']+"'");
        if request.form['about'] :
            colomns.append('about');
            values.append("'"+request.form['about']+"'");
        if request.form['start_date'] :
            colomns.append('start_date');
            values.append("'"+request.form['start_date']+"'");
        if request.form['end_date'] :
            colomns.append('end_date');
            values.append("'"+request.form['end_date']+"'");
        cols = ",".join(colomns)
        cols = cols.rstrip(',')
        vals = ",".join(values)
        vals = vals.rstrip(',')
        sql = "INSERT INTO projects ("+cols+") VALUES("+vals+")"
        print(sql);
        cursor.execute(sql)
        conn.commit()
        cursor.close()

    def updateProject(self,request):
        cursor = conn.cursor()
        query = "UPDATE projects SET "
        self.type = 'projects'
        image = self.upload_file(request)
        if image :
            query =  query + "image='"+image+"',"
        if request.form['name'] :
            query =  query + "name='"+request.form['name']+"',"
        if request.form['start_date'] :
            query =  query + "start_date='"+request.form['start_date']+"',"
        if request.form['end_date'] :
            query =  query + "end_date='"+request.form['end_date']+"',"
        if request.form['about'] :
            query =  query + "about='"+request.form['about']+"',"
        query = query.rstrip(',')
        query = query + " WHERE id = "+request.form['edit_id']
        cursor.execute(query)
        conn.commit()
        cursor.close()
        return request.form['edit_id']


    def update_profile(self,request):
        cursor = conn.cursor()
        query = "UPDATE users SET "
        self.type = 'profile'
        image = self.upload_file(request)
        if image :
            query =  query + "image='"+image+"',"
        if request.form['name'] :
            query =  query + "name='"+request.form['name']+"',"
        if request.form['email'] :
            query =  query + "email='"+request.form['email']+"',"
        if request.form['phone'] :
            query =  query + "phone='"+request.form['phone']+"',"
        if request.form['address'] :
            query =  query + "address='"+request.form['address']+"',"
        if request.form['about'] :
            query =  query + "about='"+request.form['about']+"',"
        query = query.rstrip(',')
        query = query + " WHERE id = "+request.form['edit_id']
        cursor.execute(query)
        conn.commit()
        cursor.close()
        return request.form['edit_id']

    def allowed_file(filename):
        return '.' in filename and \
               filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

    def upload_file(self,request):
        print(self.type)
        if request.method == 'POST':
            # check if the post request has the file part
            if 'image' not in request.files:
                # flash('No file part')
                # return redirect(request.url)
                return
            file = request.files['image']

            # if user does not select file, browser also
            # submit an empty part without filename
            if file.filename == '':
                # flash('No selected file')
                # return redirect(request.url)
                return
            # if file and self.allowed_file(file.filename):
            filename = secure_filename(file.filename)
            print('/uploads/'+filename)
            # file.save(os.path.join('./static/img/profile', filename))
            file.save('./app/static/img/'+self.type+'/'+filename)
            # file.save('./uploads/'+filename)
            return '/'+self.type+'/'+filename

    def san_Middleware():
        # if 'userid' not in session:
        print('in')

class Upload_Functions:
    def upload_file(request):
        if request.method == 'POST':
            # check if the post request has the file part
            if 'image' not in request.files:
                # flash('No file part')
                # return redirect(request.url)
                return
            file = request.files['image']

            # if user does not select file, browser also
            # submit an empty part without filename
            if file.filename == '':
                # flash('No selected file')
                # return redirect(request.url)
                return
            # if file and self.allowed_file(file.filename):
            filename = secure_filename(file.filename)
            print('/uploads/'+filename)
            # file.save(os.path.join('./static/img/profile', filename))
            file.save('./app/static/img/profile/'+filename)
            # file.save('./uploads/'+filename)
            return '/profile/'+filename
