def cat_arrays(arr1, arr2):
    """  concatenates two arrays """

    # copy the first array
    arr3 = arr1[:]

    # add the second array
    arr3.extend(arr2)

    return arr3
