from array import array
from datetime import date
import json
import logging
from multiprocessing.sharedctypes import Array
from tokenize import Double, Double3
#import terceros

import sys
from flask import session, jsonify
from flask_restful import Resource, reqparse
from mongoengine.context_managers import switch_db
from bson import ObjectId
#Import del sistema
from v1.resources.auth.authorization import Auth
from v1.resources.auth.dbDecorator import dbAccess
from types import *
import pymongo
from mongoengine.fields import ListField
from mongoengine.fields import StringField

logger = logging.getLogger(__name__)

#Import del sistema
from v1.models.api_models import Transcripciones_Originales

class Transcripciones_origin(Resource):

    @Auth.authenticate
    @dbAccess.mongoEngineAccess
    def put(self): #Se ejecutara este metodo con el metodo post del endpoint
        parser = reqparse.RequestParser() #creamos un objeto para obtener los datos de la request
        parser.add_argument("AudioNombre", type=str, required=True, help="Se ingreso mal el AudioNombre")
        parser.add_argument("AudioRuta", type=str, required=True, help="Se ingreso mal el AudioRuta")
        parser.add_argument("ArchicMetadata", type=str, required=True, help="Se ingreso mal el ArchicMetadata")
        parser.add_argument("Estado", type=str, required=True, help="Se ingreso mal el Estado")
        parser.add_argument("Campania", type=str, required=True, help="Se ingreso mal el Campania")
        parser.add_argument("Cliente", type=str, required=True, help="Se ingreso mal el Estado")
        parser.add_argument("Fecha", type=str, required=True, help="Se ingreso mal el Fecha")
        parser.add_argument("FechaTranscripcion", type=str, required=True, help="Se ingreso mal el FechaTranscripcion")
        parser.add_argument("HoraTranscripcion", type=str, required=True, help="Se ingreso mal el HoraTranscripcion")
        parser.add_argument("MT_DNIS", type=str, required=True, help="Se ingreso mal el MT_DNIS")
        parser.add_argument("MT_Destinatario", type=str, required=True, help="Se ingreso mal el MT_Destinatario")
        parser.add_argument("MT_DireccionLLamada", type=str, required=True, help="Se ingreso mal el MT_DireccionLLamada")
        parser.add_argument("MT_Ejecutivo", type=str, required=True, help="Se ingreso mal el MT_Ejecutivo")
        parser.add_argument("MT_FechaLlamada", type=str, required=True, help="Se ingreso mal el MT_FechaLlamada")
        parser.add_argument("MT_Folio", type=str, required=True, help="Se ingreso mal el MT_Folio")
        parser.add_argument("MT_IDScript", type=str, required=True, help="Se ingreso mal el MT_IDScript")
        parser.add_argument("MT_MotivoMora", type=str, required=True, help="Se ingreso mal el MT_MotivoMora")
        parser.add_argument("MT_NombreAudio", type=str, required=True, help="Se ingreso mal el MT_NombreAudio")
        parser.add_argument("MT_NombreScript", type=str, required=True, help="Se ingreso mal el MT_NombreScript")
        parser.add_argument("MT_RutDestinatario", type=str, required=True, help="Se ingreso mal el MT_RutDestinatario")
        parser.add_argument("MT_TiempoLLamado", type=str, required=True, help="Se ingreso mal el MT_TiempoLLamado")
        parser.add_argument("MT_TipoLlamadaCodigo", type=str, required=True, help="Se ingreso mal el MT_TipoLlamadaCodigo")
        parser.add_argument("MT_TipoLlamadaNombre", type=str, required=True, help="Se ingreso mal el MT_TipoLlamadaNombre")
        parser.add_argument("MT_UnidadNegocio", type=str, required=True, help="Se ingreso mal el MT_UnidadNegocio")
        parser.add_argument("TiempoAudio", type=float, required=True, help="Se ingreso mal el TiempoAudio")
        parser.add_argument("TiempoSilencio", type=float, required=True, help="Se ingreso mal el TiempoSilencio")
        parser.add_argument("Agent_spk", type=int, required=True, help="Se ingreso mal el Agent_spk")
        parser.add_argument("Confidence", type=float, required=True, help="Se ingreso mal el Confidence")
        parser.add_argument("TranscritoChat", type=str, required=True, help="Se ingreso mal el TranscritoChat")
        parser.add_argument("MotivoMoraCX", type=str, required=True, help="Se ingreso mal el MotivoMoraCX")
        data = parser.parse_args() #obtenemos los datos de la request

        try:
            with switch_db(Transcripciones_Originales, session["dbMongoEngine"]) as my_collection:
                my_model = my_collection(
                    AudioNombre=data['AudioNombre'], 
                    AudioRuta=data['AudioRuta'],
                    ArchicMetadata=data['ArchicMetadata'],
                    Estado=data['Estado'],
                    Campania=data['Campania'],
                    Cliente=data['Cliente'],
                    Fecha=data['Fecha'],
                    FechaTranscripcion=data['FechaTranscripcion'],
                    HoraTranscripcion=data['HoraTranscripcion'],
                    MT_DNIS=data['MT_DNIS'],
                    MT_Destinatario=data['MT_Destinatario'],
                    MT_DireccionLLamada=data['MT_DireccionLLamada'],
                    MT_Ejecutivo=data['MT_Ejecutivo'],
                    MT_FechaLlamada=data['MT_FechaLlamada'],
                    MT_Folio=data['MT_Folio'],
                    MT_IDScript=data['MT_IDScript'],
                    MT_MotivoMora=data['MT_MotivoMora'],
                    MT_NombreAudio=data['MT_NombreAudio'],
                    MT_NombreScript=data['MT_NombreScript'],
                    MT_RutDestinatario=data['MT_RutDestinatario'],
                    MT_TiempoLLamado=data['MT_TiempoLLamado'],
                    MT_TipoLlamadaCodigo=data['MT_TipoLlamadaCodigo'],
                    MT_TipoLlamadaNombre=data['MT_TipoLlamadaNombre'],
                    MT_UnidadNegocio=data['MT_UnidadNegocio'],
                    TiempoAudio=data['TiempoAudio'],
                    TiempoSilencio=data['TiempoSilencio'],
                    Agent_spk=data['Agent_spk'],
                    Confidence=data['Confidence'],
                    TranscritoChat=data['TranscritoChat'],
                    MotivoMoraCX=data['MotivoMoraCX'],
                    )
                my_model.save()
        except Exception as err:
            logger.error(err)
        return jsonify(my_model.to_json())
    
    @Auth.authenticate
    @dbAccess.mongoEngineAccess
    def post(self): #Se ejecutara este metodo con el metodo post del endpoint
        parser = reqparse.RequestParser() #creamos un objeto para obtener los datos de la request
        parser.add_argument("AudioNombre", type=str, required=True, help="Se ingreso mal el AudioNombre")
        parser.add_argument("AudioRuta", type=str, required=True, help="Se ingreso mal el AudioRuta")
        parser.add_argument("ArchicMetadata", type=str, required=True, help="Se ingreso mal el ArchicMetadata")
        parser.add_argument("Estado", type=str, required=True, help="Se ingreso mal el Estado")
        parser.add_argument("Campania", type=str, required=True, help="Se ingreso mal el Campania")
        parser.add_argument("Cliente", type=str, required=True, help="Se ingreso mal el Estado")
        parser.add_argument("Fecha", type=str, required=True, help="Se ingreso mal el Fecha")
        parser.add_argument("FechaTranscripcion", type=str, required=True, help="Se ingreso mal el FechaTranscripcion")
        parser.add_argument("HoraTranscripcion", type=str, required=True, help="Se ingreso mal el HoraTranscripcion")
        parser.add_argument("MT_DNIS", type=str, required=True, help="Se ingreso mal el MT_DNIS")
        parser.add_argument("MT_Destinatario", type=str, required=True, help="Se ingreso mal el MT_Destinatario")
        parser.add_argument("MT_DireccionLLamada", type=str, required=True, help="Se ingreso mal el MT_DireccionLLamada")
        parser.add_argument("MT_Ejecutivo", type=str, required=True, help="Se ingreso mal el MT_Ejecutivo")
        parser.add_argument("MT_FechaLlamada", type=str, required=True, help="Se ingreso mal el MT_FechaLlamada")
        parser.add_argument("MT_Folio", type=str, required=True, help="Se ingreso mal el MT_Folio")
        parser.add_argument("MT_IDScript", type=str, required=True, help="Se ingreso mal el MT_IDScript")
        parser.add_argument("MT_MotivoMora", type=str, required=True, help="Se ingreso mal el MT_MotivoMora")
        parser.add_argument("MT_NombreAudio", type=str, required=True, help="Se ingreso mal el MT_NombreAudio")
        parser.add_argument("MT_NombreScript", type=str, required=True, help="Se ingreso mal el MT_NombreScript")
        parser.add_argument("MT_RutDestinatario", type=str, required=True, help="Se ingreso mal el MT_RutDestinatario")
        parser.add_argument("MT_TiempoLLamado", type=str, required=True, help="Se ingreso mal el MT_TiempoLLamado")
        parser.add_argument("MT_TipoLlamadaCodigo", type=str, required=True, help="Se ingreso mal el MT_TipoLlamadaCodigo")
        parser.add_argument("MT_TipoLlamadaNombre", type=str, required=True, help="Se ingreso mal el MT_TipoLlamadaNombre")
        parser.add_argument("MT_UnidadNegocio", type=str, required=True, help="Se ingreso mal el MT_UnidadNegocio")
        parser.add_argument("TiempoAudio", type=float, required=True, help="Se ingreso mal el TiempoAudio")
        parser.add_argument("TiempoSilencio", type=float, required=True, help="Se ingreso mal el TiempoSilencio")
        parser.add_argument("Agent_spk", type=int, required=True, help="Se ingreso mal el Agent_spk")
        parser.add_argument("Confidence", type=float, required=True, help="Se ingreso mal el Confidence")
        parser.add_argument("TranscritoChat", type=str, required=True, help="Se ingreso mal el TranscritoChat")
        parser.add_argument("MotivoMoraCX", type=str, required=True, help="Se ingreso mal el MotivoMoraCX")
        data = parser.parse_args() #obtenemos los datos de la request

        with switch_db(Transcripciones_Originales, session["dbMongoEngine"]):
            my_model = Transcripciones_Originales.objects(AudioNombre=data['AudioNombre']).first()
            my_model.AudioRuta = data['AudioRuta']
            my_model.ArchicMetadata = data['ArchicMetadata']
            my_model.Estado = data['Estado']
            my_model.Campania = data['Campania']
            my_model.Cliente = data['Cliente']
            my_model.Fecha = data['Fecha']
            my_model.FechaTranscripcion = data['FechaTranscripcion']
            my_model.HoraTranscripcion = data['HoraTranscripcion']
            my_model.MT_DNIS = data['MT_DNIS']
            my_model.MT_Destinatario = data['MT_Destinatario']
            my_model.MT_DireccionLLamada = data['MT_DireccionLLamada']
            my_model.MT_Ejecutivo = data['MT_Ejecutivo']
            my_model.MT_FechaLlamada = data['MT_FechaLlamada']
            my_model.MT_Folio = data['MT_Folio']
            my_model.MT_IDScript = data['MT_IDScript']
            my_model.MT_MotivoMora = data['MT_MotivoMora']
            my_model.MT_NombreAudio = data['MT_NombreAudio']
            my_model.MT_NombreScript = data['MT_NombreScript']
            my_model.MT_RutDestinatario = data['MT_RutDestinatario']
            my_model.MT_TiempoLLamado = data['MT_TiempoLLamado']
            my_model.MT_TipoLlamadaCodigo = data['MT_TipoLlamadaCodigo']
            my_model.MT_TipoLlamadaNombre = data['MT_TipoLlamadaNombre']
            my_model.MT_UnidadNegocio = data['MT_UnidadNegocio']
            my_model.TiempoAudio = data['TiempoAudio']
            my_model.TiempoSilencio = data['TiempoSilencio']
            my_model.Agent_spk = data['Agent_spk']
            my_model.Confidence = data['Confidence']
            my_model.TranscritoChat = data['TranscritoChat']
            my_model.MotivoMoraCX = data['MotivoMoraCX']
            my_model.save()
        return jsonify(my_model.to_json())
    
    @Auth.authenticate
    @dbAccess.mongoEngineAccess
    def get(self):
        #print('Hello world!', file=sys.stderr)
        with switch_db(Transcripciones_Originales, session["dbMongoEngine"]):
            my_model = Transcripciones_Originales.objects.fields(id=0,AudioNombre=1, Confidence=1, Campania=1, MT_Ejecutivo=1, Cliente=1)
            if my_model:
                return jsonify(my_model.to_json())
        return "Objeto no encontrado", 400

