from datetime import datetime
from repository.user_repo import User_repository
import uuid
from app import app
from models.user import User
from models.response import Response
from werkzeug.security import generate_password_hash, check_password_hash
import pytz
import jwt

class User_service():
    # user_repo = User_repository()
    # user = User()
    # response = Response()

    def __init__(self):
        self.user_repo = User_repository()
        self.user = User()
        self.response = Response()

    def get_user(self, user_id):
        message , data , code = self.user_repo.get_by_id(user_id)
        response = self.response(code, data, message)
        return response


    def get_all_users(self):
        message , data , code = self.user_repo.get_all()
        response = self.response(code, data, message)
        return response


    def create(self, user):
        ids = self.user_repo.get_all_ids()
        this_uuid = uuid.uuid4().hex
        if this_uuid in ids:
            this_uuid = uuid.uuid4().hex        
        new_user = self.user(this_uuid,user.username,generate_password_hash(user.password))
        message , data , code = self.user_repo.create(new_user)
        response = self.response(code, data, message)
        return response

    def update_user(self,id,username,password):
        message , data , code = self.user_repo.update(id,username,generate_password_hash(password))
        response = self.response(code, data, message)
        return response

    def delete_user(self, user_id):
        message , data , code = self.user_repo.delete_user(user_id)
        response = self.response( code, data, message)
        return response


    def user_login(self, auth):
        if not auth or not auth.username or not auth.password:
            response = self.response(400, None, "Missing username or password")
            return response
        
        user = self.user_repo.get_by_username(auth.username)
        if not user:
            response = self.response(400, None, "Could not verify user")
            return response

        if check_password_hash(user.password, auth.password):
            this_time = datetime.datetime.now(pytz.timezone('Asia/Dhaka'))
            token = jwt.encode({'user_id': user.id, 'exp': this_time+ datetime.timedelta(hours=3)}, app.config['SECRET_KEY'], algorithm='HS256')
            self.user_repo.update_token(user.id, token, this_time)
            response = self.response(200, token, "User logged in successfully")
            return response
        response = self.response(400, None, "Could not verify user")
        return response