def maior(* num):
    maior = 0
    for i in range(0, len(num)):
        if(num[i] > maior):
            maior = num[i]
    return maior

print(maior(10, -5, 2, 0, 10)) #exemplo
print(maior(2, 7, 4)) #exemplo