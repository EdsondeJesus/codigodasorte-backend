from itertools import combinations

# Grupos de dezenas definidos
grupo1 = [1,3,4,6,7,8,9,12,13,15,16,17,18,21,25]
grupo2 = [2,5,10,11,14,19,20,22,23,24]

# Números proibidos e obrigatórios
excluir_numeros = [16,17]
exigir_numeros = [8]

def contar_impares(seq):
    return sum(1 for n in seq if n % 2 != 0)

def gerar_combinacoes():
    resultados = []

    for qtd_g1 in [9, 10]:
        qtd_g2 = 15 - qtd_g1
        for comb1 in combinations(grupo1, qtd_g1):
            for comb2 in combinations(grupo2, qtd_g2):
                jogo = sorted(list(comb1 + comb2))

                # Critério: 1ª dezena entre 1 e 3
                if jogo[0] not in [1, 2, 3]:
                    continue

                # Critério: 15ª dezena > 22
                if jogo[-1] <= 22:
                    continue

                # Critério: 7 a 9 ímpares
                impares = contar_impares(jogo)
                if impares not in [7, 8, 9]:
                    continue

                # Eliminar jogos que contenham qualquer número proibido
                if any(n in jogo for n in excluir_numeros):
                    continue

                # Manter somente jogos que contenham todos os exigidos
                if not all(n in jogo for n in exigir_numeros):
                    continue

                resultados.append(jogo)

                # Para testes: gerar apenas 3
                if len(resultados) == 3:
                    return resultados

    return resultados

