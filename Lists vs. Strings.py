import copy
Ex_1=[2,3,4,5,6]
Ex_2=copy.deepcopy(Ex_1)
Ex_2[3]=7
Ex_3=Ex_2
Ex_3[2]=9
Ex_4=Ex_3
Ex_4[3]=8
print("Exercise 1:", Ex_1)
print("Exercise 2:", Ex_2)
print("Exercise 3:", Ex_3)
print("Exercise 4:", Ex_4)