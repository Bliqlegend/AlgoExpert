def selectionSort(array):
    for i in range(len(array)-1):
        minindex = i
        for j in range(i+1,len(array)):
            if array[j] < array[minindex]:
                minindex = j
        array[i],array[minindex]=array[minindex],array[i]
    return array