from typing import Text
from flask_appbuilder import Model
from sqlalchemy import Column,String, DateTime, Boolean

class User(Model):
    id = Column(String(32))
    username = Column(String(255))
    password = Column(String(255))
    jwt_token = Column(String(255))
    last_login = Column(DateTime)
    name_id = Column(String(255))
    password_hash = Column(String(255))
    team = Column(String(255))
    api_token = Column(String(4000))
    project = Column(String(255))
    username_is_assigned = Column(Boolean)
    authentication_mechanism = Column(String(255))

    def __init__(self, id, username, password, jwt_token, last_login, name_id, password_hash, team, api_token, project, username_is_assigned, authentication_mechanism):
        self.id = id
        self.username = username
        self.password = password
        self.jwt_token = jwt_token
        self.last_login = last_login
        self.name_id = name_id
        self.password_hash = password_hash
        self.team = team
        self.api_token = api_token
        self.project = project
        self.username_is_assigned = username_is_assigned
        self.authentication_mechanism = authentication_mechanism


    def __repr__(self):
        return self.username