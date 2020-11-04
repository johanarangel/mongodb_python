#! set/bin/env python
'''
SQL Introducción [Python]
Ejercicios de profundización
---------------------------
Autor: Johana Rangel
Version: 1.1

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Johana Rangel"
__email__ = "johanarang@hotmail.com"
__version__ = "1.1"

import tinymongo as tm
import tinydb
import json
import requests


class TinyMongoClient(tm.TinyMongoClient):
    @property
    def _storage(self):
        return tinydb.storages.JSONStorage


db_name = 'titulo'

def fetch():

    response = requests.get('https://jsonplaceholder.typicode.com/todos')
    
    data = json.loads(response.text)
    data = response.json()
    
    print(json.dumps(data, indent=4))
    return data


def clear():
    
    conn = TinyMongoClient()
    db = conn[db_name]

    db.title.remove({}) # Se eliminan todos los documentos que existan en la coleccion titulo.

    conn.close() # Cerrar la conexión con la DB


def fill(data):
    
    conn = TinyMongoClient()
    db = conn[db_name]

    title_insert = db.title.insert_many(data) 
    print(title_insert)
    
    conn.close()

def title_completed_count(userId):
    
    conn = TinyMongoClient()
    db = conn[db_name]

    count = db.title.find({"userId": userId}, {"completed": True}).count()
    print(count)

    conn.close()


if __name__ == "__main__":
    # Borrar DB
    clear()
    
    # Completar la DB con el JSON request
    data_info = fetch()
    fill(data_info)

    # Buscar titulos completados
    userId = 5
    title_completed_count(userId)