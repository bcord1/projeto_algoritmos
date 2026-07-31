import cv2
import pytesseract
import numpy as np
import re
from tkinter.filedialog import askopenfilename

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

unidades = (r"(?P<unidade>caixas?|comprimidos?|c[áa]psulas?|frascos?|ampolas?|tubos?|unidades?|gotas?|ml|mg)")

padrao_medicamento = re.compile(r"^(?P<nome>.+?)[_\s]+(?P<quantidade>\d+)\s*" + unidades + r"\s*$", re.IGNORECASE)

padrao_crm_uf = re.compile(r"CRM\s*[-–—]?\s*([A-Z]{2})\s*(\d{3,6})", re.IGNORECASE)

padrao_medico = re.compile(r"Dr\(?a\)?\.?\s*([^\n]+)", re.IGNORECASE)

def selecionar_imagem():
    caminho = askopenfilename(
        title = "Selecione a receita médica",
        filetypes = [("Imagens", "*.png *.jpg *.jpeg *.bmp")]
    )
    return caminho


def carregar_imagem(caminho):
    with open(caminho, "rb") as arquivo:
        dados_binarios = arquivo.read()
    array_bytes = np.frombuffer(dados_binarios, dtype = np.uint8)
    imagem = cv2.imdecode(array_bytes, cv2.IMREAD_COLOR)
    return imagem


def pre_processar(imagem):
    cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    _, binaria = cv2.threshold(cinza, 150, 255, cv2.THRESH_BINARY)
    return binaria


def extrair_texto(imagem_processada):
    config = r"--oem 3 --psm 6"
    texto = pytesseract.image_to_string(imagem_processada, lang = "por", config = config)
    return texto


def extrair_medico(texto):
    match = padrao_medico.search(texto)
    if match:
        nome = match.group(1).strip()
        nome = re.sub(r"\s{2,}", " ", nome)
        return nome
    return None


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
            nome = m.group("nome").strip(" _.")
            quantidade = int(m.group("quantidade"))
            unidade = m.group("unidade").lower()
            medicamentos.append({
                "nome": nome,
                "quantidade": quantidade,
                "unidade": unidade
            })
    return medicamentos


def extrair_dados_receita(texto):
    nome_medico = extrair_medico(texto)
    crm, uf = extrair_crm_uf(texto)
    medicamentos = extrair_medicamentos(texto)
 
    return {
        "medico": nome_medico,
        "crm": crm,
        "uf": uf,
        "medicamentos": medicamentos
    }


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
 