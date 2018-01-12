#Insertion Sort usando dois laços "for", sem otimização de código
def insertionSort (vetor):
    #Vai do segundo elemento do vetor até o ultimo
    for i in range(1, len(vetor)):
        #???????
        for j in range(i-1, -1,-1):
            #Se o elemento à esquerda do atual, for maior
            if vetor[j] > vetor[j+1]:
                vetor[j], vetor[j+1] = vetor[j+1],vetor[j]
            else:
                break
