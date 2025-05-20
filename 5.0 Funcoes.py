# def - define uma funcao nome + (parametros)



def saudacao(nome):
    print ("\n\nHello world")
    print (f"Ola, {nome}!")

saudacao ("cauan")


def somar (a,b):
    return a + b


resultado = somar (1, 5)
print (f"\nResultado: {resultado}")

# função lambda -> função curta, definidas em uma única linha
# é o mesmo que fazer x = x**2
quadrado = lambda x: x ** 2 
print("\n\nFunção lambda:", quadrado(3))


# qualquer variável definida fora de um comando com escopo (if, for, while, else, def) -> variável com escopo global
def funcao():
    variavel_local = 10

variavel_global = 20

def funcao2():
    print (variavel_global)
    # print (variavel_local) -> gera erro 

funcao2()


# função Args -> passa qualquer quantidade de variaveis -> operador *
def calcular_media (*numeros):
    soma = sum(numeros)
    quantidade = len(numeros)
    media = soma / quantidade

    return media

print ("\n\nA media desses numeros: ", calcular_media(10, 20, 32, 54, 2, -9, 6))


def area_triangulo (base, altura):
    return base * altura / 2


print("\n\n",area_triangulo(3, 2))

def soma_variavel (*numeros):
    total = 0

    for numero in numeros:
        total += numero
    return total

print ("\n\nO total: ", soma_variavel(2, 4, 1, 6, 7, 11))
print ("\n\nO total: ", soma_variavel(-2, -4, -1, -6, -7, -11))