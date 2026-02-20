def ajuda(parametro):
    help(parametro)

while True:
    parametro=str(input('Função ou Biblioteca > ')).strip()
    if parametro.upper()=='FIM':
        break
    else:
        ajuda(parametro)
        print('-='*30)