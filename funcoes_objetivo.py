#   Programa: HILL-CLIMBING E ILS
#   Autor: Victor Hugo Santos
#   Matéria: Meta-Heurísticas
#   Professor: Marcus Henrique Soares Mendes

import math

def funcao_objetivo1(x, y):  # calcula o valor para a funcao objetivo do exercício 1
    funcao = (math.sin(math.radians(x+y))) + (math.pow(x-y,2)) - (1.5*x) + (2.5*y) + 1

    return funcao

def funcao_objetivo2(x, y):  # calcula o valor para a funcao objetivo do exercício 2
    funcao = -1*(y+47)*(math.sin(math.radians(math.sqrt(abs(x/2 + (y+47)))))) -x*(math.sin(math.radians(math.sqrt(abs(x - (y + 47))))))

    return funcao