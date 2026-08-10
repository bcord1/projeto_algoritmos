import sqlite3
from pathlib import Path
from Funcoes.Interface.menu import cores

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

        while resultado is None:
            print(f'{cores["vermelho"]}{nome} não encontrado.{cores["limpa"]}')
            novo_nome = input("Digite o nome do remédio manualmente (ou deixe em branco para cancelar): ").strip().upper()

            if not novo_nome:
                conexao.close()
                return False

            cursor.execute("""
                        SELECT * FROM medicamentos
                        WHERE nome = ?
                    """, (novo_nome, ))
            
            resultado = cursor.fetchone()

            if resultado is None:
                print(f'{cores["vermelho"]}{novo_nome} não encontrado.{cores["limpa"]}\n')
            else:
                medicamento["nome_do_medicamento"] = novo_nome
                nome = novo_nome
                
    conexao.close()
    return True

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