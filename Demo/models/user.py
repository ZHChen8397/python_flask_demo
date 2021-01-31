from common.db import db

users = []

class UserModel(db.Model):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120))

    def __init__(self, name, password):
        self.name = name
        self.password = password
    
    def update_user(self):
        db.session.commit()

    def add_user(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_user(cls, name):
        return cls.query.filter_by(name=name).first()

    @staticmethod
    def delete_user(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_all_user(cls):
        return cls.query.all()
    
    @classmethod
    def verify_user(cls, name, password):
        return cls.query.filter_by(name = name, password = password).first()
