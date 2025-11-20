num=int(input('Digite o primeiro termo: '))
razao=int(input('Digite a razão: '))
qnttermo=int(input('Digite a quantidade de termos: '))
cont=True

while cont==True:
    for i in range(qnttermo):
        print(num+i*razao, end=' - ')
        i+=1

    if qnttermo!=0:
        qnttermo=int(input('\nDeseja mostrar mais ou menos termos? Digite a quantidade desejada: '))
        cont==True
    else:
        cont=False
print('Programa encerrado! Volte sempre!')    