def somar(numero01, numero02):
    print("resultado: ", numero01 + numero02)

def subtrair(numero01, numero02):
    print("resultado: ", numero01 - numero02)

def multiplicar(numero01, numero02):
    print("resultado: ", numero01 * numero02)

def dividir(numero01, numero02):
    print("resultado: ", numero01 / numero02)

metodo = 0

while metodo != 5:

    metodo = int(input("\n Escolha um método:\n"
                   "1 -> somar\n"
                   "2 -> subtrair\n"
                   "3 -> multiplicar\n"
                   "4 -> dividir\n"
                   "5 -> sair\n"
                   " método: "))

    if metodo < 5:
        numero01 = int(input("\nDigite um número: "))
        numero02 = int(input("Agora, digite outro: "))
        if metodo == 1:
            somar(numero01, numero02)
        elif metodo == 2:
            subtrair(numero01, numero02)
        elif metodo == 3:
            multiplicar(numero01, numero02)
        elif metodo == 4:
            dividir(numero01, numero02)
    elif metodo > 5:
        print("\nOperação invalida ...")
        resultado = 0

print("\nEncerrando sessão ...")