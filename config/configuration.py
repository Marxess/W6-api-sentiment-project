import os
import dotenv
from pymongo import MongoClient

dotenv.load_dotenv()

DBURL = os.getenv('URL')

#Vamos a conectar con la base de datos de Mongo en local
if not (DBURL):
    raise ValueError('Tienes que especificar la URL pls')


client = MongoClient(DBURL)
db = client.get_database()
collection = db['frases'] 


