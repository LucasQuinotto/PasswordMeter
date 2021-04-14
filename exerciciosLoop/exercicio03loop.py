import string

alfabeto = list(string.ascii_lowercase)

palavra = input("Digite uma palavra: ")

novaPalavra = []

for i in range(len(palavra)):

    numeroLetra = alfabeto.index(palavra[i])

    if palavra[i] in "aeiou":
        numeroLetra -= 4
        if numeroLetra < 0:numeroLetra += 26
    else:
        numeroLetra += 9
        if numeroLetra < 0:
             numeroLetra += 26
        elif numeroLetra > 25:
             numeroLetra -= 26

    novaPalavra.append(alfabeto[numeroLetra])

print("".join(novaPalavra))

