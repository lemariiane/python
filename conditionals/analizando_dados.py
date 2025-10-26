idades=[];
mais_velho=0;
nome_homem=' ';
f_menor=0;

for i in range(1,5):
    print(f'-------{i}° PESSOA-------');
    
    nome=str(input('Digitte o nome: '));
    idade=int(input('Digite a idade: '));
    idades.append(idade);
    print('''[1] Feminino \n[2] Masculino \n[3] Outros \n[4] Prefiro não informar''');
    sexo=int(input('Qual o sexo? '));

    if sexo==1 and idade<20:
        f_menor+=1;

    if sexo==2 and idade>mais_velho:
        mais_velho=idade;
        nome_homem=nome;

media= sum(idades) / len(idades);

print (f'A média de todas a idades é {media}');
print(f'O mais velho dos homens é o {nome_homem} que tem {mais_velho} anos');
print(f'Tem {f_menor} mulheres com menos de 20 anos');