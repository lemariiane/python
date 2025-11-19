print('GERADOR DE PA')

num=int(input('Digite o primeiro termo: '))
razao=int(input('Digite a razão da PA: '))
i=0
progressao=0

while i<10:
    progressao=num +i*razao
    print(progressao, end=" ")
    i+=1
