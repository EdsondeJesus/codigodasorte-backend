from itertools import combinations

# ================================ #
# CONFIGURAÇÃO DOS FILTROS FIXOS  #
# ================================ #
pares_desejados = 9
impares_desejados = 6

# Grupos de dezenas definidos
grupo1 = [1,2,3,4,5,11,14,16,18,20,21,22,23,24,25]
grupo2 = [6,7,8,9,10,12,13,15,17,19]

# Números proibidos e obrigatórios
excluir_numeros = [16,17]
exigir_numeros = [8]

# ================================ #
# FUNÇÕES DE APOIO                #
# ================================ #
def contar_impares(jogo):
    return sum(1 for d in jogo if d % 2 == 1)

def contar_pares(jogo):
    return sum(1 for d in jogo if d % 2 == 0)

# ================================ #
# GERADOR PRINCIPAL               #
# ================================ #
def gerar_combinacoes():
    resultados = []

    for qtd_g1 in [8,9]:
        qtd_g2 = 15 - qtd_g1
        for comb1 in combinations(grupo1, qtd_g1):
            for comb2 in combinations(grupo2, qtd_g2):
                jogo = sorted(comb1 + comb2)

                # Critério 1: 1ª dezena entre 1 e 3
                if jogo[0] not in [1, 2, 3]:
                    continue

                # Critério 2: 15ª dezena > 22
                if jogo[-1] <= 22:
                    continue

                # Critério 3: exatamente X pares e Y ímpares
                pares = contar_pares(jogo)
                impares = contar_impares(jogo)
                if pares != pares_desejados or impares != impares_desejados:
                    continue

                # Critério 4: eliminar jogos com números proibidos
                if any(n in jogo for n in excluir_numeros):
                    continue

                # Critério 5: exigir todos os números obrigatórios
                if not all(n in jogo for n in exigir_numeros):
                    continue

                resultados.append(jogo)

                # Limite para teste (remova ou altere depois)
                if len(resultados) == 1:
                    return resultados

    return resultados


