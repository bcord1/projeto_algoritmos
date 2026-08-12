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
    dados["texto_bruto"] = texto
<<<<<<< HEAD
    return dados

# dados_receita = processar_receita()

# if dados_receita:
#     print("=== Texto extraído (bruto) ===")
#     print(dados_receita["texto_bruto"])

#     print("\n=== Dados estruturados ===")
#     print(f"CRM: {dados_receita['crm']}")
#     print(f"UF: {dados_receita['uf']}")
#     print("Medicamentos:")
#     if dados_receita["medicamentos"]:
#         for med in dados_receita["medicamentos"]:
#             print(f"  - {med['nome_do_medicamento']} | Qtd: {med['quantidade']} {med['unidade']}")
#     else:
#         print("  Nenhum medicamento reconhecido pelo padrão.")

#     valido = validar_crm(medicos_cadastrados, dados_receita["crm"], dados_receita["uf"])
#     if valido:
#         print("Receita Validada com sucesso!")
#     else:
#         print("Receita Inválida!")
=======
    return dados
>>>>>>> Verificação-de-CRM-lido-errado
