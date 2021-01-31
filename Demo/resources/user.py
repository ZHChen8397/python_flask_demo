from flask_restful import Resource, reqparse
from common.db import db
from models.user import UserModel

    

class GetUser(Resource):
    def get(self, name):
        user = UserModel.get_user(name)
        if not user:
            return {
                'message': 'username not exist!'
            }, 403
        return {
            'message': '',
            'name': user.name,
            'password': user.password
        }

class AddUser(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', required=True, help='Name is required')
    parser.add_argument('password', required=True, help='Password is required')

    def post(self):
        arg = self.parser.parse_args()
        user = UserModel(arg['name'], arg['password'])
        user.add_user()
        return {
            'message': 'Insert user success',
            'user': user.name
        }

class VerifyUser(Resource):
    def get(self, name, password):
        user = UserModel.verify_user(name=name, password= password)
        if not user:
            return{
                'message': 'User Not found'
            }
        else:
            return{
                'message': 'success',
                'name':user.name,
                'password':user.password
            }
        
    
#     def put(self, name):
#         arg = self.parser.parse_args()
#         find = [item for item in users if item['name'] == name]
#         if len(find) == 0:
#             return {
#                 'message': 'username not exist!'
#             }, 403
#         user = find[0]
#         user['name'] = arg['name']
#         user['password'] = arg['password']
#         return {
#             'message': 'Update user success',
#             'user': user
#         }

#     def delete(self, name):
#         global users
#         users = [item for item in users if item['name'] != name]
#         return {
#             'message': 'Delete done!'
#         }


class Users(Resource):
    def get(self):
        users = UserModel.get_all_user()
        li = []
        for user in users:
            li.append({"name": user.name, "password": user.password})
        return li