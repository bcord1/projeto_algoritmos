import cv2
import pytesseract
from tkinter.filedialog import askopenfilename

from .config import Tesseract_cmd


pytesseract.pytesseract.tesseract_cmd = Tesseract_cmd


def selecionar_imagem():
    caminho_da_imagem = askopenfilename(
        title = "Selecione a receita médica",
        filetypes = [("Imagens", "*.png *.jpg *.jpeg *.bmp")]
    )
    return caminho_da_imagem


def processar_imagem(caminho):
    imagem = cv2.imread(caminho)
    cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    return cinza


def extrair_texto(imagem):
    texto_da_imagem = pytesseract.image_to_string(imagem, lang="por", config="--oem 3 --psm 6")
    return texto_da_imagem