""" Pruebas Persistencia """

def test_guardar_pedido(firstline, secondline):
    """ Prueba general """
    with open("pedidos.txt", "w+", encoding="utf-8") as file:
        firstline = file.readline()
        secondline = file.readline()
        file.close()
        assert firstline == "-Pedro Gil de Diego\n"
        assert secondline == "-Michael Jordan\n"

test_guardar_pedido("Pedro", "Gil de Diego")
test_guardar_pedido("Pedro", "Gil de Diego")
