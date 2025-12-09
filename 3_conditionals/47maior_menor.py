#Mais leve e mais pesado do grupo
print("-"*30);
print("Qual o maias leve e o mais pesado?");
print("-"*30);

lista=[];
for i in range(1,7):
    peso=float(input(f"Peso da pessoa {i}°: "));
    i+=1;
    lista+=[peso];

maior=max(lista);
menor=min(lista);

print(f"O MAIOR peso é {maior}kg e o MENOR peso é {menor}kg!");