import sqlite3
from pathlib import Path

caminho_medico = Path(__file__).parent / "medicos.db"

def validar_medico(crm, uf):
    if crm is False or uf is False:
        return False

    crm_receita = str(crm).strip()
    uf_receita = str(uf).strip()
    
    crm_encontrado = False
    uf_encontrado = False

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
