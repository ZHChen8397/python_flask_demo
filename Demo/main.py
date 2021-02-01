from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from resources.user import GetUser, AddUser, VerifyUserAccount, Users

app = Flask(__name__)
api = Api(app)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///common/user.db?check_same_thread=False'
app.config['CORS_HEADERS'] = 'Content-Type'
api.add_resource(GetUser, "/getuser/<string:name>")
api.add_resource(AddUser, "/adduser/")
api.add_resource(VerifyUserAccount, "/verifyuser/<string:name>/<string:password>/")
api.add_resource(Users, "/allusers/")


if __name__ == "__main__":
    from common.db import db
    db.init_app(app)


    app.run()