""" Flask """
from flask import Flask, request, redirect, Response

app = Flask(__name__)

@app.route("/pizza", methods=['POST'])

def formulario():
    """ Redireccion de formulario """
    nombre = request.form.get("nombre")
    apellido = request.form.get("apellido")
    print(nombre, apellido)
    return redirect("http://localhost/PizzaFullStackRelease/FrontEnd/solicita_pedido.html",code=302)

@app.route("/checksize", methods=['POST'])
    
def checksize():
    """ Comprueba disponibilidad de un tamaño de pizza. """
    tamaño = request.form.get("tamaño")
    mensaje = 'Lo que corresponda'
    if (tamaño == 'M' or tamaño =='L' or tamaño =='XXL'):
        print("Pizza selecionada")
        return "Disponible"
    elif (tamaño == 'S'):
        return "No Disponible, " + mensaje

    return Response(mensaje, 200, {'Access-Control-Allow-Origin': '*'})
