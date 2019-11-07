def in_array(array1, array2):
    #Creation of result list
    result = []
    
    #Using two for cycles, appending items to result list
    for array1_item in array1:
        for array2_item in array2:
            if array1_item in array2_item:
                result.append(array1_item)
                break
                
    #Erasing duplicity by changing list into dictionary and back
    result = list(dict.fromkeys(result))
    
    #Aplhabeticaly sorting list using list.sort()
    result.sort()
    
    return result