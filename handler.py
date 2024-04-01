import json
from helper.helper import get_data
from helper.jwt import validate_token, get_token
from Class.tipo_identificacion_class import Tipo_identificacion
from Class.genero_class import Genero_class
from Class.medico_class import Medico_class
from Class.pacientes_class import Pacientes_class
from Class.eps_class import Eps_class
from Class.ingreso_pacientes_class import Ingreso_pacientes_class
from Class.procedimientos_class import Procedimientos_class
from Class.gravedad_class import Gravedad_class
from Class.altas_medicas_class import Altas_medicas_class
from Class.login_class import Login_class

def insert_login(event, context):
    body = get_data(event['body'])
    login = Login_class()

    if login.get_user(body,'user'):
        return {"statusCode": 200, "body": json.dumps("usuario ya existente")}
    else:
        add = login.insert_login(body)

        response = {"statusCode": 200, "body": json.dumps(add)}
        return response

def login(event, context):
    body = get_data(event['body'])
    login = Login_class()
    if login.get_user(body,'login'):
        token = get_token(body)
        response = {"statusCode": 200, "body": json.dumps(token)}
        return response
    
    else:
        response = {"statusCode": 401, "body": json.dumps({"message": "credenciales incorrectas"})}
        return response

@validate_token
def insert_tipo_identificacion(event, context):
    tipo_identificacion =  Tipo_identificacion()
    body = get_data(event['body'])
    add = tipo_identificacion.insert_tipo_identificacion(body)
    response = {"statusCode": 200, "body": json.dumps(add)}

    return response

@validate_token
def get_tipo_identificacion(event, context):

    tipo_identificacion =  Tipo_identificacion()
    data = tipo_identificacion.get_tipo_identificacion()

    response = {"statusCode": 200, "body": json.dumps(data)}

    return response

@validate_token
def insert_genero(event, context):
    genero =  Genero_class()
    body = get_data(event['body'])
    add = genero.insert_genero(body)


    response = {"statusCode": 200, "body": json.dumps(add)}

    return response

@validate_token
def insert_medico(event, context):
    medico = Medico_class()
    body = get_data(event['body'])
    add = medico.insert_medico(body)


    response = {"statusCode": 200, "body": json.dumps(add)}

    return response

@validate_token
def insert_paciente(event, context):
    pacientes = Pacientes_class()
    body = get_data(event['body'])
    add = pacientes.insert_pacientes(body)

    response = {"statusCode": 200, "body": json.dumps(add)}
    return response

@validate_token
def insert_eps(event, context):
    eps = Eps_class()
    body = get_data(event['body'])
    add = eps.insert_eps(body)

    response = {"statusCode": 200, "body": json.dumps(add)}
    return response

@validate_token
def insert_ingreso_pacientes(event, context):
    ingreso_pacientes = Ingreso_pacientes_class()
    body = get_data(event['body'])
    add = ingreso_pacientes.insert_ingreso_pacientes(body)

    response = {"statusCode": 200, "body": json.dumps(add)}
    return response

@validate_token
def delete_ingreso_pacientes(event, context):
    ingreso_pacientes = Ingreso_pacientes_class()
    id = event['pathParameters']['id']
    add = ingreso_pacientes.delete_ingreso_pacientes(id)

    response = {"statusCode": 200, "body": json.dumps(add)}
    return response

@validate_token
def insert_procedimientos(event, context):
    Procedimientos = Procedimientos_class()
    body = get_data(event['body'])
    add = Procedimientos.insert_procedimientos(body)

    response = {"statusCode": 200, "body": json.dumps(add)}
    return response

@validate_token
def insert_gravedad(event, context):
    gravedad = Gravedad_class()
    body = get_data(event['body'])
    add = gravedad.insert_gravedad(body)

    response = {"statusCode": 200, "body": json.dumps(add)}
    return response

@validate_token
def update_gravedad(event, context):
    gravedad = Gravedad_class()
    id = event['pathParameters']['id']
    new_value = get_data(event['body'])
    data = gravedad.update_gravedad(id, new_value)


    response = {"statusCode": 200, "body": json.dumps(data)}
    return response

@validate_token
def insert_altas_medicas(event, context):
    altas_medicas = Altas_medicas_class()
    body = get_data(event['body'])
    add = altas_medicas.insert_altas_medicas(body)

    response = {"statusCode": 200, "body": json.dumps(add)}
    return response