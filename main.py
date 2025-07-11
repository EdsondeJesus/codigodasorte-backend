from fastapi import FastAPI
from helpers.gerador import gerar_combinacoes

app = FastAPI()

@app.get("/")
def raiz():
    return {"mensagem": "API do Código da Sorte Online."}

@app.get("/gerar")
def gerar():
    combinacoes = gerar_combinacoes()
    return {"jogos": combinacoes}
