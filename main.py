from ocr import selecionar_imagem, carregar_imagem, pre_processar, extrair_texto
from extrator import extrair_dados_receita


def processar_receita():
    caminho = selecionar_imagem()
    if not caminho:
        print("Nenhuma imagem selecionada.")
        return None
 
    imagem = carregar_imagem(caminho)
    imagem_tratada = pre_processar(imagem)
    texto = extrair_texto(imagem_tratada)
    dados = extrair_dados_receita(texto)
    dados["texto_bruto"] = texto
    return dados

def validar_crm(medicos, crm, uf):
    if crm is None or uf is None:
        print("CRM/UF não foram extraídos da receita!")
        return False

    crm_receita = str(crm).strip()
    uf_receita = str(uf).strip()

    crm_encontrado = False
    uf_encontrado = False

    for chave in medicos:
        print(f"Comparando com a chave", chave)
        if chave[0] == crm_receita:
            crm_encontrado = True
            print(f"Encontrei um CRM igual! UF cadastrada", chave[1])

            if chave[1] == uf_receita:
                uf_encontrado = True
                print(f"Encontrei uma UF igual!")

    if not crm_encontrado:
        print("Não encontrei um CRM igual no sistema!")
    if not uf_encontrado:
        print("Não encontrei um UF igual para o CRM informado!")

    if uf_encontrado:
        print("Validação Concluida com sucesso!")
    else:
        print("CRM Inválido!")

    return uf_encontrado

medicos_cadastrados = {
    ("12345", "PB"): {"nome": "Carlos"},
    ("67890", "SP"): {"nome": "Ana"},
    ("12345", "SP"): {"nome": "Bruno"}}

if __name__ == "__main__":
    dados_receita = processar_receita()
 
    if dados_receita:
        print("=== Texto extraído (bruto) ===")
        print(dados_receita["texto_bruto"])
 
        print("\n=== Dados estruturados ===")
        print(f"Médico: {dados_receita['medico']}")
        print(f"CRM: {dados_receita['crm']}")
        print(f"UF: {dados_receita['uf']}")
        print("Medicamentos:")
        if dados_receita["medicamentos"]:
            for med in dados_receita["medicamentos"]:
                print(f"  - {med['nome']} | Qtd: {med['quantidade']} {med['unidade']}")
        else:
            print("  Nenhum medicamento reconhecido pelo padrão.")

        valido = validar_crm(medicos_cadastrados, dados_receita["crm"], dados_receita["uf"])
        if valido:
            print("Receita Validada com sucesso!")
        else:
            print("Receita Inválida!")
 