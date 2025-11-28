print('SEQUÊNCIA DE FIBONACCI')
i=2 #pois já vamos mostrar os dois primeiros termos
a=b=1

qnt=int(input('Digite a quantidade de termos que deseja: '))
print(a,b, end=' ')#primeiros termos sendo mostrados

while qnt>i:
    num=a+b
    a=b #ir mudando a posição a cada loop
    b=num #ir mudando a posição a cada loop
    i+=1
    print(num, end=' ')
