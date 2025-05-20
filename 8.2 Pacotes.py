# agrupamento de módulos relacionados
    # evita conflito entre os módulos

""" 
meu_pacote/             -> nome da pasta/diretório
    __init__.py         -> módulo 1
    modulo1.py          -> módulo 2
    modulo2.py          -> módulo 3


 """

# permite organizar e reutilizar os códigos de maneira mais eficiente 
# + legível
# + estruturado



from pacotesProprios import mod1


mod1.helloWorld()