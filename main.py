from Funcoes.Interface.menu import sistema, encerramento
from Funcoes.BD.database import listarMedicamentos, fecharBanco


executando = True

while executando: 
    opc = sistema()

    if opc == 1:
        print('a')

        
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
