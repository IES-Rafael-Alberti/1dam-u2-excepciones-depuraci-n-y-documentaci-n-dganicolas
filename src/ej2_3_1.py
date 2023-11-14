#Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
def frase_edades(edad):
    edad= "\n"+ "has cumplido " +str(edad) + " años."
    return edad

def pregunta_edad():
    
        años= input("dime tu edad: ")
        años =int(años)
        return años
def edades (edad):
    edad = edad
    edad_texto = 1
    serie_edad= "has cumplido " +str(edad_texto) + " años."
    cont=1
    if edad < 0:
        raise ValueError ("Illo edad negativa no, churra")
    while cont < edad:
        edad_texto+=1
        serie_edad+=frase_edades(edad_texto)
        cont+=1
    return(serie_edad)
    

def main():
    try:
        años = pregunta_edad()
        print(edades(años))
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()