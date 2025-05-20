
# Lista -> permite armazenar coleção de elementos e são encerrados por colchetes
#       -> o tamanho é dinâmico
frutas = ["maçã", "banana", "laranja"]

print ("Ordem inicial: ")
print (frutas[0])
print (frutas[1])
print (frutas[2])

# Índice negativo -> faz o acesso ao contrário
print ("\nOrdem contrária: ")
print (frutas[-1])
print (frutas[-2])
print (frutas[-3])

# .apppend -> inserção no final
frutas.append("pera") 
print (frutas)

# .insert -> inserção na posição desejada
frutas.insert(1, "uva")
print (frutas)

# .remove -> remove a primeira aparição de algum elemento
frutas.remove ("laranja")
print (frutas)

# .pop -> remove e retorna o elemento da posição x
fruta_removida = frutas.pop(3)
print (fruta_removida)
print (frutas)

# .sort -> ordena os elementos em ordem ascendente(palavras) ou crescente (números)
frutas.sort()
print (frutas)

vetor = [1, 5, 2, -9, 6]
vetor.sort()
print (vetor)

# .reverse -> inverte a ordem dos elementos
frutas.reverse()
print (frutas)


# Listas de compreensão -> cria uma lista baseada em uma sequência já existente

numeros = [2, 3, 6, 8, 5, 4, 1]
pares_ao_quadrado = [x ** 2 for x in numeros if x % 2 == 0]
print (numeros)
print (pares_ao_quadrado)

    # nesse caso, a segunda lista pega cada elemento de 'numeros', verifica se é par e, se for, eleva ao quadrado