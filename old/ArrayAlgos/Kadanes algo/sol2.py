def kadanesAlgorithm(array):
    csum = array[0]
    osum = array[0]
    
    for i in range(1,len(array)):
        num = array[i]
        csum = max(num,csum + num)
        osum = max(osum,csum)
    return osum
