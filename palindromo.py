"""Confirmar si una palabra es un palindromo"""
palabra=input("Escriba una palabra:  ")

ini=0
fin=len(palabra)-1


while ini < fin:
    if palabra[ini] == palabra[fin]:
        ini+= 1
        fin-= 1
        validacion=palabra + " es Palindromo"
    else: 
        validacion=palabra + " No es Palindromo"
        break

print(validacion)






