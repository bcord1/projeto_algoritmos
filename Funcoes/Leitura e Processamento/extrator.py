import re
from config import padrao_crm_uf, padrao_medicamento


def extrair_crm_uf(texto):
    match = padrao_crm_uf.search(texto)
    if match:
        uf = match.group(1).upper()
        crm = match.group(2)
        return crm, uf
    return None, None
 
 
def extrair_medicamentos(texto):
    medicamentos = []
    for linha in texto.split("\n"):
        linha_limpa = linha.strip()
        if not linha_limpa:
            continue
        m = padrao_medicamento.match(linha_limpa)
        if m:
            nome = m.group("nome_do_medicamento").strip(" _.")
            quantidade = int(m.group("quantidade"))
            unidade = m.group("unidade").lower()
            medicamentos.append({
                "nome_do_medicamento": nome,
                "quantidade": quantidade,
                "unidade": unidade
            })
    return medicamentos


def extrair_dados_receita(texto):
    crm, uf = extrair_crm_uf(texto)
    medicamentos = extrair_medicamentos(texto)
 
    return {
        "crm": crm,
        "uf": uf,
        "medicamentos": medicamentos
    }