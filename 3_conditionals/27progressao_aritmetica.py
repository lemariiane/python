#Progressão aritmética

print("="*25);
print("10 TERMOS DE UMA PA");
print("="*25);

termo1=int(input("Digite o primeiro termo: "));
razao=int(input("Digite a razão: "));

for i in range(10):
    termo= termo1 + i * razao;
    print(termo, end=" -> ");
print("ACABOU");