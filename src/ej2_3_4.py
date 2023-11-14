#Escribir un programa que pida al usuario un número entero, si la entrada no es correcta, mostrará el mensaje "La entrada no es correcta" y lanzará la excepción capturada.
def linea (numero):
    """convierte el input en numero entero"""
    numero = int(numero)
def main():
    try:
        entrada = input("dame un numero\n")
        linea(entrada)
    except ValueError as e:
        print(e)
if __name__ == "__main__":
    main()