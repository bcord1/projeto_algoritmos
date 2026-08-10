from Funcoes.Interface.menu import sistema, encerramento, deseja_continuar, decidir_apos_quantidade, cores
from Funcoes.Interface.compra import selecionar_medicamentos, definir_quantidades, mostrar_resumo, confirmar_compra
from Funcoes.BD.criar_medicamentos import listarMedicamentos, fecharBanco
from Funcoes.Leitura_Processamento.processamento import processar_receita
from Funcoes.BD.medicos import validar_medico
from Funcoes.BD.medicamentos import verificar_medicamentos, baixar_estoque


executando = True
compra_total = []

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
                print(f'{cores["verde"]}\nReceita Válida\n{cores["limpa"]}')
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
                        compra_total.extend(compra)

                        if not decidir_apos_quantidade():
                            executando = False

                else:
                    print('Foram encontrados medicamentos não cadastrados.')
                    if not deseja_continuar():
                        encerramento()
                        fecharBanco()
                        executando = False

            else:
                print(f'{cores["vermelho"]}\nReceita Inválida{cores["limpa"]}')
                if not deseja_continuar():
                    encerramento()
                    fecharBanco()
                    executando = False
        
    elif opc == 2:
        listarMedicamentos()
        
        if not deseja_continuar():
            encerramento()
            fecharBanco()
            executando = False

    elif opc == 3:
        executando = False

if compra_total:
    mostrar_resumo(compra_total)
    if confirmar_compra():
        baixar_estoque(compra_total)
        print(f'{cores["verde"]}\nCompra efetuada com sucesso!{cores["limpa"]}')
    else: 
        print(f'{cores["vermelho"]}\nCompra cancelada!{cores["limpa"]}')
else:
    print('Nenhum medicamento foi comprado.')

fecharBanco()
encerramento()