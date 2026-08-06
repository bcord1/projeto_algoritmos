import sqlite3
import sqlite3
from pathlib import Path

caminho_medico = Path(__file__).parent / "medicos.db"


def validar_medico(crm, uf):
    conexao = sqlite3.connect(caminho_medico)
    cursor = conexao.cursor()    

    cursor.execute("""
        SELECT * FROM medicos
        WHERE crm = ? AND uf = ?
    """, (crm, uf))

    resultado = cursor.fetchone
    conexao.close()

    return resultado is not None