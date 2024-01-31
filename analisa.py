from collections import Counter

def processar_arquivos(arquivo_entrevista, arquivo_excluir):
    with open(arquivo_entrevista, "r", encoding="utf-8") as file:
        texto_entrevista = file.read()

    with open(arquivo_excluir, "r", encoding="utf-8") as file:
        texto_excluir = file.read()

    # Remova pontuações do texto_entrevista
    for char in ".,":
        texto_entrevista = texto_entrevista.replace(char, "")

    palavras_entrevista = texto_entrevista.split()
    palavras_excluir = set(texto_excluir.split())

    # Filtrar e contar as palavras
    palavras_filtradas = [palavra for palavra in palavras_entrevista if len(palavra) >= 4 and palavra not in palavras_excluir]
    contagem = Counter(palavras_filtradas)

    return contagem

def salvar_resultados(contagem, arquivo_palavras_frequentes, arquivo_lista_palavras, arquivo_top_20, arquivo_repetido):
    # Salvar as palavras frequentes
    with open(arquivo_palavras_frequentes, "w") as file:
        for palavra, frequencia in contagem.most_common(50):
            palavra = palavra.replace('(', '').replace(')', '').replace("'", '')
            file.write(f"{palavra} {frequencia}\n")

    # Salvar a lista de palavras filtradas
    with open(arquivo_lista_palavras, "w") as file:
        for palavra in sorted(contagem.elements()):
            palavra = palavra.replace('(', '').replace(')', '').replace("'", '')
            file.write(f"{palavra}\n")

    # Salvar as 20 palavras mais frequentes
    with open(arquivo_top_20, "w") as file:
        top_20 = contagem.most_common(20)
        for palavra, frequencia in top_20:
            palavra = palavra.replace('(', '').replace(')', '').replace("'", '')
            file.write(f"{palavra} {frequencia}\n")

    # Salvar as 20 palavras mais repetidas
    with open(arquivo_repetido, "w") as file:
        top_20 = contagem.most_common(20)
        for palavra, frequencia in top_20:
            palavra = palavra.replace('(', '').replace(')', '').replace("'", '')
            linha_repetida = f"{palavra} " * frequencia  # Repete a palavra 'frequencia' vezes
            file.write(linha_repetida.strip() + "\n")

if __name__ == "__main__":
    arquivo_entrevista = "arquivos/Entrevista.txt"
    arquivo_excluir = "arquivos/Excluir.txt"
    arquivo_palavras_frequentes = "arquivos/PalavrasFrequentes.txt"
    arquivo_lista_palavras = "arquivos/ListaDePalavras.txt"
    arquivo_top_20 = "arquivos/Top20Palavras.txt"
    arquivo_repetido = "arquivos/PalavrasRepetidas.txt"

    contagem = processar_arquivos(arquivo_entrevista, arquivo_excluir)
    salvar_resultados(contagem, arquivo_palavras_frequentes, arquivo_lista_palavras, arquivo_top_20, arquivo_repetido)

