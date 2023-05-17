''' DISTRIBUIÇÃO DE FREQUENCIA 
Na estatística a ideia de frequência é aplicada ao problema que
estamos analisando. Ou seja, verificamos a frequência de um ou mais
eventos a partir da amostra da população e assim permitindo gerar a
Distribuição de Frequências ou Distribuição de Densidade.
Outro evento deverá gerar uma nova distribuição.
'''

import numpy as np
sexo = np.loadtxt('./sexoCenso.csv')
#print(sexo)

print('Tamanho da Amostra: ',sexo.size)
print('FREQUENCIAS: ----------------------------------------------------------------')

freqMasculino = np.count_nonzero(sexo == 0)
freqFeminino = np.count_nonzero(sexo == 1)

print('Tamanho da Amostra: ',sexo.size)
print('Frequencia Masculina: ',freqMasculino)
print('Frequencia Feminino: ',freqFeminino)

'''FREQUENCIA RELATIVA
É uma forma de identificar como uma categoria se apresenta frente às
demais e em relação a amostra.
Esta é uma característica que está diretamente ligada ao tamanho da
amostra. 1/10 é muito diferente de 1/10000.

FREQUENCIA RELATIVA = FREQUENCIA DA CATEGORIA / TAMANHO DA AMOSTRA
* Para obter o percentual :
FREQUENCIA RELATIVA = FREQUENCIA DA CATEGORIA / TAMANHO DA AMOSTRA * 100
'''
print('FREQUENCIA RELATIVA: ----------------------------------------------------------------')
print(f'Frequencia Feminino: {freqMasculino/sexo.size*100:.2f}%')

print(f'Frequencia Feminino: {freqFeminino/sexo.size*100:.2f}%')

'''FREQUENCIAS QUANTITATIVAS'''
renda = np.loadtxt('./rendaCenso.csv')
#print(renda)

vMin= renda.min()
vMax = renda.max()

# Amplitude Total
aT = vMax - vMin
print('vMin (Valor Mínimo: ',vMin)
print('vMax (Valor Máximo: ',vMax)
print('Amplitude = ',aT)

'''DIVISÃO DE CLASSES'''
#Qtde. Colunas
k = 6

#Amplitude das classes (h)
h = aT / k
print(f'Amplitude das classes: {h:.2f}')

classes = []
limite = renda.min()

for i in range(k):
    classes.append(limite)
    limite += h
print(f'Classes: {classes}')

# Define nome das classes
rotulos = ['E','D','C','B','A']

import pandas as pd
#Associa os elementos da lista de RENDA aos ROTULOS de acordo com as CLASSES
print(pd.cut(x = renda, bins = classes, labels = rotulos))

#Inclui o menor valor (include_lowest=True)
freqRendas = pd.cut(x = renda, bins = classes, labels = rotulos,include_lowest=True)

#CONTAR AS FREQUENCIAS DAS MINHAS CLASSES
print(pd.value_counts(freqRendas))

#REGRA DE STURGES
k = 1 + (10/3)* np.log10(renda.size)
k = int(k) 

fraquencia = pd.value_counts(
    pd.cut(x = renda, bins = k, include_lowest=True)
    )
print(fraquencia)

import seaborn as sns

grafico = sns.displot(renda, kde = True )
grafico.ax.set_title('Renda')
grafico.figure.set_size_inches(10,4)
grafico.set_axis_labels('R$', fontsize=14)

#FREQUENCIAS ACUMULADAS
import scipy.stats as sts

print(sts.cumfreq(renda,11))

