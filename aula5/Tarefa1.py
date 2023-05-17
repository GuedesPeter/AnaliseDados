'''Tarefa 1
a. Gerar uma lista aleatória de 100 posições
b. Identificar a média da lista
c. Identificar a média geométrica
d. Identificar a mediana da lista
e. Identificar a moda da lista
f. Imprimir o histograma da lista
g. Façam um plot (mostrar o gráfico) do histograma dos valores de carros do
carro-valor.txt'''

import numpy as np
from scipy.stats import mode
from math import sqrt
from matplotlib import pyplot 


#A) Gerar uma lista aleatória de 100 posições
lista = np.random.randint(100, size=100)
print(lista)

#B) Identificar a média da lista
media = np.sum(lista)/lista.size
print('Média: ',media)

#C) Identificar a média geométrica
mediaGeo = np.prod(lista)
print(f'Média Geométrica: {(mediaGeo)**(1/lista.size):.2f}')

#D) Identificar a mediana da lista
mediana = np.median(lista)
print('Mediana: ',mediana)

#E) Identificar a moda da lista
moda = mode(lista)
print('Moda: ',moda)

#F) Imprimir o histograma da lista
pyplot.hist(lista)
pyplot.show()

#G) Façam um plot (mostrar o gráfico) do histograma dos valores de carros do
#carro-valor.txt

carros = np.loadtxt('carros-valor.txt')
#print(carros)
pyplot.hist(carros)
pyplot.show()
