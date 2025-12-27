from itertools import combinations

# ============================== #
# CONFIGURAÇÃO DOS FILTROS FIXOS #
# ============================== #

pares_desejados = 8
impares_desejados = 7

grupo1 = [1,6,11,16,20,21,23]
grupo2 = [2,4,5,10,12,14]
grupo3 = [15,17,18,19,22]
grupo4 = [3,8,9,13,25]

quantidade_g1 = 7
quantidade_g2 = 3
quantidade_g3 = 3
quantidade_g4 = 2

# === Funções auxiliares ===

def contar_pares(jogo):
    return sum(1 for n in jogo if n % 2 == 0)

def contar_impares(jogo):
    return sum(1 for n in jogo if n % 2 != 0)

# === Geração com regras fixas ===

def gerar_combinacoes():
    resultados = []

    for comb1 in combinations(grupo1, quantidade_g1):
        for comb2 in combinations(grupo2, quantidade_g2):
            for comb3 in combinations(grupo3, quantidade_g3):
                for comb4 in combinations(grupo4, quantidade_g4):
                    jogo = list(comb1 + comb2 + comb3 + comb4)
                    if len(jogo) != 15:
                        continue

                    jogo = sorted(jogo)

                    # Regra 1: o menor número deve ser 1, 2 ou 3
                    if jogo[0] not in [1, 2, 3]:
                        continue

                    # Regra 2: o maior número deve ser maior que 22
                    if jogo[-1] <= 22:
                        continue
                    
                    # Regra 3: paridade exata
                    pares = contar_pares(jogo)
                    impares = contar_impares(jogo)
                    if pares != pares_desejados or impares != impares_desejados:
                        continue
                    
                    resultados.append(jogo)

    return resultados
