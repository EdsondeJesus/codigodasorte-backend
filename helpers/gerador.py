from itertools import combinations

# ============================== #
# CONFIGURAÇÃO DOS FILTROS FIXOS #
# ============================== #

pares_desejados = 7
impares_desejados = 8

grupo1 = [1,9,13,15,17,19,25]
grupo2 = [2,10,14,16,18,20,22,24]
grupo3 = [3,5,7,11,21]
grupo4 = [4,6,8,12]

quantidade_g1 = 5
quantidade_g2 = 4
quantidade_g3 = 3
quantidade_g4 = 3

excluir_numeros = [11]
exigir_numeros = [24]

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
                    
                    # Regra 4: exclusões
                    if any(n in jogo for n in excluir_numeros):
                        continue

                    # Regra 5: exigências obrigatórias
                    if not all(n in jogo for n in exigir_numeros):
                        continue

                    resultados.append(jogo)

    return resultados
