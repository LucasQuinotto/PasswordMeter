import string

def number_of_Characters(senha):
    count = 0
    for i in range(len(senha)):
        count += 4

    return count


def uppercase_Letters(senha):
    count = 0
    countMaiusculo = 0
    temMaiusculo = False

    for i in range(len(senha)):
        if senha[i] in string.ascii_uppercase:
            countMaiusculo += 1
            temMaiusculo = True

    if temMaiusculo:
        count = (len(senha) - countMaiusculo) * 2

    return count


def lowercase_Letters(senha):
    count = 0
    countMinusculo = 0
    temMinusculo = False

    for i in range(len(senha)):
        if senha[i] in string.ascii_lowercase:
            countMinusculo += 1
            temMinusculo = True

    if temMinusculo:
        count = (len(senha) - countMinusculo) * 2

    return count


def number(senha):
    count = 0
    for i in range(len(senha)):
        if not senha.isdigit() and senha[i] in "0123456789":
            count += 4

    return count


def symbols(senha):
    count = 0
    for i in range(len(senha)):
        if senha[i] not in string.ascii_letters and senha[i] not in "0123456789 _":
            count += 6

    return count


def midle_Numbers_or_Symbols(senha):
    count = 0
    for i in range(1, len(senha) - 1):
        if senha[i] not in string.ascii_letters and senha[i] not in " _":
            count += 2

    return count


def requirements(senha):

    count = 0
    temMaiusculo = False
    temMinusculo = False
    temSimbolo = False
    temNumero = False

    if len(senha) >= 8:

        count += 2

        for i in range(len(senha)):
            if senha[i] in string.ascii_uppercase:
                temMaiusculo = True

            if senha[i] in string.ascii_lowercase:
                temMinusculo = True

            if senha[i] in "0123456789":
                temNumero = True
            if senha[i] not in string.ascii_lowercase and \
                    senha[i] not in string.ascii_uppercase and \
                        senha[i] not in "0123456789 _":
                    temSimbolo = True


        if temMaiusculo:
            count += 2

        if temMinusculo:
            count += 2

        if temNumero:
            count += 2

        if temSimbolo:
            count += 2


    if count < 8:
        count = 0

    return count


def letters_Only(senha):
    count = 0
    for i in range(len(senha)):
        if senha.isalpha():
            count -= 1

    return count


def numbers_Only(senha):
    count = 0
    for i in range(len(senha)):
        if senha.isdigit():
            count -= 1

    return count


def consecutive_Uppercase_Letters(senha):
    count = 0
    for i in range(len(senha) - 1):
        if senha[i] in string.ascii_uppercase and senha[i + 1] in string.ascii_uppercase:
            count -= 2

    return count


def consecutive_Lowercase_Letters(senha):
    count = 0
    for i in range(len(senha) - 1):
        if senha[i] in string.ascii_lowercase and senha[i + 1] in string.ascii_lowercase:
            count -= 2

    return count


def consecutive_Numbers(senha):
    count = 0
    for i in range(len(senha) - 1):
        if senha[i].isdigit() and senha[i + 1].isdigit():
            count -= 2

    return count


def sequential_Letters(senha):
    count = 0
    for i in range(len(senha) - 2):
        if senha[i].isalpha():
            if senha[i:i + 3].upper() in string.ascii_uppercase:
                count -= 3

    return count


def sequential_Numbers(senha):
    count = 0
    for i in range(len(senha) - 2):
        if senha[i].isdigit():
            if senha[i:i + 3] in "0123456789":
                count -= 3

    return count


def executar(senha):

    countTotal = 0
    countTotal += number_of_Characters(senha)
    countTotal += uppercase_Letters(senha)
    countTotal += lowercase_Letters(senha)
    countTotal += number(senha)
    countTotal += symbols(senha)
    countTotal += midle_Numbers_or_Symbols(senha)
    countTotal += requirements(senha)
    countTotal += letters_Only(senha)
    countTotal += numbers_Only(senha)
    countTotal += consecutive_Uppercase_Letters(senha)
    countTotal += consecutive_Lowercase_Letters(senha)
    countTotal += consecutive_Numbers(senha)
    countTotal += sequential_Letters(senha)
    countTotal += sequential_Numbers(senha)

    if countTotal > 100:
        countTotal = 100

    print("count: ", countTotal)
    return countTotal


senha = input("senha: ")
executar(senha)


