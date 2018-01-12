#Insertion Sort usando dois laços "for", sem otimização de código.
def insertionSort (vetor):
    #Vai do segundo elemento do vetor até o ultimo.
    for i in range(1, len(vetor)):
        #???????
        for j in range(i-1, -1,-1):
            #Se o elemento à esquerda do atual, for maior.
            if vetor[j] > vetor[j+1]:
                vetor[j], vetor[j+1] = vetor[j+1],vetor[j]
            else:
                break

#Insertion Sort mais legível, usando um laço "for" e um "while".
def insertionSortWhile (vetor):
    for i in range(1,len(vetor)):
        j = i-1
        while vetor[j] > vetor[j+1] and j>= 0:
            vetor[j], vetor[j+1] = vetor[j+1],vetor[j]
            j -=1

#Insertion Sort otimizado (2x mais rápido)
def insertionSortOtimizado (vetor):
    for i in range(1, len(vetor)):
        atual = vetor[i]
        for j in range(i-1, -1,-1):
            #Se o elemento à esquerda do atual, for maior.
            if vetor[j] > vetor[j+1]:
                vetor[j+1] = vetor[j]
            else:
                vetor[j] = atual
                break
