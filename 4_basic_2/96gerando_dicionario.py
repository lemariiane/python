from ast import arg

def notas(*nota, sit=False):
    conjunto_notas={}

    conjunto_notas['total']=len(nota)
    conjunto_notas['maior']=max(nota)
    conjunto_notas['menor']=min(nota)
    conjunto_notas['media']=sum(nota)/len(nota)

    if sit:
        if conjunto_notas['media']>7:
            conjunto_notas['situacao']='Boa'
        elif conjunto_notas['media']>5:
            conjunto_notas['situacao']='Razoável'
        else:
            conjunto_notas['situacao']='Ruim'
        
    return conjunto_notas

print(notas(7,8,9, sit=True))