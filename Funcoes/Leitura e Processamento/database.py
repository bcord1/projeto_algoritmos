import sqlite3
medicamentos = sqlite3.connect('medicamentos.db')

cursor = medicamentos.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS medicamentos (id INTEGER PRIMARY KEY AUTOINCREMENT,nome TEXT NOT NULL UNIQUE)")

medicamentosAdicionados = [
    "Tylenol",
    "Novalgina",
    "Dorflex",
    "Cataflam",
    "Voltaren",
    "Buscopan",
    "Buscopan Composto",
    "Aspirina",
    "Benegrip",
    "Amoxil",
    "Augmentin",
    "Glifage",
    "Losartan",
    "Norvasc",
    "Lipitor",
    "Plasil",
    "Luftal",
    "Nexium",
    "Puran T4",
    "Rivotril"
]

cursor.executemany(
    "INSERT OR IGNORE INTO medicamentos (nome) VALUES (?)",
    [(medicamento,) for medicamento in medicamentosAdicionados]
)

medicamentos.commit()

def listarMedicamentos():
    cursor.execute("SELECT * FROM medicamentos")
    resultados = cursor.fetchall()
    for linha in resultados:
        print(linha)

def fecharPrograma():
    print("Até logo!\n\nEncerrando programa...")
    return medicamentos.close()