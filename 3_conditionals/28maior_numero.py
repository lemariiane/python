#Qual número é maior e menor dos três?
num1=int(input("Digite o primeiro número: "));
num2=int(input("Digite o segundo número: "));
num3=int(input("Digite o terceiro número: "));

maior=max(num1,num2,num3); #função do python
menor=min(num1,num2,num3);

print(f"O maior é {maior} e o menor número é {menor}");