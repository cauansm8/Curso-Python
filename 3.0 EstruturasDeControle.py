""" 
    Operadores lógicos

    operação    comando
      AND         and
      OR           or
      NOT         not

"""

a = 5
b = 3

if a > b:
    print ("A maior que B")

elif a < b:
    print ("A menor que B")

else:
    print("A igual a B") 
    


if (a>b) and (a % 2 == 0):
    print ("A maior que B e A é par")

if (a % 2 == 0) or (b % 2 == 0):
    print ("A ou B são pares")

else:
    print ("não há valores pares")
