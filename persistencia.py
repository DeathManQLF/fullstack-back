""" Funcion que guarda el nombre y el apellido """
def guardar_pedido(nombre, apellidos):
    """ Guarda nombre y apellido """
    with open("pedidos.txt", "a", encoding="utf-8") as file:
        file.write(f"{nombre} {apellidos}\n")
