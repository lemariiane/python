#IMC
altura=float(input("Digite a altura (m): "));
peso=float(input("Digite o peso (kg): "));

imc=peso/(altura**2);

if imc<18.5:
    print(f"Seu IMC é {imc:.2f} e você está ABAIXO do peso ideal.");
elif imc<25:
    print(f"Seu IMC é {imc:.2f} e você está no peso ideal.");
elif imc<30:
    print(f"Seu IMC é {imc:.2f} e você está  com sobrepeso.");
elif imc<40:
    print(f"Seu IMC é {imc:.2f} e você está com obesidade.");
else:
    print(f"Seu IMC é {imc:.2f} e você está com obesidade mórbida.");
