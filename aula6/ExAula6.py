'''
Tarefa 1
1.2. UF;
1.2.1.Faz sentido dividir UFs em classes? PQ?
1.2.1.1. E calcular o desvio padrão das UFs? Tem como? PQ?
1.2.2. Calcule o desvio padrão das frequências dos UFs
1.3. Altura
1.3.1.Calcule o desvio padrão das alturas.
1.3.2. Número de classes de acordo com a regra de sturges
1.3.3. Calcular a amplitude das classes
1.3.4. Gerar os rótulos para cada classe da regra de sturges
1.3.5. Os dados possuem uma distribuição normal?

'''
#1. Realizar a distribuição de frequência com os valores totais e o percentual para os dados:
#1.1. COR

import numpy as np
cor = np.loadtxt('./corCenso.csv')
#Tam. Amostra
#print(cor.size)

freqCor1 = np.count_nonzero(cor == 0) # =! 0
freqCor2 = np.count_nonzero(cor == 2) # =! 2
freqCor3 = np.count_nonzero(cor == 4) # =! 4
freqCor4 = np.count_nonzero(cor == 6) # =! 6
freqCor5 = np.count_nonzero(cor == 8) # =! 8


print(f'Valor Total: {freqCor1/cor.size} - Percentual: {freqCor1/cor.size*100}%')
print(f'Valor Total: {freqCor2/cor.size} - Percentual: {freqCor2/cor.size*100}%')
print(f'Valor Total: {freqCor3/cor.size} - Percentual: {freqCor3/cor.size*100}%')
print(f'Valor Total: {freqCor4/cor.size} - Percentual: {freqCor4/cor.size*100}%')
print(f'Valor Total: {freqCor5/cor.size} - Percentual: {freqCor5/cor.size*100}%')