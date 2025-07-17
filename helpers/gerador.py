from itertools import combinations

# ================================ #
# CONFIGURAÇÃO DOS FILTROS FIXOS  #
# ================================ #
pares_desejados = 7
impares_desejados = 8

grupo1 = [2,3,6,7,9,11,12,13,16,17,19,21,22,24,25]
grupo2 = [1,4,5,8,10,14,15,18,20,23]

excluir_numeros = [14,16,17,20]
exigir_numeros = [6,13]

def contar_impares(jogo):
    return sum(1 for d in jogo if d % 2 == 1)

def contar_pares(jogo):
    return sum(1 for d in jogo if d % 2 == 0)

def gerar_combinacoes():
    resultados = []

    for qtd_g1 in [9]:
        qtd_g2 = 15 - qtd_g1
        for comb1 in combinations(grupo1, qtd_g1):
            for comb2 in combinations(grupo2, qtd_g2):
                jogo = sorted(comb1 + comb2)

                if jogo[0] not in [1, 2, 3]:
                    continue

                if jogo[-1] <= 22:
                    continue

                pares = contar_pares(jogo)
                impares = contar_impares(jogo)
                if pares != pares_desejados or impares != impares_desejados:
                    continue

                if any(n in jogo for n in excluir_numeros):
                    continue

                if not all(n in jogo for n in exigir_numeros):
                    continue

                resultados.append(jogo)

    return resultados





