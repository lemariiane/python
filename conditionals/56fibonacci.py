print('SEQUÊNCIA DE FIBONACCI')
qnt=int(input('Deseja ver quantos termos? '))
print('-'*30)

t1=0 
t2=1
i=2

print(t1, t2, end=' ')

while i<qnt:
    t3=t1+t2
    t1=t2
    t2=t3
    print(t3, end=' ')
    i+=1
