def bubbleSort(array):
    for j in range(1,len(array)):
        for i in range(len(array)-1):
            if array[i] > array[i+1]:
                array[i] ,array[i+1] = array[i+1],array[i]
    return array