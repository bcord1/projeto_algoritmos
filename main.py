from Funcoes.Interface.menu import sistema, encerramento, deseja_continuar
from Funcoes.BD.database import listarMedicamentos, fecharBanco
from Funcoes.Leitura_Processamento.processamento import processar_receita
from Funcoes.BD.medicos import validar_medico


executando = True

while executando: 
    opc = sistema()

    if opc == 1:
        dados_receita = processar_receita()
        if dados_receita:
            valido = validar_medico(
                dados_receita["crm"],
                dados_receita["uf"]
            )

            if valido:
                print('Receita válida')
            else:
                print('Receita inválida')
                if not deseja_continuar():
                    encerramento()
                    fecharBanco()
                    executando = False
        
    elif opc == 2:
        listarMedicamentos()
        o = deseja_continuar()
        if not deseja_continuar():
            encerramento()
            fecharBanco()
            executando = False

    elif opc == 3:
        encerramento()
        fecharBanco()
        executando = False
