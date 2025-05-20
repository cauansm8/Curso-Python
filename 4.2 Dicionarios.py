
    # Dicionário -> permite armazenar elementos pares e alterar quando quiser, são separados por chaves
    
        # (colunas) (conteúdo)
        #  keys     values
pessoa = {"nome": "Cauan", 
          "idade": "19", 
          "cidade": "Prudente"}

        # item -> junção de tudo: (keys, values)



print (pessoa)

print (pessoa["nome"])
print (pessoa["idade"])
print (pessoa["cidade"])

print ()

# métodos de dicionários

print (pessoa.keys())
print (pessoa.values())
print (pessoa.items())

print ()


pessoa.update({"profissão": "estudante"})
print (pessoa.items())
    # atualiza o dicionário