import sqlite3
from pathlib import Path

caminho_banco = Path(__file__).parent / "medicamentos.db" 

medicamentos = sqlite3.connect(caminho_banco)

cursor = medicamentos.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS medicamentos (id INTEGER PRIMARY KEY AUTOINCREMENT,nome TEXT NOT NULL UNIQUE, quantidade INTEGER NOT NULL)")

medicamentosAdicionados = [
    "TYLENOL 500MG",
    "TYLENOL 750MG",
    "NOVALGINA 500MG",
    "DORFLEX 300MG",
    "CATAFLAM 25MG",
    "CATAFLAM 50MG",
    "VOLTAREN 50MG",
    "VOLTAREN 75MG",
    "BUSCOPAN 10MG",
    "BUSCOPAN COMPOSTO 10MG",
    "ASPIRINA 100MG",
    "ASPIRINA 500MG",
    "BENEGRIP 400MG",
    "AMOXIL 250MG",
    "AMOXIL 500MG",
    "AMOXIL 875MG",
    "AUGMENTIN 500MG",
    "AUGMENTIN 875MG",
    "GLIFAGE 500MG",
    "GLIFAGE 850MG",
    "GLIFAGE 1G",
    "LOSARTAN 25MG",
    "LOSARTAN 50MG",
    "LOSARTAN 100MG",
    "NORVASC 5MG",
    "NORVASC 10MG",
    "LIPITOR 10MG",
    "LIPITOR 20MG",
    "LIPITOR 40MG",
    "PLASIL 10MG",
    "LUFTAL 40MG",
    "LUFTAL 75MG",
    "NEXIUM 20MG",
    "NEXIUM 40MG",
    "PURAN T4 50MCG",
    "PURAN T4 100MCG",
    "RIVOTRIL 0,5MG",
    "RIVOTRIL 2MG",
    "AMOXICILINA 250MG",
    "AMOXICILINA 500MG",
    "AMOXICILINA 875MG",
    "LOSARTANA POTÁSSICA 25MG",
    "LOSARTANA POTÁSSICA 50MG",
    "LOSARTANA POTÁSSICA 100MG",
    "PARACETAMOL 500MG",
    "PARACETAMOL 750MG",
    "IBUPROFENO 200MG",
    "IBUPROFENO 300MG",
    "IBUPROFENO 400MG",
    "IBUPROFENO 600MG",
    "OMEPRAZOL 10MG",
    "OMEPRAZOL 20MG",
    "OMEPRAZOL 40MG",
    "DIPIRONA 500MG",
    "DIPIRONA 1G",
    "AZITROMICINA 250MG",
    "AZITROMICINA 500MG",
    "AZITROMICINA 600MG",
    "LORATADINA 10MG",
    "PREDNISONA 5MG",
    "PREDNISONA 20MG",
    "CEFALEXINA 500MG",
    "CEFALEXINA 1G",
    "NIMESULIDA 100MG",
    "AMBROXOL 30MG",
    "METFORMINA 500MG",
    "METFORMINA 850MG",
    "METFORMINA 1G",
    "VITAMINA D 1000UI",
    "VITAMINA D 2000UI",
    "VITAMINA D 7000UI",
    "VITAMINA D 50000UI",
    "LEVOFLOXACINO 500MG",
    "LEVOFLOXACINO 750MG",
    "PANTOPRAZOL 20MG",
    "PANTOPRAZOL 40MG",
    "DICLOFENACO SÓDICO 50MG",
]


cursor.executemany(
    "INSERT OR IGNORE INTO medicamentos (nome, quantidade) VALUES (?, 50)",
    [(medicamento,) for medicamento in medicamentosAdicionados],
)

medicamentos.commit()

def listarMedicamentos():
    cursor.execute("SELECT * FROM medicamentos")
    resultados = cursor.fetchall()
    for id_medicamento, nome, quantidade in resultados:
        print(f'{id_medicamento} - {nome} - {quantidade}')

def fecharBanco():
    medicamentos.close()
