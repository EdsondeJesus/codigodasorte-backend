from itertools import combinations

# ================================ #
# CONFIGURAÇÃO DOS FILTROS FIXOS  #
# ================================ #
pares_desejados = 9
impares_desejados = 6

grupo1 = [1,2,4,5,6,9,11,12,14,18,19,20,21,22,25]
grupo2 = [3,7,8,10,13,15,16,17,23,24]

excluir_numeros = [16]
exigir_numeros = [8]

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





