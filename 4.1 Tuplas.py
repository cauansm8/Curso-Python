
    # Tuplas -> permite armazenar uma coleção de elementos e são encerrados por parênteses 
    #        -> são imutáveis (não é possível add, remover ou alterar após a criação)


ponto = (3, 4)

print (ponto)
print ("Ponto 0: ", ponto[0])
print ("Ponto 1: ", ponto[1])

print ("\n")

nome, idade, cidade = ("João", 30, "São Paulo")
print (nome)
print (idade)
print (cidade)

print ("\n")

# métodos para trabalhar com tupla:

minha_tupla = (1, 2, 3, 2, 4, 2)

print ("Quantas vezes o elemento 2 apareceu na tupla: ", minha_tupla.count(2))
    # count -> conta quantas vezes um elemento apareceu na tupla

print ("Index da primeira aparição de 2: ", minha_tupla.index(2))
    # index -> retorna o index da primeira aparição de algum elemento
print ("Index da terceira aparição de 2: ", minha_tupla.index(2, 4))
        # é possivel verificar as demais aparições
        # escolhe o número e depois a índice de start

print ("Tamanho da tupla: ", len(minha_tupla))
    # len -> retorna o tamanho da tupla


print ("\n")

# funções que retornam tuplas: enumerate e zip


nomes = ["Ana", "Bruno", "Carlos"]
for i, nome in enumerate(nomes):
    print(f"{i}: {nome}")

idades = [25, 30, 35]
for nome, idade in zip(nomes, idades):
    print(f"{nome} tem {idade} anos.")

# a função zip serve para agrupar elementos diferentes -> na função acima, zip agrupou as duas listas

print ("\n")