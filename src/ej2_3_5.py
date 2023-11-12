#Escribir que solicite una contraseña, y si no coincide con la que se tiene, lance la excepción NameError con el mensaje, "Incorrect Password!!"
def linea (numero):
    """comprueba si la contraseña es correcta"""
    contrasena="contraseña"
    if numero == contrasena:
        print ("bien hecho")
    else:
        raise NameError ("incorrect pasword!!!")        

def main():
    try:
        entrada = input("dame una contraseña\n")
        linea(entrada)
    except NameError as e:
        print(e)
if __name__ == "__main__":
    main()