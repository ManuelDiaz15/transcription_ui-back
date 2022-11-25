'''
API de ejemplo
'''
from os import getenv

from dotenv import load_dotenv
from flask_restful import Api #importamos la libreria para crear recursos REST
from flask_cors import CORS #biblioteca para configurar cors
from config import app #de aqui se obtienen configuraciones
from v1.resources.routes import initialize_routes, inicializarURL #importamos las rutas

from flask import send_file, request
from v1.resources.auth.authorization import Auth 

# Flask restful con errores personalizados
CORS(app) #configuramos cors
api = Api(app) #instanciamos el api
load_dotenv()

#@app.route('/audio', methods=['GET'], endpoint="auth:TR_CRUD:5")

#def get():
#    ruta = request.args.get("Ruta")
#    print(ruta)
#    return send_file("v1/Audios/"+ruta, mimetype="audio/mp3")



initialize_routes(api) #inicializamos las rutas
inicializarURL(app)
#app.add_url_rule("/audio", endpoint="auth:TR_CRUD:5", view_func=get, methods=['GET'])

if __name__ == '__main__':
    # inicializamos el servidor flask con el puerto 4043
    # (este puerto debe ser cambiado al momento de probar en maquina de desarrollo)
    app.run(host=getenv("APP_HOST"), port=getenv("APP_PORT"), debug=True)
