from persistencia import guardar_pedido

def comprobacion(nombre,apellidos):

    if guardar_pedido == "":
        print("La funcion de persistencia 'guardar_pedido' no funciona")
    else:
        print(f"La función de persistencia 'guardar_pedido' está funcionando. Se ha escrito en el archivo pedidos: {nombre} {apellidos}")


