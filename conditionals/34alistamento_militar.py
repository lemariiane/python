#ALISTAMENTO MILITAR
from datetime import date;

print("ALISTAMENTO MILITAR OBRIGATÓRIO!"); #alistamento obrigatório: é no ano em que vc completa 18 anos
print("="*35);
ano_nasc=int(input("Digite o ano do seu nascimento: "));# ano de nascimento

ano_atual=date.today().year;
idade = ano_atual - ano_nasc ;

if idade > 18:
    print(f"Você tem {idade} anos e já deveria ter se alistado!");
    print(f"Você deveria ter se alistado a {idade-18} ano(s).");
    print(f"O ano do seu alistamento foi em {ano_atual-(idade-18)}."); 
elif idade < 18:
    print(f"Você tem {idade} anos e ainda não tem idade para se alistar!");
    print(f"Ainda falta(m) {18-idade} ano(s) para o seu alistamento.");
    print(f"Você deverá se alistar no ano de {ano_atual+(18-idade)}.");
else: #idade = 18
    print("Você deve se alistar IMEDIATAMENTE!");
