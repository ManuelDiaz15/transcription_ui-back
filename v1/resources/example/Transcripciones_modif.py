from array import array
from datetime import date
import json
import logging
from multiprocessing.sharedctypes import Array
from tokenize import Double, Double3
#import terceros
from flask import session, jsonify
from flask_restful import Resource, reqparse
from mongoengine.context_managers import switch_db
from bson import ObjectId
#Import del sistema
from v1.resources.auth.authorization import Auth
from v1.resources.auth.dbDecorator import dbAccess
from types import *
import pymongo

logger = logging.getLogger(__name__)
from mongoengine.fields import ListField
from mongoengine.fields import StringField
#Import del sistema
from v1.models.api_models import Transcripciones_Modificadas, Transcripciones_Originales

class Transcripciones_Modif(Resource):
    @Auth.authenticate
    @dbAccess.mongoEngineAccess
    def post(self): #Se ejecutara este metodo con el metodo post del endpoint

        parser = reqparse.RequestParser() #creamos un objeto para obtener los datos de la request
        parser.add_argument("AudioNombre", type=str,  help="Se ingreso mal el AudioNombre")
        parser.add_argument("TranscritoChat",type=dict, action="append", help="Se ingreso mal el TranscritoChat")
        data = parser.parse_args() #obtenemos los datos de la request
        with switch_db(Transcripciones_Originales, session["dbMongoEngine"]) as col:
            db = Transcripciones_Originales.objects(AudioNombre=data['AudioNombre']).first()
        try:
            with switch_db(Transcripciones_Modificadas, session["dbMongoEngine"]) as my_collection:
                my_model = my_collection(
                    AudioNombre=db["AudioNombre"], 
                    AudioRuta=db['AudioRuta'],
                    ArchicMetadata=db['ArchicMetadata'],
                    Estado=db['Estado'],
                    Campania=db['Campania'],
                    Cliente=db['Cliente'],
                    Fecha=db['Fecha'],
                    FechaTranscripcion=db['FechaTranscripcion'],
                    HoraTranscripcion=db['HoraTranscripcion'],
                    MT_DNIS=db['MT_DNIS'],
                    MT_Destinatario=db['MT_Destinatario'],
                    MT_DireccionLLamada=db['MT_DireccionLLamada'],
                    MT_Ejecutivo=db['MT_Ejecutivo'],
                    MT_FechaLlamada=db['MT_FechaLlamada'],
                    MT_Folio=db['MT_Folio'],
                    MT_IDScript=db['MT_IDScript'],
                    MT_MotivoMora=db['MT_MotivoMora'],
                    MT_NombreAudio=db['MT_NombreAudio'],
                    MT_NombreScript=db['MT_NombreScript'],
                    MT_RutDestinatario=db['MT_RutDestinatario'],
                    MT_TiempoLLamado=db['MT_TiempoLLamado'],
                    MT_TipoLlamadaCodigo=db['MT_TipoLlamadaCodigo'],
                    MT_TipoLlamadaNombre=db['MT_TipoLlamadaNombre'],
                    MT_UnidadNegocio=db['MT_UnidadNegocio'],
                    TiempoAudio=db['TiempoAudio'],
                    TiempoSilencio=db['TiempoSilencio'],
                    Agent_spk=db['Agent_spk'],
                    Confidence=db['Confidence'],
                    TranscritoChat=data['TranscritoChat'],
                    MotivoMoraCX=db['MotivoMoraCX']
                    )
                my_model.save()
        except Exception as err:
            logger.error(err)
        return jsonify(my_model.to_json())
    
    
    @Auth.authenticate
    @dbAccess.mongoEngineAccess
    def get(self):
        #print('Hello world!', file=sys.stderr)
        with switch_db(Transcripciones_Modificadas, session["dbMongoEngine"]):
            my_model = Transcripciones_Modificadas.objects.fields(id=0,AudioNombre=1, Confidence=1, Campania=1, MT_Ejecutivo=1, Cliente=1)
            if my_model:
                return jsonify(my_model.to_json())
        return "Objeto no encontrado", 400
