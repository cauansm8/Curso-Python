# leitura e escrita de arquivos funciona igual em C
    # r -> abre em modo leitura
    # w -> abre em modo escrita -> se não existir, ele é criado
    #                           -> se existir, o conteúdo é sobrescrito


# em C é 'fopen()', 'fclose()'
# em Python é 'open()', 'close()'
    # fechar o arquivo libera os recursos do sistema


arquivo = open("dados.txt", "r")

# lê o arquivo inteiro
conteudo = arquivo.read()
print (conteudo)

# fecha o arquivo
arquivo.close()


arquivo = open("dados.txt", "w")

# sobrescreve o conteúdo
arquivo.write("Inserindo informacoes no arquivo")

# fecha o arquivo
arquivo.close()


# para não ter problemas por esquecer do close(), pode-se usar o with

with open ("dados.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print (conteudo)

# o close() é automático quando sai do bloco!