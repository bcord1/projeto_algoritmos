from time import sleep

cores = {
"vermelho":"\033[31m",
"verde":"\033[32m",
"amarelo":"\033[33m",
"azul":"\033[34m",
"roxo":"\033[35m",
"ciano":"\033[36m",
"limpa":"\033[m"
}

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except(TypeError, ValueError):
            print('Digite uma entrada válida!')
        except(KeyboardInterrupt):
            print('Usuário não digitou nada.')
            return(0)
        else:
            return(n)

def linha():
    print('-' * 42)

def cabecalho(txt):
    linha()
    print(txt.center(42))
    linha()

def menu():
    cabecalho(f"OPÇÕES")
    opcoes = {
    "1":"Ler receita",
    "2":"Analisar medicações",
    "3":"Sair"
    }
   
    for k, v in opcoes.items():
        print(f"{cores['amarelo']}{k}{cores['limpa']} - {cores['azul']}{v}{cores['limpa']}")
    linha()
    
def sistema():
    print(f"{cores["roxo"]}",end="")
    cabecalho("LEITOR DE RECEITA MÉDICA")
    print(f"{cores["limpa"]}",end="")
    menu()
    while True:
        opc = leiaInt('Sua Opção: ')
        linha()

        if opc in (1, 2, 3):
            return opc

        print(f"{cores["vermelho"]}Opção Inválida! Tente novamente.{cores["limpa"]}")

def encerramento():
    print('Finalizando o sistema', end ='', flush = True)
    for n in range(3):
        sleep(1)
        print('.', end = '', flush = True)
    print('\nAté logo!')

def deseja_continuar():
    loop = True
    while loop:
        try:
            continuar = input('\nDeseja voltar ao menu? [S/N] ').strip().upper()
        except(TypeError):
            print('Entrada inválida.')
        except(KeyboardInterrupt):
            print('Digite alguma opção válida!')
        else:
            if continuar == 'S':
                return True
            elif continuar == 'N':
                return False
            else:
<<<<<<< HEAD
                print('Opção inválida! Digite S ou N.')
=======
                print('Opção inválida, digite S ou N.')

def decidir_apos_quantidade():
    linha()
    print('1 - Ir para o menu e adicionar outra receita à compra')
    print('2 - Finalizar a compra atual')
    linha()
    while True:
        opcao = leiaInt('Sua opção: ')
        if opcao == 1:
            print()
            return True
        elif opcao == 2:
            linha()
            return False
        print(f'{cores["vermelho"]}Opção Inválida! Tente Novamente.{cores["limpa"]}')
>>>>>>> Verificação-de-CRM-lido-errado
