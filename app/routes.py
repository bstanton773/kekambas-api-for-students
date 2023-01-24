from app import app
from app.models import Kekambas
from flask import jsonify

@app.route('/')
def index():
    return 'Hello World'

@app.route('/kekambas')
def kekambas():
    return [k.to_dict() for k in Kekambas.query.all()]
    