from flask import Flask, request, redirect

app = Flask(__name__)

@app.route("/pizza", methods=['POST'])
def formulario():
     nombre = request.form.get("nombre")
     apellido = request.form.get("apellido")
     print(nombre, apellido)
     return redirect("http://localhost/PizzaFullStackRelease/FrontEnd/solicita_pedido.html", code=302)