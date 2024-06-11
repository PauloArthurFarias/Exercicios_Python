print("MATRIZ 3x3")
matriz = [[], [], []] #cada sublista é uma linha
for i in range(0,len(matriz)):
    for j in range(0,len(matriz)):
        matriz[i].append(input(f"Digite o elemento A{i+1}x{j+1}: "))
for i in range(0,len(matriz)):
    print()
    for j in range(0,len(matriz)):
        print(f"[{matriz[i][j]}]", end=' ')