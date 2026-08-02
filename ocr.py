import cv2
import pytesseract
import numpy as np
from tkinter.filedialog import askopenfilename

from config import Tesseract_cmd


pytesseract.pytesseract.tesseract_cmd = Tesseract_cmd


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


def extrair_texto(imagem_tratada):
    config = "--oem 3 --psm 6"
    texto = pytesseract.image_to_string(imagem_tratada, lang = "por", config = config)
    return texto