# sorteio entre 4 pessoas
import random; #pegar elemento aleatório

nm1=str(input("Digite o primeiro nome: ")); #nm1 é de 'nome' 1
nm2=str(input("Digite o segundo nome: "));
nm3=str(input("Digite o terceiro nome: "));
nm4=str(input("Digite o quarto nome: "));

lista=[nm1,nm2,nm3,nm4];

print (f"O nome escolhido foi {random.choice(lista)}");
