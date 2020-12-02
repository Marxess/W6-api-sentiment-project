from config.configuration import db, collection
import pandas as pd

def mensajepersonaje(Name):
    """
    Hacemos una query a la base de datos para sacar las frases de un personaje
    """
    query = {'Name':f'{Name}'}
    #id set to 0 so that id from mongo is not shown
    frases = list(collection.find(query,{"_id":0, 'Season':0}))
    return frases

def distintospersonajes():
    """Funcion para obtener los personajes de nuestro dataset"""
    names = list(collection.distinct('Name'))
    return names

def mensajefamilia(familias):
    """Funcion para obtener los mensajes de una familia"""
    query = {'Name' : {'$regex' : '.*{Name}*'}}
    mensajes_familias = list(collection.find(query, {"_id":0, 'Season':0}))

#Functions to obtain polarity and subjectivity of a sentence
#TextBlob not used
def polarity(text):
    en_blob=TextBlob(u'{}'.format(text))
    translated = en_blob.translate(to='fr')
    return translated.sentiment[0]

def subjectivity(text):
    en_blob=TextBlob(u'{}'.format(text))
    translated = en_blob.translate(to='fr')
    return translated.sentiment[1]

def sentimentAnalysis(sentence):
    sia = SentimentIntensityAnalyzer()
    polarity = sia.polarity_scores(sentence)
    pol = polarity['compound']
    return pol

def analisispol(Name):
    query = {'Name': f'{Name}'}
    todos = list(collection.find(query, {'_id:0'}))
    todos['Polarity']= todos['Sentence'].apply(sentimentAnalysisis)
    datos = todos.groupby('Name')['Polarity'].mean()
    return datos

def analisissubjective(Name):
    query = {'Name': f'{Name}'}
    all = list(c.find(query, {'_id:0'}))
    all['Subjectivity']= all['Sentence'].apply(sentimentAnalysisis)
    data = todos.groupby('Name')['Subjectivity'].mean()
    return data
