from itertools import combinations

# ============================== #
# CONFIGURAÇÃO DOS FILTROS FIXOS #
# ============================== #

pares_desejados = 9
impares_desejados = 6

grupo1 = [1,7,9,15,17,21,25]
grupo2 = [2,6,8,14,18,20,22,24]
grupo3 = [3,5,11,13,19,23]
grupo4 = [4,10,12,16]

# Quantidade fixa por grupo (deve sempre somar 15)
quantidade_g1 = 3
quantidade_g2 = 6
quantidade_g3 = 3
quantidade_g4 = 3

excluir_numeros = [16]
exigir_numeros = [19]


# === Funções auxiliares ===

def contar_impares(jogo):
    return sum(1 for d in jogo if d % 2 == 1)

def contar_pares(jogo):
    return sum(1 for d in jogo if d % 2 == 0)


# === Geração com regras fixas ===

def gerar_combinacoes():
    resultados = []
    
    for comb1 in combinations(grupo1, quantidade_g1):
        for comb2 in combinations(grupo2, quantidade_g2):
            for comb3 in combinations(grupo3, quantidade_g3):
                for comb4 in combinations(grupo4, quantidade_g4):
                        if len(jogo) != 15:
                           continue

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
