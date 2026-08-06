import sqlite3
from pathlib import Path

caminho_banco = Path(__file__).parent / "medicamentos.db" 
#Abre o arquivo medicamentos.db no diretório atual de execução do Python

medicamentos = sqlite3.connect(caminho_banco)

cursor = medicamentos.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS medicamentos (id INTEGER PRIMARY KEY AUTOINCREMENT,nome TEXT NOT NULL UNIQUE, quantidade INTEGER NOT NULL)")

medicamentosAdicionados = [
    "Tylenol 500mg",
    "Tylenol 750mg",
    "Novalgina 500mg",
    "Dorflex 300mg",
    "Cataflam 25mg",
    "Cataflam 50mg",
    "Voltaren 50mg",
    "Voltaren 75mg",
    "Buscopan 10mg",
    "Buscopan Composto 10mg",
    "Aspirina 100mg",
    "Aspirina 500mg",
    "Benegrip 400mg",
    "Amoxil 250mg",
    "Amoxil 500mg",
    "Amoxil 875mg",
    "Augmentin 500mg",
    "Augmentin 875mg",
    "Glifage 500mg",
    "Glifage 850mg",
    "Glifage 1g",
    "Losartan 25mg",
    "Losartan 50mg",
    "Losartan 100mg",
    "Norvasc 5mg",
    "Norvasc 10mg",
    "Lipitor 10mg",
    "Lipitor 20mg",
    "Lipitor 40mg",
    "Plasil 10mg",
    "Luftal 40mg",
    "Luftal 75mg",
    "Nexium 20mg",
    "Nexium 40mg",
    "Puran T4 50mcg",
    "Puran T4 100mcg",
    "Rivotril 0,5mg",
    "Rivotril 2mg"
]

cursor.executemany(
    "INSERT OR IGNORE INTO medicamentos (nome, quantidade) VALUES (?, 50)",
    [(medicamento,) for medicamento in medicamentosAdicionados],
)

medicamentos.commit()

def listarMedicamentos():
    cursor.execute("SELECT * FROM medicamentos")
    resultados = cursor.fetchall()
    for linha in resultados:
        print(linha)

def fecharBanco():
    medicamentos.close()
