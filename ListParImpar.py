valores = []
par = []
impar = []
valores.append(par)
valores.append(impar)
i = 1
while True:
    temp = int(input(f"Digite o {i}o. valor: "))
    if temp % 2 == 0:
        par.append(temp)
    else:
        impar.append(temp)       
    if i == 7:
        break
    i+=1
print("Valores Pares: ")
par.sort()
for v in par:
    print(v, end=' ')
print("\nValores Ímpares: ")
impar.sort()
for v in impar:
    print(v, end=' ')            
