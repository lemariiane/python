#Quantas pessoas temos maiores e menores de idade?
from datetime import date;
print("-"*50);
print("Quantas pessoas são maiores de idade? ")
print("-"*50);

ano_atual=date.today().year;
maior=0;
menor=0;

for i in range(1,8):
    ano_nasc=int(input(f"Digite o ano de nascimento da {i}° pessoa: "));
    i+=1;
    if (ano_atual-ano_nasc)>=18:#maior de 18 anos: maior de idade
        maior+=1;
    else:
        menor+=1;

print(f"Temos {maior} pessoas maior(es) de idade");
print(f"Temos {menor} pessoas menor(es) de idade");
