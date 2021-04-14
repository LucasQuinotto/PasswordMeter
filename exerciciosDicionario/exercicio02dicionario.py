def cadastroPessoa():
    nome = input("\nNome: ")
    idade = int(input("Idade: "))
    cpf = input("Cpf: ")
    if cpf in totalPessoas:
        print("Cpf já cadastrado ...")
    else:
        totalPessoas[cpf] = {"nome": nome, "idade": idade, "cpf": cpf}

def consultaPessoa():
    consultaCpf = input("\nCpf da pessoa: ")
    if consultaCpf in totalPessoas:
        print("\nCadastro consultado: ", totalPessoas[consultaCpf])
    else:
        print("\nCpf não cadastrado ...")

def alteraPessoa():
    alteraCpf = input("\nCpf da pessoa: ")
    if alteraCpf in totalPessoas:
        nome = input("\nNovo nome: ")
        idade = int(input("Nova idade: "))
        totalPessoas[alteraCpf] = {"nome": nome, "idade": idade, "cpf": alteraCpf}
        print("Cadastro alterado: ", totalPessoas[alteraCpf])
    else:
        print("\nCpf não cadastrado ...")

def listaPessoa():
    print("\n Listagem: ")
    for i in totalPessoas:
        print("\n", totalPessoas[i])

def excluiPessoa():
    excluirPessoa = input("\nCpf da pessoa: ")
    if excluirPessoa in totalPessoas:
        print("\nCadastro Excluido: ", totalPessoas[excluirPessoa])
        totalPessoas.pop(excluirPessoa)
    else:
        print("\nCpf não cadastrado ...")

totalPessoas = {}
opcao = 0

while opcao != 6:
    opcao = int(input("\n Escolha uma opção:\n\n"
                  "1 -. Cadastro\n"
                  "2 -> Consulta\n"
                  "3 -> Alteração\n"
                  "4 -> Listagem\n"
                  "5 -> Exclusão\n"
                  "6 -> Sair\n\n"
                  " Opção: "))
    if opcao == 1:
        cadastroPessoa()
    elif opcao == 2:
        consultaPessoa()
    elif opcao == 3:
        alteraPessoa()
    elif opcao == 4:
        listaPessoa()
    elif opcao == 5:
        excluiPessoa()
