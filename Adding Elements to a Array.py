import array as arr
a = arr.array('i', [1,2,4,9, 5, 3])
print("Array before insertion : ", end=" ")
for i in range(0, 6):
	print(a[i], end=" ")
print()
a.insert(3, 8)
print("Array after insertion : ", end=" ")
for i in (a):
	print(i, end=" ")
print()