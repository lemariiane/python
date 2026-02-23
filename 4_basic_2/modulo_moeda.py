#módulo usado nos exercícios 99 e 100

#funções para calcular o preço (exercício 99)
def metade(preco= 0, formato=False):
    metade_preco=preco/2
    return metade_preco if formato is False else moeda(metade_preco)

def dobro(preco= 0, formato=False):
    dobro_preco=preco*2
    return dobro_preco if formato is False else moeda(dobro_preco)

def aumento(preco= 0, taxa=10, formato=False):
    aumento_preco=preco+(preco*(taxa/100))
    return aumento_preco if formato is False else moeda(aumento_preco)

def reducao(preco= 0, taxa=5, formato=False):
    reducao_preco=preco-(preco*(taxa/100))
    return reducao_preco if formato is False else moeda(reducao_preco)

#resumo do preço (exercício 100)
def resumo(preco=0, taxaaum=10, taxared=5):
    print('=-'*30)
    print('RESUMO DO VALOR'.center(20))
    print('=-'*30)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco,True)}')
    print(f'Metade do preço: \t{metade(preco,True)}')
    print(f'{taxaaum}% de aumento: \t{aumento(preco,taxaaum,True)}')
    print(f'{taxared}% de redução: \t{reducao(preco,taxared,True)}')



#formatação do valor 
def moeda(preco = 0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.',',')