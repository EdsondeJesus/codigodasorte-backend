from fastapi import FastAPI
from itertools import combinations, product
import random

app = FastAPI()

# Grupos fixos
grupos = {
 "Grupo 1": ([2, 3, 4, 5, 6], [2, 3, 4]),
 "Grupo 2": ([7, 9, 10, 11, 12], [2, 3, 4]),
 "Grupo 3": ([14, 15, 16, 22, 23], [2, 3, 4]),
 "Grupo 4": ([8, 18, 20, 24], [2, 3]),
 "Grupo 5": ([1, 13, 17, 19, 21, 25], [3, 4, 5])
}

# Filtros
g6, q6 = [2,3,4,5,6,7,9,10,11,12,14,15,16,22,23], [8,9,10]
g7, q7 = [3,5,7,9,11,15,23], [3,4,5]
g8, q8 = [2,4,9,10,11,12,15,16,23], [6]
g9, q9 = [16,17], [0]

def filtro(jogo):
 return (
  sum(n in g6 for n in jogo) in q6 and
  sum(n in g7 for n in jogo) in q7 and
  sum(n in g8 for n in jogo) in q8 and
  sum(n in g9 for n in jogo) in q9 and
  sum(n % 2 for n in jogo) == 6
 )

@app.get("/gerar-jogos")
def gerar_jogos():
    combs = {k: sum([list(combinations(v[0], i)) for i in v[1]], []) for k, v in grupos.items()}
    jogos_validos = []
    combinacoes = list(product(combs["Grupo 1"], combs["Grupo 2"], combs["Grupo 3"], combs["Grupo 4"], combs["Grupo 5"]))
    random.shuffle(combinacoes)
    
    for g1, g2, g3, g4, g5 in combinacoes:
        jogo = sorted(set(g1 + g2 + g3 + g4 + g5))
        if len(jogo) == 15 and filtro(jogo):
            jogos_validos.append(jogo)
        if len(jogos_validos) == 3:
            break
    return {"jogos": jogos_validos}
