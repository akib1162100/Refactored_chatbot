from _typeshed import Self
from app import app
from flask import jsonify, render_template, request, redirect, url_for, flash, session
from flask_restful import Resource ,reqparse
from services.user_service import User_service 


class User_controller(Resource):
    user_parser = reqparse.RequestParser()
    user_parser.add_argument('username', type=str, required=True)
    user_parser.add_argument('password', type=str, required=True)
    
    
    
    def __init__(self):
        self.user_service = Self.user_service
        self.user_parser = reqparse.RequestParser()
        self.user_parser.add_argument('username', type=str, required=True)
        self.user_parser.add_argument('password', type=str, required=True)
    
    @app.route('/user')
    def get_all_users(self):
        response = self.user_service.get_all_users()
        return jsonify(response)
    
    @app.route('/user/<int:user_id>')
    def get_user(self,user_id):
        response = self.user_service.get_user(user_id)
        return jsonify(response)
    
    @app.route('/user/<int:user_id>', methods=['PUT'])
    def update_user(self,user_id):
        user = self.user_parser.parse_args()
        response = self.user_service.update_user(user_id,user)
        return jsonify(response)

    @app.route('/user/<int:user_id>', methods=['DELETE'])
    def delete_user(self,user_id):
        user = self.user_service.delete_user(user_id)
        return jsonify(user)

    @app.route('/user', methods=['POST'])
    def create_user(self):
        user = self.user_parser.parse_args()
        response = self.user_service.create_user(user)
        return jsonify(response)
