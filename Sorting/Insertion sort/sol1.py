def InsertionSort(array):
    for i in range(1, len(array)):
        currentValue = array[i]
        currenPosition = i
        while(currenPosition > 0 and array[currenPosition-1]> currentValue):
            array[currenPosition] = array[currenPosition-1]
            currenPosition-=1
        array[currenPosition] = currentValue
    return array