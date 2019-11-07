def sum_dig_pow(a, b):
    result_array = []
    pow_num = 0
    while a <= b:
        final_num = 0
        for number in str(a):
            pow_num+=1
            final_num += int(number)**pow_num
        if final_num == a:
            result_array.append(a)
        pow_num = 0; a+=1
    return result_array

print(sum_dig_pow(518,1027))