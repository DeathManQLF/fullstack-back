""" Flask APP """
from flask import Flask, request, redirect, Response

app = Flask(__name__)

@app.route('/')
def index():
    """ Ruta pagina Index """
    return 'Index Page'

@app.route('/pizza', methods=['POST'])
def pizza():
    """ Ruta pagina Pizza """
    nombre = request.form.get("nombre")
    apellidos = request.form.get("apellidos")

    print("Nombre:", nombre)
    print("Apellidos:", apellidos)

    return redirect("http://localhost/solicita_pedido.html", code=302)

@app.route("/checksize",methods=['POST'])
def checksize():
    """ Comprueba disponibilidad de un tamaño de pizza. """
    tamano = request.form.get("size")
    if tamano == "S":
        mensaje = "No disponible"
    else:
        mensaje = "Disponible"

    return Response(mensaje, 200, {'Access-Control-Allow-Origin': '*'})
