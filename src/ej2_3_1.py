#Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
def frase_edades(edad:str):
    try:
        edad= "\n"+ "has cumplido " +str(edad) + " años."
    except ValueError as e:
        if edad == str:
            print("La edad debe de ser un numero")
        else:
            print(e)
    return edad

def pregunta_edad():
    años= int(input("dime tu edad: "))
    return años
def edades (edad):
    edad_texto = 0
    serie_edad= "has cumplido " +str(edad_texto) + " años."
    cont=0
    while cont < edad:
        edad_texto+=1
        serie_edad+=frase_edades(edad_texto)
        cont+=1
    return(serie_edad)

def main():
    años = pregunta_edad()
    print(edades(años))

if __name__ == "__main__":
    main()