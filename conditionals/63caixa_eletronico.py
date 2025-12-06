#Quantas cédulas de cada valor seram entreges para o usuário?
print('-'*30)
print('CAIXA ELETRÔNICO')
print('-'*30)

# Lista das cédulas disponíveis
cedulas = [50, 20, 10, 1] 
contagem_cedulas = {} 

valor_saque = int(input('Qual o valor que deseja sacar: R$'))
restante = valor_saque

for cedula in cedulas:
    if restante >= cedula:# Verifica se o valor restante é maior ou igual à cédula atual
        quantidade = restante // cedula
        restante = restante % cedula #atualiza o valor do restantate a cada loop
        contagem_cedulas[cedula] = quantidade 

        if quantidade > 0: #só aparece aquelas que o usuário irá receber
            print(f'R${cedula:2d}: {quantidade} cédula(s)')
            
if restante > 0:
    print(f'ATENÇÃO: R${restante} não pôde ser sacado.')

print('-'*30)
