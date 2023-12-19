""" Desde persistencia se hace un 
import de la funcion guardar_pedido """
from persistencia import guardar_pedido

def comprobacion(NOMBRE,APELLIDOS):
    """ Comprueba sin funciona correctamente el guardado """
    guardado = guardar_pedido(NOMBRE, APELLIDOS)
    if guardado == "":
        print("La funcion de persistencia 'guardar_pedido' no funciona")
    else:
        print(f"La función de persistencia 'guardar_pedido' está funcionando. "
                f"Se ha escrito en el archivo pedidos: {NOMBRE} {APELLIDOS}")

