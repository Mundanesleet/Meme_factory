# Importar
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


app.run(debug=True)



'''
# Comando para crear rama
'git branch nombre-de-la-rama'

#Para ver ramas existentes y en la cual se encuentran
'git branch'

#Crear una rama y pasar a ella directamente
'git checkout -b nombre-de-la-rama'

#Para cambiar entre ramas
'git checkout nombre-de-rama-existente'
'''