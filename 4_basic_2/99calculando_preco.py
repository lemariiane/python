import modulo_moeda 

preco=float(input('Digite o preço: '))
print(f'A metade da moeda é R${modulo_moeda.metade(preco)}')
print(f'O dobro é R${modulo_moeda.dobro(preco)}')
print(f'Aumentando 10%, temos R${modulo_moeda.aumento(preco)}')
