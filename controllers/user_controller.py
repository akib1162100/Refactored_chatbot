from app import app
from flask import jsonify
from flask_restful import Resource ,reqparse
from services.user_service import User_service


class User_controller(Resource):
    global user_parser
    user_parser = reqparse.RequestParser()
    user_parser.add_argument('username', type=str, required=True)
    user_parser.add_argument('password', type=str, required=True)

    
    @app.route('/user')
    def get_all_users():
        response = User_service.get_all_users()
        return jsonify(response)
    
    @app.route('/user/<user_id>')
    def get_user(user_id):
        response = User_service.get_user(user_id)
        return jsonify(response)
    
    @app.route('/user/<user_id>', methods=['PUT'])
    def update_user(user_id):
        response= User_service.get_user_data(user_id)
        # print(user)
        return jsonify(response)

    @app.route('/user/<user_id>', methods=['DELETE'])
    def delete_user(user_id):
        response = User_service.delete_user(user_id)
        return jsonify(response)

    @app.route('/user', methods=['POST'])
    def create_user():
        user = user_parser.parse_args()
        response = User_service.create(user)
        return jsonify(response)
