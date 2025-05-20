# arquivo que contém funções, classes e variáveis importantes
    # IA, ordenação, math, random, datetime, sys, json, 
    # numpy (cálculo numérico), pandas (análise de dados), matplotlib (gráficos)
    # requests, flask (back-end), django, (framework), scikit-learn (machine learning)

# muitas funções e conteúdos prontos para facilitar o desenvolvimento

""" 
import math

resultado = math.sqrt(50)
print (resultado)

 """

# é possível importar funções específicas

from math import sin, radians

graus = 30
radianos = radians(graus)
print (sin(radianos))

    # estamos importando somente os métodos -> seno e transformação de graus em radianos

import random

valor = random.randint(10, 30)
print (f"Valor random entre 10 e 30: {valor}")


import datetime

dataAtual = datetime.datetime.now()
print (f"Data atual {dataAtual}")

data = datetime.date(2025, 5, 20)
print (f"Data {data}")

hora = datetime.time()
print (f"Hora {hora}")