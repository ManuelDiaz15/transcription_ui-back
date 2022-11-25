from mongoengine import Document, DynamicDocument
from mongoengine import StringField, IntField, DateField, FloatField, ListField



class Model1(Document):
    name = StringField(max_length=30, required=True)
    number = IntField()

    def hello(self):
        return f"Hola {self.name}"


class Model2(DynamicDocument):
    meta = {'collection': 'model2'}

class Transcripciones_Originales(DynamicDocument):
    meta = {'collection': 'Transcripciones_Originales'}

class Transcripciones_Modificadas(DynamicDocument):
    meta = {'collection': 'Transcripciones_Modificadas'}
