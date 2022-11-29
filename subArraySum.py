def subArraySum(queries, array):
    sum_holder = [0] * len(array)
    zero_indexes = [0] * len(array)
    sum_holder[0] = array[0]
    zero_indexes[0] = 1 if array[0] == 0 else 0 

    for i in range(1, len(array)):
        sum_holder[i] = sum_holder[i - 1] + array[i]
        zero_indexes[i] = zero_indexes[i - 1]
        if array[i] == 0:
            zero_indexes[i] = zero_indexes[i - 1] + 1

    result = []
    for querie in queries:
        begin = querie[0]
        end = querie[1]
        n = querie[2]

        if begin == 0:
            total_value = sum_holder[end] + zero_indexes[end] * n
            result.append(total_value)
        else:
            total_value = sum_holder[end] - sum_holder[begin - 1]
            zeroes = zero_indexes[end] - zero_indexes[begin - 1]
            total_value = total_value + zeroes * n
            result.append(total_value)
    
    return result

print(subArraySum([(2, 6, 1), (0, 3, 5), (5, 11, 3), (0, 12, 2)],[4,2,0,1,5,7,0,8,9,15,-2,0,-1]))

        
