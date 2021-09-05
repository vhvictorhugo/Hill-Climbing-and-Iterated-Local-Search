import random
import funcoes_objetivo
import hill_climbing

def perturba_ils(vetor_solucao, r, vetor_minimo, vetor_maximo):

    for i in range (2):
        while True:
            n = (r + r)*(random.random()) - r   # n = valor aleatório entre -r e r
            if (vetor_minimo[i] <= (vetor_solucao[i] + n) and (vetor_solucao[i] + n) <= vetor_maximo[i]):
                
                break
        vetor_solucao[i] = (vetor_solucao[i] + n)
    return vetor_solucao
    
def define_melhor_solucao(memoria):    # vai percorrer a estrutura de memória e verificar qual solução apresenta o melhor valor
    
    tamanho_memoria = len(memoria)

    valor_solucoes = []
    melhor = []

    for i in range (tamanho_memoria - 1):   # percorre a memoria e calcula o valor solucao para cada vetor de solucao - assim teremos um vetor com o valor das funcoes objetivo
        # valor da função objetivo para a solucao - descomentar um e comentar o outro para cada execução
        #valor_solucoes.append(funcoes_objetivo.funcao_objetivo1(memoria[i][0], memoria[i][1]))
        valor_solucoes.append(funcoes_objetivo.funcao_objetivo2(memoria[i][0], memoria[i][1]))
    
    melhor = valor_solucoes[0]  # atribuicao inicial
    indice = 0
    
    for j in range (1, tamanho_memoria - 1):    # percorre o vetor_solucoes para se resgatar o indice de melhor valor para funcao objetivo
        if (valor_solucoes[j] < melhor):
            melhor = valor_solucoes[j]
            indice = j


    return memoria[indice]

def ils(solucao, vetor_minimo, vetor_maximo):   # parametro solucao = solucao_inicial

    memoria = []    # estrutura de memória que vai armazenar as possíveis soluções e possibilitar escolher a melhor dentre todas
    cont_interacoes = 0
    
    solucao_busca_local = hill_climbing.hill_climbing(solucao.copy(), vetor_minimo, vetor_maximo)[0]    # busca local (é o s* da literatura)
    memoria.append(solucao_busca_local)

    r = 0.02 # tamanho da perturbacao vai depender do problema - deve ser suficientemente grande para evitar um reinicio aleatorio e suficientemente pequena para encontrar soluções diversas

    while (cont_interacoes < 50):    # condição de parada: 50 iterações
        
        solucao_perturbada = perturba_ils(solucao_busca_local.copy(), r, vetor_minimo, vetor_maximo)    # perturbacao (é o s' da literatura)   
        memoria.append(solucao_perturbada)

        solucao_auxiliar = hill_climbing.hill_climbing(solucao_perturbada.copy(), vetor_minimo, vetor_maximo)[0]  # busca local novamente (é o s*' da literatura)
        memoria.append(solucao_auxiliar)
        
        solucao_busca_local = solucao_auxiliar.copy() # critério de aceitação: aceitar sempre o ótimo local mais recente, favorecendo a diversificação (é o s* da literatura)

        cont_interacoes += 1

        r += 0.02

    melhor_solucao = define_melhor_solucao(memoria)

    # valor da função objetivo para a solucao - descomentar um e comentar o outro para cada execução
    #valor_melhor_solucao = funcoes_objetivo.funcao_objetivo1(melhor_solucao[0], melhor_solucao[1])
    valor_melhor_solucao = funcoes_objetivo.funcao_objetivo2(melhor_solucao[0], melhor_solucao[1])
        
    return melhor_solucao, valor_melhor_solucao