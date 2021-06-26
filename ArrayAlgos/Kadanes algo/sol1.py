def kadanesAlgorithm(array):
    # Write your code here.
        csum = array[0]
        osum = array[0]
	
        for i in range(1,len(array)):
            if csum >=0:
                csum+=array[i]
            else:
                csum = array[i]
            if csum > osum:
                osum = csum
        return osum	