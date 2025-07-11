def aplicar_filtros(jogo, config):
    if any(n in jogo for n in config["numeros_proibidos"]):
        return False
    if not all(n in jogo for n in config["exigir"]):
        return False
    if any(n in jogo for n in config["excluir"]):
        return False

    pares = sum(1 for n in jogo if n % 2 == 0)
    impares = 15 - pares

    if pares != config["qtde_pares"] or impares != config["qtde_impares"]:
        return False

    return True
