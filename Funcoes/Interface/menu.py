from time import sleep
from Funcoes.BD.medicamentos import buscar_medicamento_nome, buscar_medicamento_id
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
    "3":"Buscar medicamento",
    "4":"Sair"
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

        if opc in (1, 2, 3, 4):
            return opc

        print(f"{cores["vermelho"]}Opção Inválida! Tente novamente.{cores["limpa"]}")

def opc_busca():
    print("OPÇÕES DE BUSCA:")
    print("1: Buscar medicamento por ID")
    print("2: Buscar medicamento por nome")
    opc_selecionada = leiaInt("De que maneira deseja buscar? ")

    while opc_selecionada != 1 or 2:
        print(f"{cores["vermelho"]}Opção Inválida! Tente novamente.{cores["limpa"]}")
        opc_selecionada = leiaInt("De que maneira deseja buscar? ")

    if opc_selecionada == 1:
        return buscar_medicamento_id()
    return buscar_medicamento_nome()

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
            continuar = input('Deseja continuar? [S/N] ').strip().upper()
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
                print('Opção inválida! Digite S ou N.')
