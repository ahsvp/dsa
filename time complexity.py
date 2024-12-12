import time
def str_concadinate1(str1,str2):
    start_time = time.perf_counter()
    if str1 is None :
        return str2
    if str2 is None:
        return str1
    len1 =len(str1)
    len2 = len(str2)
    length = max(len1,len2)
    result = []
    
    
    for i in range(length):
        if i < len1:
            result.append(str1[i])
            
            
        if i < len2:
            result.append(str2[i])
    a = ''.join(result)
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time}")
    return a


def str_concadinate2(str1,str2):
    start_time = time.perf_counter()
    if str1 is None :
        return str2
    if str2 is None:
        return str1
    len1 =len(str1)
    len2 = len(str2)
    length = max(len1,len2)
    result = [None]*(2*length)
    result_index = 0
    for i in range(length):
        if i < len1:
            result[result_index] = str1[i]
            result_index += 1
            
        if i < len2:
            result[result_index] = str2[i]
            result_index += 1
    a = ''.join(result[:result_index])
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time}")

    return a
def str_concadinate3(str1,str2):
    start_time = time.perf_counter()
    if str1 is None :
        return str2
    if str2 is None:
        return str1
    len1 =len(str1)
    len2 = len(str2)
    length = max(len1,len2)
    result = ""
    
    
    for i in range(length):
        if i < len1:
            result += str1[i]
            
            
        if i < len2:
            result += str2[i]
    
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time}")

    return result
    
str1 = "fsafwgfsaf"*10000000
str2 = "fsafwgfsaf"*10000000
str_concadinate1(str1,str2)
str_concadinate2(str1,str2)
str_concadinate3(str1,str2)
