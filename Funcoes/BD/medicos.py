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

<<<<<<< HEAD
    cursor.execute("SELECT * FROM medicos WHERE crm = ?", (crm,))
    resultados = cursor.fetchall()

    for linha in resultados:
        if linha[0] == crm_receita:
            crm_encontrado = True
            print(f"Encontrei um CRM igual! UF cadastrada", linha[1])

            if linha[1] == uf_receita:
                uf_encontrado = True
                print(f"Encontrei uma UF igual!")

    if not crm_encontrado:
        print("Não encontrei um CRM igual no sistema!")
    if not uf_encontrado:
        print("Não encontrei um UF igual para o CRM informado!")

    if uf_encontrado:
        print("Validação Concluida com sucesso!")
    else:
        print("CRM Inválido!")

    conexao.close()
    return uf_encontrado
=======
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
>>>>>>> Verificação-de-CRM-lido-errado
