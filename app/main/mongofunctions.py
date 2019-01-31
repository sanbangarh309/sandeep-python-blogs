from flask import session
from .db import sanMongoDb
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, \
check_password_hash
from datetime import datetime
from werkzeug.utils import secure_filename
import os
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
db = sanMongoDb()
class San_MongoFunctions:
    def __init__(self):
        self.name = 'name'

    def login(self,request):
        user = db.users.find_one({"email": request.form['email']})
        if check_password_hash(user['password'],request.form['password']):
            session['userid'] = str(user['_id'])
            session['name'] = user['name']
            session['email'] = user['email']
            return 1
        else:
            print('wrong email or password')
            return 0

    def logout(self):
        session.clear()
        return true


    def get_user(self,id):
        result = db.users.find_one()
        return result

    def get_Projects(self,id,projectid=''):
        final_arr = []
        if projectid:
            result = db.projects.find_one({"_id": ObjectId(projectid)})
            print(result)
            return result

        else :
            result = db.projects.find()
            for row in result:
                final_arr.append(row)
        return final_arr

    def addProject(self,request):
        data = {}
        self.type = 'projects'
        image = self.upload_file(request)
        if image :
            data['image'] = image;
        if request.form['name'] :
            data['name'] = request.form['name'];
        if request.form['user_id'] :
            data['user_id'] = request.form['user_id'];
        if request.form['about'] :
            data['about'] = request.form['about'];
        if request.form['start_date'] :
            data['start_date'] = request.form['start_date'];
        if request.form['end_date'] :
            data['end_date'] = request.form['end_date'];
        data['created_at'] = datetime.now();
        project = db.projects
        id = project.insert_one(data).inserted_id
        return id

    def updateProject(self,request):
        data = {}
        self.type = 'projects'
        image = self.upload_file(request)
        if image :
            data['image'] = image;
        if request.form['name'] :
            data['name'] = request.form['name'];
        if request.form['about'] :
            data['about'] = request.form['about'];
        if request.form['start_date'] :
            data['start_date'] = request.form['start_date'];
        if request.form['end_date'] :
            data['end_date'] = request.form['end_date'];
        project = db.projects
        id = project.update_one({'_id': ObjectId(request.form['edit_id'])},{'$set': data}, upsert=False)
        return request.form['edit_id']


    def update_profile(self,request):
        cursor = conn.cursor()
        query = "UPDATE users SET "
        self.type = 'profile'
        image = self.upload_file(request)
        if image != '' :
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
            if 'image' not in request.files:
                # flash('No file part')
                # return redirect(request.url)
                return ''
            file = request.files['image']
            # if user does not select file, browser also
            # submit an empty part without filename
            if file.filename == '':
                # flash('No selected file')
                # return redirect(request.url)
                return ''
            # if file and self.allowed_file(file.filename):
            filename = secure_filename(file.filename)
            print('/uploads/'+filename)
            file.save('./app/static/img/'+self.type+'/'+filename)
            return '/'+self.type+'/'+filename

    def san_Middleware():
        # if 'userid' not in session:
        print('in')
