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
    resultado = dividir (5, 2)
    print (resultado)
except ZeroDivisionError:
    print ("Não pode dividir por zero")
except ValueError:
    print ("Valor invalido")


# cada bloco except lida com diferentes erros


"""  
    try:
        arquivo = open("arquivo.txt", "r")
    except FileNotFoundError:
        print("Erro: Arquivo não encontrado")
    finally:
        arquivo.close()

"""



# é possível criar as próprias exceções personalizadas!

def funcao(a):
    # Código que pode gerar uma exceção personalizada
    if a < 10:
        raise Exception("Número menor que 10")


try:
    funcao(5)
except Exception as e:
    print(f"Erro: {str(e)}")


# aqui, passamos um valor como parâmetro -> é utilizada para acessar a descrição do erro
# se a condição for verdade (valor < 10 == true) -> o tratamento de erro mostra a mensagem definida na função
# A classe exception cria o tratamento da exceção
# e -> classe que herda a classe Exception