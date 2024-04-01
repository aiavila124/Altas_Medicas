from Class.database import Database as DB
from models.login_model import Login_model
from datetime import datetime, timedelta

class Login_class:
    def __init__(self):
        pass

    def insert_login(self, data):
        db = DB().session
        model = Login_model(**data)
        db.add(model)
        db.commit()

        return model.as_dict()
        
    def get_user(self, data, type):
        db = DB().session

        if type == 'login':
            model = db.query(Login_model).filter(Login_model.user == data['user'], Login_model.password == data['password']).first()
        else:
            model = db.query(Login_model).filter(Login_model.user == data['user']).first()

        if model:
            return True
        else:
            return False