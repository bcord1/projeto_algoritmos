cores = {
"vermelho":"\033[31m",
"verde":"\033[32m",
"amarelo":"\033[33m",
"azul":"\033[34m",
"roxo":"\033[35m",
"ciano":"\033[36m",
"limpa":"\033[m"
}

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
        opc = int(input(f"{cores["verde"]}Sua Opção: {cores["limpa"]}"))
        linha()
        if opc == 1:
            pass
        #parte do nosso mano bento
        elif opc == 2:
            pass
        # return listarRemedios()
        elif opc == 3:
            return print(f"{cores["ciano"]}Encerrando... Volte sempre.{cores["limpa"]}")
            #return database.fecharPrograma()
        #feito no arquivo 'database'
        else:
            print(f"{cores["vermelho"]}Opção Inválida! Tente novamente.{cores["limpa"]}")