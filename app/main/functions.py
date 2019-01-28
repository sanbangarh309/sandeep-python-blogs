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
        cursor.execute("SELECT * from portfolio WHERE user_id = %s",(id))
        columns = [desc[0] for desc in cursor.description]
        for row in cursor:
            fin_row = dict(zip(columns, row))
            final_arr.push(fin_row)
        cursor.close()
        return final_arr

    def addPortfolio():
        cursor = conn.cursor()
        colomns = []
 		values = []
        image = self.upload_file(request)
        if image :
            query =  query + "image='"+image+"',"
        if request.form['name'] :
            query =  query + "name='"+request.form['name']+"',"
        if request.form['user_id'] :
            query =  query + "user_id='"+request.form['user_id']+"',"
        if request.form['project_id'] :
            query =  query + "project_id='"+request.form['project_id']+"',"
        if request.form['about'] :
            query =  query + "about='"+request.form['about']+"',"
        query = query.rstrip(',')
        query = query + " WHERE id = "+request.form['edit_id']
        cursor.execute(query)
        conn.commit()
        cursor.close()

    def update_profile(self,request):
        cursor = conn.cursor()
        query = "UPDATE users SET "
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
