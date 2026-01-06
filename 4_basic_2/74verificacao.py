#Verifica se os parênteses da expressão estão bem organizados, 
#garantindo que cada parêntese aberto seja fechado e na ordem certa.
expressao=str(input('Digite a expressão: '))
pilha=[]
for parenteses in expressao:
    if parenteses == '(':
        pilha.append('(')
    elif parenteses == ')':
        if len(pilha)>0:
            pilha.pop()
        else:
            pilha.append(')')
            break
        
if len(pilha)==0:
    print('Sua expressão é VÁLIDA!')
else:
    print('Sua expressão é INVÁLIDA!')
