from isOdd import isOdd

some_list = [8, 9, 4, 6, 3, 7, 11, 8, 88, 105, 365]
for i in range(len(some_list)):
    print(f'{some_list[i]} =<>= {isOdd(some_list[i])}')