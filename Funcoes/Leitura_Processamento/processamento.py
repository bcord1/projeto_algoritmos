from .ocr import selecionar_imagem, processar_imagem, extrair_texto
from .extrator import extrair_dados_receita

def processar_receita():
    caminho = selecionar_imagem()
    if not caminho:
        print("Nenhuma imagem selecionada.")
        return None
 
    imagem = processar_imagem(caminho)
    texto = extrair_texto(imagem)
    dados = extrair_dados_receita(texto)
    return dados
