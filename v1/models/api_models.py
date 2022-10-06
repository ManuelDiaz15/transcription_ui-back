from mongoengine import Document, DynamicDocument
from mongoengine import StringField, IntField



class Model1(Document):
    name = StringField(max_length=30, required=True)
    number = IntField()

    def hello(self):
        return f"Hola {self.name}"


class Model2(DynamicDocument):
    meta = {'collection': 'model2'}

class Model1(Document):
    name = StringField(max_length=30, required=True)
    number = IntField()

    def hello(self):
        return f"Hola {self.name}"


class Model2(DynamicDocument):
    meta = {'collection': 'model2'}

    
class Transcripcion (Document):
    hablante1 = StringField(max_length=30, required=True)
    hablante2 = StringField(max_length=30, required=True)
    compañia = StringField(max_length=30, required=True)
    porcentajeAcertividad = IntField()
    frace1 = StringField(max_length=30, required=True)
    frace2 = StringField(max_length=30, required=True)