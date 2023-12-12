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
    nombre = pedido["nombre"]
    apellidos = pedido["apellidos"]
        
    guardar_pedido(nombre, apellidos)
    print(f"Pedido guardado: {nombre} {apellidos}")

        
    comprobacion(nombre, apellidos)
    print(f"Comprobación realizada: {nombre} {apellidos}")