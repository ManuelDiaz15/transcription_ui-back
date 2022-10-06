#Imports base de python
#import json
#import logging

#Imports de terceros
from flask import session, g
from flask_restful import Resource  #, reqparse #para crear recursos REST
from bson.json_util import dumps
#Import del sistema
from v1.resources.auth.authorization import Auth  #decorador de authorization y autentificacion
from v1.resources.auth.db_decorator import pymongo_access


class EndPoint1(Resource):
    '''
    Endpoint dummy
    '''
    def get(self):
        return "Hola Mundo", 200


class EndPoint2(Resource):
    '''
    Endpoint con acceso a Mongo
    '''
    #@Auth.test_user
    @Auth.authenticate
    @pymongo_access
    def get(self):
        mydb = g.db
        qry = {"client": session["user"]["bdName"]}
        data = mydb["info"].find_one(qry)
        return f'Cliente creado a las {data["creation_date"]}', 200

class EndPoint3(Resource):
    '''
    Endpoint con Keycloak y Mongo
    '''
    @Auth.authenticate
    @pymongo_access
    def get(self):
        mydb = g.db
        qry = {"client": session["user"]["bdName"]}
        data = mydb["info"].find(qry)
        return dumps(data), 200
