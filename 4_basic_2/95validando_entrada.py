def leiaInt(num):
    ok=False
    valor=0

    while True:
        num=str(input(num))
        if num.isnumeric():
            valor=int(num)
            ok=True
        else:
            print('ERRO! Digite um número inteiro válido!')
        if ok:
            break
    return valor

num = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {num}')