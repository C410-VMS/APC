users = {
    "Ana": ("ana@gmail.com", "ana123"),
    "Bob": ("bob@hotmail.com", "123bob"),
    "Claudio": ("claudio@bol.com", "clau!*")
}

def login(dicionario:dict)->str:

    email = input("\nDigite o email cadastrado: ")

    for x in dicionario:

        if dicionario[x][0] == email:
            senha = input("\nAgora, digite sua senha: ")
            if senha == dicionario[x][1]:
                return "\nAutenticado!\n"
            else:
                return "\nAcesso negado. Senha incorreta!\n"

    return "\nEmail não encontrado no sistema.\n"
        
print(login(users))