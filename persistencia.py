""" Funcion que guarda el nombre y el apellido """
def guardar_pedido(NOMBRE, APELLIDOS):
    """ Guarda nombre y apellido """
    with open("pedidos.txt", "a", encoding="utf-8") as file:
        file.write(f"{NOMBRE} {APELLIDOS}\n")
