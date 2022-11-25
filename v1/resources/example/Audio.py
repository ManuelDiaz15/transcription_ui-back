from flask_restful import Resource, reqparse
from flask import send_file, request

def ObtenerAudio():
    ruta = request.args.get("Ruta")
    return send_file("v1/Audios/"+ruta, mimetype="audio/mp3")
