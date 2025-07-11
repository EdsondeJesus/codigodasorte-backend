from fastapi import FastAPI, Query
import random
import json
from filtros import aplicar_filtros

app = FastAPI()

@app.get("/")
def home():
    return {"mensagem": "API do Código da Sorte Online."}

@app.get("/gerar")
def gerar_combinacoes(quantidade: int = Query(..., gt=0, le=10000)):
    with open("config.json", "r") as f:
        config = json.load(f)

    resultados = []
    tentativas = 0

    while len(resultados) < quantidade and tentativas < quantidade * 50:
        jogo = sorted(random.sample(config["dezenas_validas"], 15))
        if aplicar_filtros(jogo, config):
            resultados.append(jogo)
        tentativas += 1

    return {
        "total_gerado": len(resultados),
        "tentativas": tentativas,
        "combinacoes": resultados
    }
