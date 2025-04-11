def bubble_sort(data_list):#comparing consecutive values
    for x in range(1,len(data_list)):#number of rounds , rounds must be length of data_list - 1
        for i in range(len(data_list)-x):#we need to decrease 1 number of comparisions
            if data_list[i]>data_list[i+1]:
                data_list[i], data_list[i+1]= data_list[i+1],data_list[i]
    return data_list

def modified_bubble_sort(data_list):#comparing consecutive values
    flag = False
    for x in range(1,len(data_list)):#number of rounds , rounds must be length of data_list - 1
        flag = False
        for i in range(len(data_list)-x):#we need to decrease 1 number of comparisions
            if data_list[i]>data_list[i+1]:
                data_list[i], data_list[i+1]= data_list[i+1],data_list[i]
                flag=True
        if not flag:
            break
    return data_list

result = bubble_sort([34,76,12,89,25,35,50])
result_1 = modified_bubble_sort([34,76,12,89,25,35,50])
print(result)
print(result_1)

# [12, 25, 34, 35, 50, 76, 89]
# [12, 25, 34, 35, 50, 76, 89]