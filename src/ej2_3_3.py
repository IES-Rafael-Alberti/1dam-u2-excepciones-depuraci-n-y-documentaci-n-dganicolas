#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas. Deberá solicitar el número hasta introducir uno correcto.
def contador (num1):
    """devuelve una serie de numero de x a 0"""
    serie = str(num1)
    num1-=1
    if num1 < 0:
        raise ValueError ("Illo numero negativo no, churra")
    for i in range(num1,-1,-1):
        serie+= "," + str(i)
    return serie

def main():
    try:
        numero1=int(input("dame un numero: "))
        print(contador(numero1))
    except ValueError as e:
        print(e)
if __name__ == "__main__":
    main()