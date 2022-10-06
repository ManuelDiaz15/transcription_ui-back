from os import getenv
from dotenv import load_dotenv
from flask import Flask #importamos la libreria flask


load_dotenv()

#=====================Configuraciones keycloak=====================#

################################Recordatorio#############################################
#   las configuraciones que puedan variar de ambiente en ambiente deben                 #
#   ser declaradas con variables de entorno.                                            #
#   Ejemplo:                                                                            #
#          import os                                                                    #
#          BdName = os.getenv('NombreVariableEntorno', 'valor_por_defecto')             #
#                                                                                       #
#   Ademas de estos las configuraciones en este archivo deben ocupar las variables      #
#   de configuraciones de flask.                                                        #
#   Ejemplo:                                                                            #
#           app.config['NombreVariableConfiguracion'] = 'valor_de_configuracion'        #
#                                                                                       #
#########################################################################################


AuthConfig = {
        "ClientID":str(getenv("KEYCLOAK_CLIENTID")), #cliente Keycloak que utilizara la aplicacion
        "ClientSecret":str(getenv("KEYCLOAK_CLIENTSECRET")),
        "UrlToken":str(getenv("KEYCLOAK_URLTOKEN")), #endpoint para obtener token
        "UrlInfo":str(getenv("KEYCLOAK_URLINFO")) #endpoint para obtener informacion de usuario
}

DbConfig = {
        "host":str(getenv("BD_HOST")), #ip de la base de datos principal de xentric
        "port":str(getenv("BD_PORT")), #puerto de la base de datos principal de xentric
        "user":str(getenv("BD_USER")), #usuario de la base de datos principal de xentric
        "pass":str(getenv("BD_PASS")),#contraseña de la base de datos principal de xentric
        "EncriptWord": str(getenv("ENCRIPTWORD")) #palabra clave para encriptacion y desencriptacion
}

app = Flask(__name__) #instanciamos la aplicacion
app.secret_key = getenv('FLASK_SECRET_KEY', 'secret_key') #le asignamos la clave secreta
app.config['AuthConfig'] = AuthConfig #asignamos la configuracion de keycloak a la aplicacion
app.config['DbConfig'] = DbConfig #asignamos la configuracion de base de datos a la aplicacion
