#Classificando atletas
from datetime import date;
ano_nasc=int(input("Digite o ano de nascimento do atleta: ")); #ano_nasc: ano de nascimento

ano_atual=date.today().year;
idade=ano_atual-ano_nasc;

if idade<=9:
    print(f"Com {idade} ano(s), o atleta é classificado como um atleta mirim!");
elif idade<=14:
    print(f"Com {idade} anos, o atleta é  classificado como um atleta infantil!");
elif idade<=19:
    print(f"Com {idade} anos, o atleta é  classificado como um atleta junior!");
elif idade<=25:
    print(f"Com {idade} anos, o atleta é  classificado como um atleta sênior!");
else:
    print(f"Com {idade} anos, o atleta é  classificado como um atleta master!");
