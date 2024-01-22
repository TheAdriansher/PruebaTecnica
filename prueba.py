def es_polindrome(n):

    #Convertir numero a cadena    
    numero = str(n)

    # Recorrer la cadena
    for i in range(len(numero)//2):
        if numero[i] != numero[len(numero) - 1 - i]:
            return False
        return True
    
if __name__ == '__main__':
    n = int(input("Numero:"))

    print(es_polindrome(n))

