def primo_palindromo(n):

    n = int(input("Numero: "))
    numero = n
    #Itera hasta encontrar un numero primo palindromo
    while not es_primo(numero) or not es_palindromo(numero):
        numero += 1

    return numero

def es_primo(n):
    #es primo si solo es divisible por si mismo y por 1
    if n <= 1:
        return False
    
    for i in range(2, int(n**0.5) + 1):
        if n%1 == 0:
            return False
        
    return True
    
def es_palindromo(n):

    #Convertir numero a cadena    
    numero = str(n)

    # Recorrer la cadena
    for i in range(len(numero)//2):
        if numero[i] != numero[len(numero) - 1 - i]:
            return False
        return True

