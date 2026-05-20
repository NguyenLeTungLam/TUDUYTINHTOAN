def merge(arr1 , arr2 ):
    res = []
    if arr1[0] < arr1[-1]:
        i = j = 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                res.append(arr1[i])
                i += 1
    else:
        while i < len(arr1) and j < arr2