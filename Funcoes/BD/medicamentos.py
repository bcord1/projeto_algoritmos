import sqlite3
from pathlib import Path

caminho_medicamento = Path(__file__).parent / "medicamentos.db"

def verificar_medicamentos(medicamentos_receita):
    conexao = sqlite3.connect(caminho_medicamento)
    cursor = conexao.cursor()

    for medicamento in medicamentos_receita:
        nome = medicamento["nome_do_medicamento"]

        cursor.execute("""
            SELECT * FROM medicamentos
            WHERE nome = ?
        """, (nome, ))

        resultado = cursor.fetchone()

        if resultado is None:
            print(f'{nome} não encontrado.')
            return False
    conexao.close()
    return True