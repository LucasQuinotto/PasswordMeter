lutadores = []
contador = 1

for i in range(int(input("Quantos lutadores entrarão na arena?\n"))):
    lutadores.append(int(input("Novo lutador: ")))

while len(lutadores) > 1:
    roundAtual = lutadores.copy()
    print(f"{contador}° Round: {lutadores}")
    contador += 1
    if len(roundAtual) % 2 == 1:
        roundAtual.append(0)
    lutadores.clear()
    for i in range(0,len(roundAtual),2):
        if roundAtual[i] != roundAtual[i + 1]:
            vencedor = max(roundAtual[i],roundAtual[i + 1])
            lutadores.append(vencedor)
        else:
            pass
else:
    print(f"{contador}° Round: {lutadores}")
