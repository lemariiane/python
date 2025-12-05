print('-'*30)
print('CAIXA ELETRÔNICO')
print('-'*30)
total=sobrou=0
celula_um=int(1)
celula_dez=int(10)
celula_vinte=int(20)
celula_cinquenta=int(50)
valor=int(input('Qual o valor que deseja sacar: R$'))

if valor>50:
    celula_cinquenta=int(valor/50)
    sobrou=valor-(celula_cinquenta*50)

if sobrou%50<=20:
    celula_vinte=int(sobrou/20)
    sobrou=valor-((celula_vinte*20)+(celula_cinquenta*50))

if sobrou%20<=10:
    celula_dez=int(sobrou/10)
    sobrou=valor-((celula_dez*10)+(celula_vinte*20)+(celula_cinquenta*50))

if sobrou%10>=1:
    celula_um=int(sobrou/1)

print(f'{celula_cinquenta}. {celula_vinte}. {celula_dez}. {celula_um}')