from repository.user_repo import User_repository
import uuid
from models.user import User
from models.response import Response
from werkzeug.security import generate_password_hash


class User_service():
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