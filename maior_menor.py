print("-"*30);
print("Qual o maias leve e o mais pesado?");
print("-"*30);

maior=0;
menor=0;

for i in range(1,3):
    peso=float(input(f"Peso da pessoa {i}°: "));
    i+=1;
    if peso>maior:
        maior=peso;
    else:
        menor=peso;

print(f"{maior} e {menor}");