#Preço da viagem
km=float(input("Quantos km são a sua viagem? "));

print(f"Você está prestres a realizar uma viagem de {km}km");

if km<200: #se a viagem for até 200km a taxa é 0.5, se não é 0.45
    print(f"Sua viagem irá custar R${km*0.5}");
else:
    print(f"Sua viagem irá custar R${km*0.45}");
