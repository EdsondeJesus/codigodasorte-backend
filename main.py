from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from helpers.gerador import gerar_combinacoes  # Certifique-se de que o caminho está correto
import random

app = FastAPI()

@app.get("/gerar", response_class=HTMLResponse)
def gerar():
    try:
        combinacoes = gerar_combinacoes()  # Sem parâmetros, com filtros definidos internamente
        if not combinacoes:
            return HTMLResponse("<h1>⚠️ Nenhuma combinação encontrada</h1>")

        jogo = random.choice(combinacoes)
        jogo_formatado = " - ".join(str(num).zfill(2) for num in jogo)

        html = f"""
        <!DOCTYPE html>
        <html lang="pt-BR">
        <head>
            <meta charset="UTF-8">
            <title>Código da Sorte</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
                    color: white;
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    justify-content: center;
                    height: 100vh;
                    margin: 0;
                }}
                h1 {{
                    font-size: 3em;
                    margin-bottom: 10px;
                }}
                .jogo {{
                    font-size: 2em;
                    background-color: #ffffff10;
                    padding: 15px 30px;
                    border-radius: 10px;
                    margin-top: 20px;
                    box-shadow: 0 0 10px #00ffc3;
                }}
                button {{
                    background-color: #00ffc3;
                    color: black;
                    font-size: 1.2em;
                    padding: 12px 25px;
                    border: none;
                    border-radius: 8px;
                    cursor: pointer;
                    transition: background 0.3s;
                    margin-top: 20px;
                }}
                button:hover {{
                    background-color: #00cc99;
                }}
            </style>
        </head>
        <body>
            <h1>🎯 Seu Código da Sorte</h1>
            <div class="jogo">{jogo_formatado}</div>
            <form method="get" action="/gerar">
                <button type="submit">Gerar novo jogo</button>
            </form>
        </body>
        </html>
        """
        return html

    except Exception as e:
        return HTMLResponse(f"<h1>Erro interno: {str(e)}</h1>", status_code=500)



