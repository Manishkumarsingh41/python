import array as arr
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,12,13,14,15]
a = arr.array('i', l)
print("Initial Array: ")
for i in (a):
    print(i, end=" ")
Sliced_array = a[4:14]
print("\nSlicing elements in a range 4-14: ")
print(Sliced_array)