import re

Tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

unidades = (r"(?P<unidade>caixas?|comprimidos?|c[áa]psulas?|frascos?|ampolas?|tubos?|unidades?|gotas?|ml|mg)")

padrao_medicamento = re.compile(r"^(?P<nome_do_medicamento>.+?)[_\s]+(?P<quantidade>\d+)\s*" + unidades + r"\s*$", re.IGNORECASE)

padrao_crm_uf = re.compile(r"CRM\s*[-–—]?\s*([A-Z]{2})\s*(\d{3,6})", re.IGNORECASE)