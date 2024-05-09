print("Gerador de P.A. ")
a1 = int(input("Primeiro termo: "))
r = int(input("Razão: "))
print("Primeiros 10 termos: ")
for i in range(a1, a1 + 10 * r, r):
    print(f"{i} -> ", end='') 
print("PAUSA") 
a1 = a1 + 9 * r
adicional = 1 #valor qualquer somente para inicializar o laço
contador = 0
while adicional != 0:
    a1 = a1 + adicional * r 
    adicional = int(input("Quantos termos você quer mostrar a mais ? "))
    for i in range(a1, a1 + adicional * r, r):
        print(f"{i} -> ", end='')
        contador += 1
    if adicional != 0:
        print("PAUSA")
print(f"A P.A. finalizou mostrando {contador + 10} termos ao todo !")    
print("FIM")
 

