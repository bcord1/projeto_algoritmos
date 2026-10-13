import sqlite3
from pathlib import Path
from .criar_medicos import criar_medicos

caminho_medico = Path(__file__).parent / "medicos.db"
criar_medicos()

def validar_medico(crm, uf):
    if crm is False or uf is False:
        return False


    conexao = sqlite3.connect(caminho_medico)
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT * FROM medicos
        WHERE crm = ?
    """, (crm,))
    crm_existe = cursor.fetchone() is not None

    if not crm_existe:
        conexao.close()
        return "crm_invalido"

    cursor.execute("""
            SELECT * FROM medicos
            WHERE crm = ? AND uf = ?
        """, (crm, uf))
    uf_valida = cursor.fetchone() is not None
    conexao.close()

    if not uf_valida:
        return "uf_invalida"

    return "valido"
