from Funcoes.BD.medicamentos import verificar_estoque
from Funcoes.Interface.menu import cores
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

def selecionar_medicamentos(medicamentos_receita):
    for indice, medicamento in enumerate(medicamentos_receita, start=1):
        print (f'{indice} - {medicamento["nome_do_medicamento"]}')
    print('0 - Não quero comprar nenhum medicamento.')

    total_medicamentos = len(medicamentos_receita)
    escolhas = []
    entrada_valida = False

    while not entrada_valida:
        escolha = input("\nDigite o(s) índice(s) do(s) medicamento(s) que deseja comprar: ")

        try:
            escolhas = [int(x) for x in escolha.split()]
        except ValueError:
            print("Digite apenas números separados por espaço")
            continue

        if not escolhas:
            print("Digite uma entrada válida")
        elif escolhas == [0]:
            entrada_valida = True
        elif 0 in escolhas:
            print("Não é possível combinar '0' com outras opções")
        elif any(i < 1 or i > total_medicamentos for i in escolhas):
            print(f'Digite apenas números entre 1 e {total_medicamentos}, ou 0')
        else:
            entrada_valida = True

    if escolhas == [0]:
        return []

    medicamentos_escolhidos = []

    for i in escolhas:
        medicamento = medicamentos_receita[i-1]
        medicamentos_escolhidos.append(medicamento)

    return(medicamentos_escolhidos)

def definir_quantidades(medicamentos_escolhidos):
    compra = []
    for medicamento in medicamentos_escolhidos:
        loop = True
        while loop: 
            opcao = leiaInt(f'\nQuantas unidades de {medicamento["nome_do_medicamento"]} serão compradas? '
                            f'(Qntd. na receita: {medicamento["quantidade"]} {medicamento["unidade"]}): ')
            tem_estoque = verificar_estoque(
                medicamento["nome_do_medicamento"],
                opcao
            )
            if tem_estoque:
                print(f'{cores["verde"]}Quantidade disponível{cores["limpa"]}')
                compra.append({
                    "nome_do_medicamento": medicamento["nome_do_medicamento"],
                    "quantidade": opcao
                })
                loop = False
            else:
                print(f'{cores["vermelho"]}Quantidade requisitada indisponível.{cores["limpa"]}')
    return compra

def mostrar_resumo(compra_total):
    print("\nResumo da compra: ")
    for indice, medicamento in enumerate(compra_total, start=1):
        print(
            f'{indice} - {medicamento["nome_do_medicamento"]}'
        )
        print(
            f'Quantidade: {medicamento["quantidade"]}\n'
        )

def confirmar_compra():
    loop = True
    print('Deseja confirmar a compra dos remédios selecionados? ')
    print('"S" para confirmar \n"N" para recusar ')
    while loop:
        try:
            opc = input('Sua opção: ').strip().upper()
            if opc == 'S':
                return True
            elif opc == 'N':
                return False
            else:
                print('Entrada inválida. Tente novamente.')
        except(KeyboardInterrupt):
            print('Escolha uma opção, por favor.')