numero_extenso=('zero','um','dois','três','quatro','cinco', 'seis', 'sete', 
                'oito', 'nove', 'dez', 'onze','doze treze', 'quartorze', 'quinze', 'desesseis',
                'desessete', 'dezoito', 'desenove','vinte')

numero=int(input('Digite um número entre o e 20: '))

while True:
    if 0 <= numero <=20:
        break
    numero=int(input('Valor inválido! Digite um número de 0 a 20: '))

print(f'Você digitou o número {numero_extenso[numero]}')
