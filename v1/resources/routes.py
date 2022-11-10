# obtenemos la clase del recurso que tenemos en el archivo example.py para utilizarlo en un endpoint
#from v1.resources.example.example import Role
from v1.resources.example.example_pymongo import EndPoint1, EndPoint2, EndPoint3
from v1.resources.example.example_crud import Model1_CRUD
from v1.resources.example.Transcripciones_CRUD import Transcripciones_CRUD, Coreccion

def initialize_routes(api):
    '''
    En el endpoint le indicamos el recurso keycloak a utilizar
    con el formato "auth:nombrerecurso:explicacion_corta"
    '''
    #api.add_resource(Role, '/role', endpoint='auth:flask_base:dev', methods=['GET','POST',])
    api.add_resource(EndPoint1, '/endpoint1', endpoint='auth:recurso1', methods=['GET',])
    api.add_resource(EndPoint2, '/endpoint2', endpoint='auth:recurso2', methods=['GET',])
    api.add_resource(EndPoint3, '/endpoint3', endpoint='auth:recurso3', methods=['GET',])
    api.add_resource(Model1_CRUD, '/model1', endpoint='auth:recurso4', methods=['GET', 'POST', 'PUT', 'DELETE'])
    api.add_resource(Transcripciones_CRUD, '/Transcripciones', endpoint='auth:TR_CRUD', methods=['GET', 'POST', 'PUT', 'DELETE'])
    api.add_resource(Coreccion, '/Coreccion', endpoint='auth:TR_CRUD:1', methods=['GET',])

