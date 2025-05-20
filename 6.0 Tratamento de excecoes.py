# tratamento de exceção serve para, ao se deparar com algum erro, o programa não interrompa sua execução

""" 
    erros comuns:
        sintaxe (':', ',', espaçamento)
        nome (variável inexistente ou de outro escopo)
        tipo (3 + a)
        índice -> lista[1, 2, 3]
                    print (lista[3])
        divisão por zero
            
 """

def dividir (a, b):
    return a / b

# try -> bloco de execução inicial
# except -> bloco de tratamento de erro
# finally -> opcional, executa independete se houve tratamente de exceção ou não

try:
    resultado = dividir (5, 0)
    print (resultado)
except ZeroDivisionError:
    print ("Não pode dividir por zero")
except ValueError:
    print ("Valor invalido")


# cada bloco except lida com diferentes erros



try:
    arquivo = open("arquivo.txt", "r")
except FileNotFoundError:
    print("Erro: Arquivo não encontrado")
finally:
    arquivo.close()