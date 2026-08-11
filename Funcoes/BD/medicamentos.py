import sqlite3
from pathlib import Path
from Funcoes.Interface.menu import leiaInt

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

def buscar_medicamento_nome():
    conexao = sqlite3.connect(caminho_medicamento)
    cursor = conexao.cursor()
    nome_busca = input("Digite o nome do medicamento: ")
    cursor.execute("""
        SELECT nome FROM medicamentos 
        WHERE nome = ?
    """, (nome_busca,))
    medicamento = cursor.fetchone()

    if medicamento:
        conexao.close()
        return f"Medicamento encontrado!/n {medicamento[1]}"

    conexao.close()
    return 'Não possuímos este medicamento no estoque!'

def buscar_medicamento_id():
    conexao = sqlite3.connect(caminho_medicamento)
    cursor = conexao.cursor()

    id_busca = leiaInt("Digite o ID do medicamento: ")
    cursor.execute("""
        SELECT nome FROM medicamentos WHERE id = ?
        """, (id_busca,))

    medicamento = cursor.fetchone()

    if medicamento:
        conexao.close()
        return f"Medicamento encontrado!/n {medicamento[0]}"
    conexao.close()
    return 'Não possuímos este medicamento no estoque!'

def verificar_estoque(nome, quantidade):
    conexao = sqlite3.connect(caminho_medicamento)
    cursor = conexao.cursor()
    cursor.execute("""
        SELECT quantidade FROM medicamentos
        WHERE nome = ?
    """, (nome,))

    resultado = cursor.fetchone()
    if resultado is None:
        return False

    estoque = resultado[0]

    if estoque >= quantidade:
        return True
    else:
        return False

def baixar_estoque(compratotal):
    conexao = sqlite3.connect(caminho_medicamento)
    cursor = conexao.cursor()

    for medicamento in compratotal:
        nome = medicamento["nome_do_medicamento"]
        quantidade = medicamento["quantidade"]
        cursor.execute("""
            UPDATE medicamentos
            SET quantidade = quantidade - ?
            WHERE nome = ?
        """, (quantidade, nome))

    conexao.commit()
    conexao.close()