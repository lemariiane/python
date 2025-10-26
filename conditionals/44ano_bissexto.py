#esse ano é bissexto?
from datetime import date;

ano = int(input("Digite o ano: Coloque 0 para pegar o ano atual. "));
if ano==0:
    ano=date.today().year;
if ano%4==0 and ano%100!=0 or 400==0:#bissexto: de 4 em 4 anos. 
#Exeto em casos do número não for divissível por 100- mas quando ele é divissível  por 400,nesse caso, ele volta a ser bissexto. 
     print(f"Esse ano de {ano} é bissexto");
else:
    print(f"O ano de {ano} não é bissexto!");
