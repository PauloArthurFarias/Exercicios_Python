lista = []
maiores = []
menores = []
for i in range(0,5):
    lista.append(int(input(f"Digite um valor para a posição {i}: ")))
ordenado = sorted(lista)
maior = ordenado[4]
menor = ordenado[0]
for i in range(0, len(lista)):
    if lista[i] == maior:
        maiores.append(i)
    elif lista[i] == menor:
        menores.append(i)
print(f"O maior número é {maior} e ele aparece na lista nas posições {maiores}")
print(f"O menor número é {menor} e ele aparece na lista nas posições {menores}")