class Coreccion (Resource):
    @Auth.authenticate
    @dbAccess.mongoEngineAccess
    def post(self):
        parser = reqparse.RequestParser() #creamos un objeto para obtener los datos de la request
        parser.add_argument("AudioNombre", help="Mensaje que devolvera en caso de parametro mal ingresado")
        data = parser.parse_args() #obtenemos los datos de la request

        with switch_db(Transcripciones_Originales, session["dbMongoEngine"]):
            #my_model = Transcripciones_Originales.objects(id=ObjectId(data["ID"])).fields(TranscritoChat=1, id=0).first()// {"ID":"633350996ce3123a75f707d8"} para el thinder client body
            my_model = Transcripciones_Originales.objects(AudioNombre=data["AudioNombre"]).fields(TranscritoChat=1, id=0).first() #// {"Audionombre":"FALRESP_20220910-125556_56953670812_485_175459783-all.mp3"} para el thinder client body
            #my_model = Transcripciones_Originales.objects(AudioNombre="FALRESP_20220910-125556_56953670812_485_175459783-all.mp3").fields(TranscritoChat=1, id=0)
            if my_model:
                return  jsonify(my_model["TranscritoChat"])
        return "Objeto no encontrado", 400
    

class Listado (Resource):
    @Auth.authenticate
    @dbAccess.mongoEngineAccess
    def get(self):
        parser = reqparse.RequestParser() #creamos un objeto para obtener los datos de la request
        parser.add_argument("AudioNombre", type=str, required=True, help="Se ingreso mal el AudioNombre")
        data = parser.parse_args() #obtenemos los datos de la request

        with switch_db(Transcripciones_Originales, session["dbMongoEngine"]):
            my_model = Transcripciones_Originales.objects(AudioNombre=data["AudioNombre"]).first()
            if my_model:
                return jsonify(my_model.to_json())
        return "Objeto no encontrado", 400
