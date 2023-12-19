""" Se han importado 2 funciones """
from persistencia import guardar_pedido
from prueba import comprobacion

with open("pedidos.txt", "w", encoding="utf-8") as file:
    file.write("")
    file.close()

pedidos = [
    {"nombre": "Pedro", "apellidos": "Gil de Diego"},
    {"nombre": "Michael", "apellidos": "Jordan"}
]

for pedido in pedidos:
    NOMBRE = pedido["nombre"]
    APELLIDOS = pedido["apellidos"]

    guardar_pedido(NOMBRE, APELLIDOS)
    print(f"Pedido guardado: {NOMBRE} {APELLIDOS}")

    comprobacion(NOMBRE, APELLIDOS)
    print(f"Comprobación realizada: {NOMBRE} {APELLIDOS}")
    