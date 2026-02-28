import modulo_moeda as m

preco=m.leiaDinheiro('Digite o preço: R$')
taxaaum=float(input('Digite a porcentagem do aumento: '))
taxared=float(input('Digite a porcentagem da redução: '))
m.resumo(preco,taxaaum,taxared)
