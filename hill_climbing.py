import random
import funcoes_objetivo

def perturba_hc(vetor_solucao, r, vetor_minimo, vetor_maximo):
    p = 1 # probabilidade de se adicionar um ruido em alguma variavel

    for i in range (2):
        if (p >= 1):    # sempre vai executar pois o p = 1
            while True:
                n = (r + r)*(random.random()) - r   # n = valor aleatório entre -r e r
                if (vetor_minimo[i] <= (vetor_solucao[i] + n) and (vetor_solucao[i] + n) <= vetor_maximo[i]):
                    
                    break
            vetor_solucao[i] = (vetor_solucao[i] + n)
    return vetor_solucao

def hill_climbing(solucao, vetor_minimo, vetor_maximo): # parametro solucao = solucao_inicial

    cont_interacoes_sem_melhora = 0

    # valor da função objetivo para a solucao inicial aleatoria - descomentar um e comentar o outro para cada execução
    #valorSolucao = funcoes_objetivo.funcao_objetivo1(solucao[0], solucao[1])
    valorSolucao = funcoes_objetivo.funcao_objetivo2(solucao[0], solucao[1])

    r = 0.1  # perturbacao

    while (cont_interacoes_sem_melhora < 100):    # condição de parada: 100 iterações sem melhora da Função Objetivo

        # perturba solucao
        solucao_perturbada = perturba_hc(solucao.copy(), r, vetor_minimo, vetor_maximo)

        # valor da função objetivo para a solucao perturbada - descomentar um e comentar o outro para cada execução
        #valorPerturbada = funcoes_objetivo.funcao_objetivo1(solucao_perturbada[0], solucao_perturbada[1])
        valorPerturbada = funcoes_objetivo.funcao_objetivo2(solucao_perturbada[0], solucao_perturbada[1])


        if (valorPerturbada < valorSolucao):    # verifica qualidade
            solucao = solucao_perturbada.copy()

            valorSolucao = valorPerturbada

            cont_interacoes_sem_melhora = 0 # reseta contador para condição de parada, pois houve alteracao
        
        else:
            cont_interacoes_sem_melhora += 1    # incrementa contador para condição de parada, pois não houve alteracao

    return solucao, valorSolucao