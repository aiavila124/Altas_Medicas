import jwt
import json
from datetime import datetime, timedelta
from os import getenv
from jwt import exceptions as exp
from functools import wraps

def expire_date(day):
    date = datetime.now() + timedelta(day)    

    return date

def get_token(data):
    token = jwt.encode(payload = {**data, "exp": expire_date(1)}, key = getenv('SECRET_KEY'), algorithm = 'HS256')
    return token

def validate_token(func):
    @wraps(func)
    def wrapper(event, context): #mismos parámetros que la función original
        if 'authorization' not in event['headers']:
            return {'status_code': 401, 'body' : json.dumps({"message": "Se requiere token"})}
        else:
            token = event['headers']['authorization'].split(' ')[1]
            try:
                jwt.decode(token, key = getenv('SECRET_KEY'), algorithms=['HS256'])
                return func(event, context) #representa la función que se está decorando
            
            except jwt.InvalidTokenError:
                return {'status_code': 401, 'body' : json.dumps({"message": "token invalido"})}
            
            except exp.ExpiredSignatureError:
                return {'status_code': 401, 'body' : json.dumps({"message": "token expirado"})}

    return wrapper
