list1 = [1, 2, 3,4]
list2 = [5, 6, 7,8,9]
list3 = [10, 11, 12, 13, 14, 15]
list4 = [16, 17, 18,19,20]
set1 = set(list2)
set2 = set(list1)
set1.update(set2)
print(set1)
set1.update(list3)
print(set1)
set1.update(list4)
print(set1)
