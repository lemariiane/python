listagem=('Lápis', 0.75,
         'Borracha', 0.45,
         'Caderno', 15.00,
         'Estojo', 25.00,
         'Transferidor', 4.25,
         'Compasso', 10.00,
         'Mochila', 49.99,
         'Kit Canetas', 19.99,
         'Livro', 30.25,
         )

print("LISTAGEM DE PREÇO")

for pos in range(0, len(listagem)):
    if pos%2==0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'{listagem[pos]:>6}')
