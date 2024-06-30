def creaCifrador(d: int):
    alfabeto = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ '
    longitud_alfabeto = len(alfabeto)

    
    def cifrar(mensaje: str) -> str:
        mensaje_cifrado = ""
        for letra in mensaje:
            if letra in alfabeto:
                indice_actual = alfabeto.index(letra)
                nuevo_indice = (indice_actual + d) % longitud_alfabeto
                mensaje_cifrado += alfabeto[nuevo_indice]
            else:
                mensaje_cifrado += letra  # Por si hay caracteres que no están en el alfabeto
        return mensaje_cifrado
    
    return cifrar


