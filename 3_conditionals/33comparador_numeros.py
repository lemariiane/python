#Comparador de números
print("Qual número é maior?");
print("="*25);

n1=int(input("Digite o primeiro valor: "));
n2=int(input("Digite o segundo valor: "));

if n1>n2: #se n1 é maior que n2
    print("O primeiro valor é maior!");
elif n2>n1:
    print("O segundo valor é maior!");
else:
    print("Os valores são iguais");
