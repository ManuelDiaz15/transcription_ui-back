import json
import logging
#import terceros
from flask import session, jsonify
from flask_restful import Resource, reqparse
from mongoengine.context_managers import switch_db

# Import del sistema
from v1.resources.auth.authorization import Auth
from v1.resources.auth.dbDecorator import dbAccess
from v1.models.api_models import Transcripcion
from flask_cors import cross_origin 




class Transcripcion_CRUD(Resource):
    '''
    Endpoint 4
    '''

    @dbAccess.mongoEngineAccess
    def post(self):  # Se ejecutara este metodo con el metodo post del endpoint
        # creamos un objeto para obtener los datos de la request
        parser = reqparse.RequestParser()
        parser.add_argument("hablante1", type=str, required=True, help="Error al ingresar al Hablante 1")
        parser.add_argument("hablante2", type=str, required=True, help="Error al ingresar al Hablante 2")
        parser.add_argument("compañia", type=str, required=True, help="Error al ingresar la compañia")
        parser.add_argument("porcentajeAcertividad", type=int, required=True, help="Error al ingresar el porsentaje de acertividad")
        parser.add_argument("frace1", type=str, required=True, help="Error al ingresar la frace 1 del hablante 1")
        parser.add_argument("frace2", type=str, required=True, help="Error al ingresar la frace 2 del hablante 2")
        data = parser.parse_args()  # obtenemos los datos de la request

        with switch_db(Transcripcion, session["dbMongoEngine"]):
            my_model = Transcripcion.objects(name=data['hablante1']).first()
            my_model.hablante2 = data['hablante2']
            my_model.compañia = data['compañia']
            my_model.porcentajeAcertividad = data['porcentajeAcertividad']
            my_model.frace1 = data['frace1']
            my_model.frace2 = data['frace2']
            my_model.save()
        return jsonify(my_model.to_json())
