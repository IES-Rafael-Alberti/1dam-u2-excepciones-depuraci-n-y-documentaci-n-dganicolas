#Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
def frase_edades(edad):
    edad= "\n"+ "has cumplido " +str(edad) + " años."
    return edad

def pregunta_edad():
    
    try:
        años= input("dime tu edad: ")
    
        if años == str:
            print()
    except ValueError:
        print("La edad debe de ser un numero")
            
        años =int(años)
        return años
def edades (edad):
    edad = edad
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