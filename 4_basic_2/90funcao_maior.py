
def descobrindo_maior(*num):
    print('-='*30)
    total=len(num)
    print('Analizando os valolres passados...')
    print(*num)
    print(f'Foram {total} valores ao todo')
    print(f'O maior valor informado foi {max(num)}')

descobrindo_maior(2,9,4,5,7,1)
descobrindo_maior(4,7,0)