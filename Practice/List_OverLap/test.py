a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


my_list=list(range(0,len(b)))


for i in my_list:
    if a[i]==b[i]:
        my_list.append(a[i]);