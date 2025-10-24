nomes=[]
idades=[]
mais_velho=0

for i in range(1,3):
    print(f'-------{i}° PESSOA-------');

    nome=str(input('Digitte o nome: '));
    nomes.append(nome);
    idade=int(input('Digite a idade: '));
    idades.append(idade);
    sexo=str(input('''Escolha o sexo
                   [1] Feminino
                   [2] Masculino
                   [3] Outros
                   [4] Prefiro não informar'''));

    if sexo==2:
        if idade>mais_velho:
            mais_valho=idade;

media= sum(idades) / len(idades);
print (f'A média de todas a idades é: {media}');

