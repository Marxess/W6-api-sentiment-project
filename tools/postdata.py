from config.configuration import db, collection

def insertmensaje(temp, numero, titulo, personaje, frase):
    """
    función que inserta los datos en mongo es el momento de revisar que todos los datos esten como queramos. 
    Eso os lo dejo a vosotras. Pero tenedlo en cuenta"""

    dict_insert = { 'Season' : f'{temp}',
    'Episode' : f'{numero}',
    'Episode Title': f'{titulo}',
    'Name' : f'{personaje}', 
    'Sentence': f'{frase}'
    }
    collection.insert_one(dict_insert)
