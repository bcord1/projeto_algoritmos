from Funcoes.BD.medicamentos import verificar_estoque
from Funcoes.Interface.entrada import leiaInt

def selecionar_medicamentos(medicamentos_receita):
    for indice, medicamento in enumerate(medicamentos_receita, start=1):
        print (indice, medicamento["nome_do_medicamento"])
    print('0 - Não quero comprar nenhum medicamento.')

    escolha = input("Digite os medicamentos")
    escolhas = [int(x) for x in escolha.split()]

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
            opcao = leiaInt(f'Quantas unidades de {medicamento["nome_do_medicamento"]} serão compradas?')
            tem_estoque = verificar_estoque(
                medicamento["nome_do_medicamento"],
                opcao
            )
            if tem_estoque:
                print('Quantidade disponível')
                compra.append({
                    "nome_do_medicamento": medicamento["nome_do_medicamento"],
                    "quantidade": opcao
                })
                loop = False
            else:
                print('Quantidade requisitada indisponível.')
    return compra

def mostrar_resumo(compra_total):
    print("Resumo da compra: ")
    for indice, medicamento in enumerate(compra_total, start=1):
        print(
            f'{indice} - {medicamento["nome_do_medicamento"]}'
        )
        print(
            f'Quantidade: {medicamento["quantidade"]}'
        )

def confirmar_compra():
    loop = True
    print('Deseja confirmar a compra do(s) remédio(s) selecionado(s)? ')
    print('"S" para confirmar \n"N" para recusar ')
    while loop:
        try:
            opc = input('Sua opção: ').strip().upper()
            if opc == 'S':
                return True
            elif opc == 'N':
                return False
            else:
                print('Entrada inválida! Tente novamente.')
        except(KeyboardInterrupt):
            print('Escolha uma opção válida, por favor.')