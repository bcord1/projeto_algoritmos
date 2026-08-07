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
    "Rivotril 2mg",
    "Amoxicilina 250mg",
    "Amoxicilina 500mg",
    "Amoxicilina 875mg",
    "Losartana Potássica 25mg",
    "Losartana Potássica 50mg",
    "Losartana Potássica 100mg",
    "Paracetamol 500mg",
    "Paracetamol 750mg",
    "Ibuprofeno 200mg",
    "Ibuprofeno 300mg",
    "Ibuprofeno 400mg",
    "Ibuprofeno 600mg",
    "Omeprazol 10mg",
    "Omeprazol 20mg",
    "Omeprazol 40mg",
    "Dipirona 500mg",
    "Dipirona 1g",
    "Azitromicina 250mg",
    "Azitromicina 500mg",
    "Azitromicina 600mg"
    "Loratadina 10mg",
    "Prednisona 5mg",
    "Prednisona 20mg",
    "Cefalexina 500mg",
    "Cefalexina 1g",
    "Nimesulida 100mg",
    "Ambroxol 30mg",
    "Metformina 500mg",
    "Metformina 850mg",
    "Metformina 1g",
    "Vitamina D 1000UI",
    "Vitamina D 2000UI",
    "Vitamina D 7000UI",
    "Vitamina D 50000UI",
    "Levofloxacino 500mg",
    "Levofloxacino 750mg",
    "Pantoprazol 20mg",
    "Pantoprazol 40mg",
    "Diclofenaco Sódico 50mg",
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
