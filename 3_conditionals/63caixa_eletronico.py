#Quantas cédulas de cada valor seram entreges para o usuário?
print('-'*30)
print('CAIXA ELETRÔNICO')
print('-'*30)

cedulas=[50,20,10,1]
contagem_cedulas={}#dicionário

valor_sacado=int(input('Digite o valor que deseja saca: [somente valor inteiro] '))
resto=valor_sacado

for cedula in cedulas:
    qnt_cedula=resto//cedula #divisao inteira
    resto=resto-(qnt_cedula*cedula) #calcula quanto que ainda falta
    contagem_cedulas[cedula] = qnt_cedula 

    if qnt_cedula>0:
        print(f'O total de {qnt_cedula} de R${cedula}')
