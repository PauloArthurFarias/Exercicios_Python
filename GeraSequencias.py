def contador(inicio, fim, passo):
    if inicio > fim:
            if passo > 0:
                passo *= -1
            for i in range(inicio, fim - 1, passo):
                print(i, end=' ')
            print("\n")    
    else:        
        for i in range(inicio, fim + 1, passo):
            print(i, end=' ')
        print("\n")        

contador(1, 10, 1)  #exemplo
contador(10, 0, 2)  #exemplo
contador(20,0,-4)   #exemplo