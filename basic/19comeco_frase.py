#A cidade começa com 'Santo'?

cidade=str(input("Em que cidade você nasceu? ")).strip(); #strip para tirar os espaços antes e depois
print(cidade[:5].upper() == 'SANTO');
