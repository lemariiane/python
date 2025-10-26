#Média de notas
n1=float(input("Digite a primeira nota: ")); #n1 de número 1
n2=float(input("Digite a segunda nota: ")); #n2 de número 2

media=(n1+n2)/2;

print(f"Tirando as notas {n1} e {n2} a média fica {media}");

if media>=6: #A média é 6 
    print("O aluno foi APROVADO!");
else:
    print("O aluno foi REPROVADO!");
