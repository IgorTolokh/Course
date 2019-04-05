lst = [i for i in range(25)]
print(max(lst), min(lst))




lst = [i%2 for i in range(len(lst))]
print(lst)




lst = [0 for i in range(len(lst))]
lst[0] = 1
lst[-1] = 1
print(lst)




print(list([i for i in lst if lst.count(i)>1]))




lst = input()
l = len(lst)
print(lst[int(l/2-2):int(l/2+2)])
