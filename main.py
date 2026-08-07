from Funcoes.Interface.menu import sistema, encerramento, deseja_continuar
from Funcoes.Interface.compra import selecionar_medicamentos, definir_quantidades
from Funcoes.BD.criar_medicamentos import listarMedicamentos, fecharBanco
from Funcoes.Leitura_Processamento.processamento import processar_receita
from Funcoes.BD.medicos import validar_medico
from Funcoes.BD.medicamentos import verificar_medicamentos


executando = True

while executando: 
    opc = sistema()

    if opc == 1:
        dados_receita = processar_receita()
        if dados_receita:
            medico_valido = validar_medico(
                dados_receita["crm"],
                dados_receita["uf"]
            )

            if medico_valido:
                remedio_valido = verificar_medicamentos(
                    dados_receita["medicamentos"]
                )

                if remedio_valido:
                    medicamentos_escolhidos = selecionar_medicamentos(
                        dados_receita["medicamentos"]
                    )

                    if medicamentos_escolhidos:
                        compra = definir_quantidades(
                            medicamentos_escolhidos
                        )

                else:
                    print('Foram encontrados medicamentos não cadastrados.')
                    if not deseja_continuar():
                        encerramento()
                        fecharBanco()
                        executando = False

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
