#   Programa: HILL-CLIMBING E ILS
#   Autor: Victor Hugo Santos
#   Matéria: Meta-Heurísticas
#   Professor: Marcus Henrique Soares Mendes

import hill_climbing
import ils
import random

def gera_solucao_inicial(vetor_minimo, vetor_maximo):    # gera solucao inicial
    solucao = []    # lista de solução inicial

    for i in range (2):
        x = (vetor_maximo[i] - vetor_minimo[i])*(random.random()) + vetor_minimo[i] # gera um número aleatório para a variável i, sendo x quando i = 0 e y quando y = 1
        solucao.append(x)
    return solucao

# alterar os vetores abaixo para cada execução
vetor_minimo = [511, 404]   # vetor que contém os minimos de x e y, respectivamente
vetor_maximo = [512, 405]   # vetor que contém os máximos de x e y, respectivamente

solucao_inicial = gera_solucao_inicial(vetor_minimo, vetor_maximo)  # solucao inicial

for i in range (30):    # executa 30x

    # escolher algoritmo - descomentar um e comentar o outro, para cada execução
    #print(hill_climbing.hill_climbing(solucao_inicial, vetor_minimo, vetor_maximo)[1])
    print(ils.ils(solucao_inicial, vetor_minimo, vetor_maximo)[1])