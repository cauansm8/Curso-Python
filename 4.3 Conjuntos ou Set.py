
    # permite armazenar uma coleção de elementos únicos, delimitada por chaves 
    # criados usando a função set()
    # operações -> são as mesmas operações de conjuntos na matemática (união, intersecção, diferença, diferença simétrica)
    #                                                                    |         &          -            ^ 

numeros = set([1, 2, 3, 4, 5])

conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}

# metodos dos conjuntos

print ("União: ", conjunto1 | conjunto2)
print ("Intersecção: ", conjunto1 & conjunto2)
print ("Diferença: ", conjunto1 - conjunto2)
print ("Diferença: ", conjunto2 - conjunto1)
print ("Diferença simétrica: ", conjunto1 ^ conjunto2)


print ()

# outros métodos
    # add()
    # remove() -> se não encontrar o elemento, gera erro
    # discard() -> remove se encontrar o elemento, caso contrário, não faz nada
    # clear() -> limpa o conjunto - remove all

frutas = {"maçã", "banana", "laranja"}
frutas.add("pera")
print (frutas)

frutas.remove ("maçã")
print (frutas)

frutas.discard("uvas")
print (frutas)

frutas.clear()
print (frutas)  # -> set() significa NULL