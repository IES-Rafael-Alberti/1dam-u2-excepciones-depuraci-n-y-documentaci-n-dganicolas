
def lista(a):
    """ ordena la lista """
    total = len(a)
    numero = 0
    for i in range(0, len(a)):
        for j in range(0, total - 1):
            if a[numero] > a[numero +1]:
                A = a[rango]
                a[numero] = a[numero + 1]
                a[numero + 1] = A
            rango += 1
        total -= 1
    return a

def main():
    a = [8, 3, 1, 19, 14]
    print(lista(a))

if __name__ == "main":
    main()