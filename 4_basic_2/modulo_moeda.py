#módulo usado no exercício 99
#funções para calcular o preço
def metade(preco= 0, formato=False):
    metade_preco=preco/2
    return metade_preco if formato is False else moeda(metade_preco)

def dobro(preco= 0, formato=False):
    dobro_preco=preco*2
    return dobro_preco if formato is False else moeda(dobro_preco)

def aumento(preco= 0, formato=False):
    aumento_preco=(preco*0.1)+preco
    return aumento_preco if formato is False else moeda(aumento_preco)


#formatação do valor 
def moeda(preco = 0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.',',')