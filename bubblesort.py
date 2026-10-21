class BubbleSort:
    def bubbleSort(self, vet):
        for i in range(len(vet), 1, -1):
            for j in range(i - 1):

                if vet[j] > vet[j + 1]:
                    aux = vet[j]
                    vet[j] = vet[j + 1]
                    vet[j + 1] = aux
        return vet