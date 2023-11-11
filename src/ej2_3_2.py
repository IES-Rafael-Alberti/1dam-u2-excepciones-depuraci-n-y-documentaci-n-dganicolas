#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
def parimpar (num1):
    serie = ""
    if num1 < 0:
        raise ValueError ("Illo numero negativo no, churra")
    for i in range(1,num1+1,2):
        if i < num1-1:
            serie+= str(i) + ","
        if i == num1 -1 or num1 == i:
            serie+= str(i)
    return serie

def main():
    try:
        numero1=int(input("dame un numero: "))
        print(parimpar(numero1))
    except ValueError as e:
        print(e)
if __name__ == "__main__":
    main()