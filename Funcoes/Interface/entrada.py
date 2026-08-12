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