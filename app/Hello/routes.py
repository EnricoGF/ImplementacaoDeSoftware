from flask import Blueprint

hello_bp = Blueprint('hello', __name__)
name_bp = Blueprint('name', __name__)

@hello_bp.route('/')
def index():
    return "Hello world"

@name_bp.route ('/sobre')
def index():
    return "Hello nome"