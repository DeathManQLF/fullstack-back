""" Flask APP """
from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    """ Ruta pagina Index """
    return 'Index Page'

@app.route('/pizza', methods=['POST'])
def pizza():
    """ Ruta pagina Pizza """
    NOMBRE = request.form.get('nombre')
    APELLIDOS = request.form.get('apellidos') 

    print("Nombre:", NOMBRE)
    print("Apellidos:", APELLIDOS)

    return redirect("http://localhost/solicita_pedido.html", code=302)
