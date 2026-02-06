def voto(ano_nasc):
    from datetime import date #só fica na memória durante a execução da def
    ano_atual=date.today().year
    global idade
    idade=ano_atual-ano_nasc
    if idade<16:
        return 'VOTO NEGADO'
    elif (idade>=16 and idade<18) or (idade>70):
        return 'VOTO FACULTATIVO'
    else:
        return 'VOTO OBRIGATÓRIO'


ano_nasc=int(input('Em que ano você nasceu? '))
status=voto(ano_nasc)
print(f'Com {idade} anos: {status}')
 