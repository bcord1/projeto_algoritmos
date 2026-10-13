import sqlite3
from pathlib import Path

caminho_medico = Path(__file__).parent / "medicos.db"

def criar_medicos():
    medicos = sqlite3.connect(caminho_medico)
    cursor = medicos.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS medicos(
        crm TEXT NOT NULL,
        uf TEXT NOT NULL,
        PRIMARY KEY(crm, uf)
        )
    """)

    medicosCadastrados = [
        ("806247", "PI"),
        ("354198", "BA"),
        ("642915", "AL"),
        ("918362", "RN"),
        ("275814", "PE"),
        ("483951", "CE"),
        ("123456", "PB")
    ]

    cursor.executemany(
        "INSERT OR IGNORE INTO medicos (crm, uf) VALUES (?, ?)",
        medicosCadastrados
    )

    medicos.commit()
    medicos.close()

criar_medicos()