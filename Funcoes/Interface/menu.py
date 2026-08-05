from processamento import processar_receita

cores = {
"vermelho":"\033[31m",
"verde":"\033[32m",
"amarelo":"\033[33m",
"azul":"\033[34m",
"limpa":"\033[m"
}

def linha(tam = 42):
    print( '=' * 42)

def cabecalho(eeuseila):
    linha()
    print(eeuseila.center(42))
    linha()

def menu():
    cabecalho(f"{cores['verde']}Opções{cores['limpa']}")
    opcoes = {
    "1":"Ler receita",
    "2":"Analisar medicações",
    "3":"Sair"
    }
   
    for k, v in opcoes.items():

        print(f"{cores['amarelo']}{k}{cores['limpa']} - {cores['azul']}{v}{cores['limpa']}")
    linha()
    
def sistema():
    
    while True:
        menu()
        opc = int(input("O que deseja ? "))
        if opc == 1:

            return processar_receita()
        elif opc == 2:
            #parte de gugu 
            return print('')
           
        elif opc == 3:
            return print("Encerrando ... Volte sempre.")

sistema()