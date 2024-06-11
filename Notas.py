def notas(*num, sit = False):
    resumo = dict()
    resumo["total"] = len(num)
    resumo["maior"] = max(num)
    resumo["menor"] = min(num)
    total = 0
    for n in num:
        total += n
    resumo["media"] = float(total / len(num)) 
    if sit == True: 
        if resumo["media"] >= 7:
            resumo["sit"] = 'Boa'
        else:
            resumo["sit"] = 'Ruim'    
    return resumo

print(notas(4.5, 6.8, 10, sit = True)) #Exemplo