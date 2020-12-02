from flask import Flask, request
import markdown.extensions.fenced_code
import random
import json
import tools.getdata as get
import tools.postdata as pos
from textblob import TextBlob
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from textblob import TextBlob
import spacy
import pandas as pd



#Initializing app 
app = Flask(__name__)


@app.route('/')
def index():
    readme_file = open("README.md", "r")
    md_template_string = markdown.markdown(readme_file.read(), extensions = ['fenced_code'])
    return md_template_string


@app.route('/ejemplo1')
def datitos():
    diccionario = { 'Nombre' : 'Fer',
    'Amigos': ['Dobby', 'Ras', 'Sheriff', 'Ignacio'],
    'Edad' : 28
    }
    return diccionario
#GET ENDPOINTS
#parameter introduced to get the name of the character 
@app.route('/frases/<personaje>')
def frasepersonaje(personaje):
    frases = get.mensajepersonaje(personaje)
    return json.dumps(frases)
#function get personaje comes from tools

@app.route('/personajes')
def personajes_got():
    personajes = get.distintospersonajes()
    return json.dumps(personajes)

@app.route('/mensajes/<house>')
def familias_mensajes(house):
    mensajes = get.mensajefamilia(house)
    return json.dumps(mensajes)


#POST ENDPOINTS
@app.route('/nuevafrase', methods=['POST'])
def insertmensaje():
    temp = request.form.get('Season')
    numero = request.form.get('Episode')
    titulo = request.form.get('Episode Title')
    personaje = request.form.get('Name')
    frase = request.form.get('Sentence')
    pos.insertmensaje(temp, numero, titulo, personaje, frase)
    return 'Mensaje introducido correctamente en la base de datos'

#GET ENDPOINS - SENSIBILIDAD
@app.route('/polaridad/<Name>', methods=['GET'])
def analisispol(Name):
    Name = request.form.get('Name')
    polarity = get.analisispol(Name)
    return json.dumps(polarity)

@app.route('/subjetividad/<Name>', methods=['GET'])
def analisissub(Name):
    Name = request.form.get('Name')
    subjectivity = get.analisissubjective(Name)
    return json.dumps(subjetivity)



























app.run(debug=True)