fator=int(input('Digite o número da tabuada: ')) 
cont=0
while fator<0:
   
    for cont in range(0,10):
        print(f'{fator}X{cont}={fator*cont}')
        cont+=1    

fator=int(input('Digite o número da tabuada: '))
