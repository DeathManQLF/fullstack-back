from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/pizza', methods=['POST'])
def pizza():

    nombre = request.form.get('nombre')
    apellidos = request.form.get('apellidos') 

    print("Nombre:", nombre)
    print("Apellidos:", apellidos)

    return redirect("http://localhost/solicita_pedido.html", code=302)


