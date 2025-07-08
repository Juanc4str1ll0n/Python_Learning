def esPalindromo(dato):
    dato2 = str(dato)
    if(dato2 == dato2[::-1]):
       return True
    else:
        return False
    
print(esPalindromo(123321))