from flask import Flask

app = Flask(__name__)
app.config.from_object('config')
app.config['SECRET_KEY'] = 'secret'

# Importe seus módulos e views aqui
from app.controllers import default
from app.controllers import apontamentocontroller
