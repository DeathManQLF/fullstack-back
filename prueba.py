""" Desde persistencia se hace un 
import de la funcion guardar_pedido """
from persistencia import guardar_pedido

def comprobacion(nombre,apellidos):
    """ Comprueba sin funciona correctamente el guardado """
    guardado = guardar_pedido(nombre, apellidos)
    if guardado == "":
        print("La funcion de persistencia 'guardar_pedido' no funciona")
    else:
        print(f"La función de persistencia 'guardar_pedido' está funcionando. 
                Se ha escrito en el archivo pedidos: {nombre} {apellidos}")
