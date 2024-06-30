from funciones import suma_rara


def test_suma_numeros():
    resultado = suma_rara(2, 3)

    assert resultado == 8

def test_suma_cadenas():
    
    resultado = suma_rara("Hola", "Mundo")

    assert resultado == "HolaMundoMundo"

