
# For é melhor para iterar sobre uma sequência (lista, tupla, string, vetor, ...) -> para números, o incremento é automático
# While faz o loop enquanto a condição for verdadeira - se a condição nunca for falsa -> loop infinito

    # Break serve para interromper o fluxo do loop
    # Continue pula o restante do bloco para a próxima iteração
    # Pass serve para criar um bloco vazio -> útil para reservar bloco de código que será implementado depois


frutas = ["macã", "banana", "laraja"]

for fruta in frutas: 
    print (fruta)
    # serve para passar cada string do vetor de string 'frutas' a string 'fruta
    # e dps printa

print ("For: ")
for i in range (10):
    if i == 5:
        break # fim do for
    print (i)

print ("While: ")

contador = 0
while contador < 10:
    print (contador)
    contador += 1

print ("Imprimindo somente numeros impares: ")
for i in range (10):
    if i % 2 == 0:
        continue # pula para a próxima iteração
    print (i)

for i in range (5):
    pass

print ("Printando em uma ordem sem começar pelo zero:")
for i in range (5, 10):
    print (i)