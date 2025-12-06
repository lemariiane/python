print('-'*30)
print('CAIXA ELETRÔNICO')
print('-'*30)
total=sobrou=0
cedula_um=0
cedula_dez=0
cedula_vinte=0
cedula_cinquenta=0

valor=int(input('Qual o valor que deseja sacar: R$'))

if valor>50:
    cedula_cinquenta=valor//50 #calcula a qauntidade de cédulas
    restante=valor-(cedula_cinquenta*50) #calcula o retante para verficar se há necessidade de ter outra cédula
if restante>=20:
    cedula_vinte=(restante//20)
    restante-=(cedula_vinte*20)
if restante>=10:
    cedula_dez=(restante//10)
    restante-=(cedula_dez*10)
if restante>=1:
    cedula_um=(restante//1)

#só monstra para o usuário se ele receber ao menos 1 cedula do valor
if cedula_cinquenta>1:
    print(f'Total de {cedula_cinquenta} de R$50')
if cedula_vinte>1:
    print(f'Total de {cedula_vinte} de R$20')
if cedula_dez>1:
    print(f'Total de {cedula_dez} de R$10')
if cedula_um>1:
    print(f'Total de {cedula_um} de R$1')
