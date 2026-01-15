aluno=[]
boletim=[]
media=codigo=stop=0
while True:
    nome=str(input('Nome: '))
    nota1=float(input('Nota 1: '))
    nota2=float(input('Nota 2: '))
    media= (nota1+nota2)/2
    aluno.append(codigo)
    aluno.append(nome)
    aluno.append(nota1)
    aluno.append(nota2)
    aluno.append(media)

    codigo+=1
    boletim.append(aluno[:])
    aluno.clear()

    cont=str(input('Deseja continuar? [S/N] ')).upper().strip()
    while cont not in ('S','N'):
        cont=str(input('DADO INVÁLIDO! Digite apenas "S" OU "N": ')).upper().strip()
    
    if cont=='N':
        break

print('-='*20)
print('Código   Nome       Média')
for i in range(0, len(boletim)):
    print('')
    print(f"{boletim[i][0]:<8}", end=' ')
    print(f"{boletim[i][1]:<10}", end=' ')
    print(f"{boletim[i][4]}")
print('-='*20)

while stop != 999:
    stop=int(input('Digite o código para mostrar as notas do aluno (999 interrompe): '))
    for i in range(len(boletim)):
        if stop == boletim[i][0]:
            print(f'Notas de {boletim[i][1]} são {boletim[i][2]} e {boletim[i][3]}')

print('Volte sempre!')
