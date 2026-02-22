import modulo_moeda as m

preco=float(input('Digite o preço: R$'))
print(f'A metade da moeda é {m.metade(preco, True)}')
print(f'O dobro é {m.dobro(preco, True)}')
print(f'Aumentando 10%, temos {m.aumento(preco, True)}')
