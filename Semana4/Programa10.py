"""
      Programa10
      Nombre: Marcos Eduardo I. H.
      Fecha: 09/02/2023 
      Descripcion: 
"""
def mayor(numero1:int,numero2:int)->int|None:
    result = None
    if numero1 > numero2:
        result = numero1
    elif numero2 > numero1:
        result = numero2
    return result
    
print()
print(mayor(8.2,5)) #8.2
print(mayor(3.5,5)) #5
print(mayor(10.2,5)) #10.2
print(mayor(3.5,7)) #7
print(mayor(9.2,8)) #9.2
print(mayor(5.9,5.9)) #None
print(mayor(3.3,9)) #9
print(mayor(4.2,6)) #6