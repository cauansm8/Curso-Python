# interação com o usuário e com arquivos


# input -> obtém informações do usuário pelo terminal

nome = input ("Informe o seu nome: ")
idade = input ("Informe sua idade: ")


print (f"A pessoa '{nome}' tem {idade} anos")


# o input só arquiva STRING!!!!!
# para arquivar outros tipos de dados -> cast

try:
    idade = int(input("Informe sua idade: "))

    print (f"Idade informada: {idade}")

    if idade >= 18:
        print ("Maior de idade")
    
    else:
        print ("Menor de idade")

except:
    print ("Conteúdo informado não é valor inteiro")


# Saída de dados -> print()

# print ("", variavel1, variavel2, ....)
    # insere conteudo de variavel somente ao final do print

# print (f:"{variavel1}, {variavel2}, ....")
    # insere conteudo onde quiser -> indicado por {}
    # exemplo feito anteriormente: 
    #           print (f"A pessoa '{nome}' tem {idade} anos")
