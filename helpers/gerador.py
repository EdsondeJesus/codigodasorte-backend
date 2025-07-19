from itertools import combinations

# ============================== #
# CONFIGURAÇÃO DOS FILTROS FIXOS #
# ============================== #

pares_desejados = 7
impares_desejados = 8

grupo1 = [3,5,7,9,13,19,21,23,25]
grupo2 = [4,10,12,16,22,24]
grupo3 = [1,11,15,17,]
grupo4 = [2,6,8,14,18,20]

# ajuste conforme desejar:
quantidades = [6, 4, 2, 3]  # deve sempre somar 15

excluir_numeros = [2,15,16]
exigir_numeros = [8,17]

def contar_impares(jogo):
    return sum(1 for d in jogo if d % 2 == 1)

def contar_pares(jogo):
    return sum(1 for d in jogo if d % 2 == 0)

def gerar_combinacoes():
    resultados = []
    
    for comb1 in combinations(grupo1, quantidades[0]):
        for comb2 in combinations(grupo2, quantidades[1]):
            for comb3 in combinations(grupo3, quantidades[2]):
                for comb4 in combinations(grupo4, quantidades[3]):
                    jogo = sorted(set(comb1 + comb2 + comb3 + comb4))
                    if len(jogo) != 15:
                        continue

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






