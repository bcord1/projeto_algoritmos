from Funcoes.Interface.menu import sistema, encerramento
from Funcoes.BD.database import listarMedicamentos, fecharBanco
from Funcoes.Leitura_Processamento.processamento import processar_receita


executando = True

while executando: 
    opc = sistema()

    if opc == 1:
        dados_receita = processar_receita()
        print(dados_receita)
        
    elif opc == 2:
        listarMedicamentos()
        try:
            continuar = input('Deseja continuar? [S/N] ').strip().upper()
        except(TypeError):
            print('Entrada inválida.')
        except(KeyboardInterrupt):
            print('Digite alguma opção.')
        else:
            if continuar == 'S':
                continue
            else:
                encerramento()
                fecharBanco()
                executando = False

    elif opc == 3:
        encerramento()
        fecharBanco()
        executando = False
