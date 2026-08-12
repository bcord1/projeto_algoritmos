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
            resultado_medico = validar_medico(
                dados_receita["crm"],
                dados_receita["uf"]
            )

            if resultado_medico == "crm_invalido":
                print(f'{cores["vermelho"]}Receita Inválida: CRM não encontrado.{cores["limpa"]}')
            elif resultado_medico == "uf_invalida":
                print(f'{cores["vermelho"]}Receita inválida: UF não corresponde ao CRM informado.{cores["limpa"]}')

            while resultado_medico in ("crm_invalido", "uf_invalida"):
                if resultado_medico == "crm_invalido":
                    novo_valor = input ("Digite o CRM manualmente (ou deixe em branco para cancelar): ").strip()

                    if not novo_valor:
                        resultado_medico = "cancelado"
                    else:
                        resultado_medico = validar_medico(novo_valor, dados_receita["uf"])

                        if resultado_medico == "valido":
                            dados_receita["crm"] = novo_valor
                        elif resultado_medico == "crm_invalido":
                            print(f'{cores["vermelho"]}CRM não encontrado. Tente novamente{cores["limpa"]}')
                        elif resultado_medico == "uf_invalida":
                            dados_receita["crm"] = novo_valor
                            print(f'{cores["vermelho"]}CRM encontrado, mas não corresponde à UF informada.{cores["limpa"]}')

                elif resultado_medico == "uf_invalida":
                    novo_valor = input("Digite a UF manualmente (ou deixe em branco para cancelar): ").strip().upper()

                    if not novo_valor:
                        resultado_medico = "cancelado"
                    else:
                        resultado_medico = validar_medico(dados_receita["crm"], novo_valor)

                        if resultado_medico == "valido":
                            dados_receita["uf"] = novo_valor
                        elif resultado_medico == "uf_invalida":
                            print(f'{cores["vermelho"]}UF não corresponde. Tente novamente.{cores["limpa"]}')
                        elif resultado_medico == "crm_invalido":
                            print(f'{cores["vermelho"]}CRM também não encontrado com essa UF.{cores["limpa"]}')

            if resultado_medico == "valido":
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
                        executando = False

            elif resultado_medico == "cancelado":
                print(f'{cores["vermelho"]}Receita Inválida.{cores["limpa"]}')
                if not deseja_continuar():
                    executando = False
        
    elif opc == 2:
        listarMedicamentos()
        
        if not deseja_continuar():
            executando = False

    elif opc == 3:
        executando = False

fecharBanco()

if compra_total:
    mostrar_resumo(compra_total)
    if confirmar_compra():
        baixar_estoque(compra_total)
        print(f'{cores["verde"]}\nCompra efetuada com sucesso!{cores["limpa"]}')
    else: 
        print(f'{cores["vermelho"]}\nCompra cancelada!{cores["limpa"]}')
else:
    print('Nenhum medicamento foi comprado.')

encerramento()