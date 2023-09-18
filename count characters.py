s=input("Enter any string:-")
d=dict()
for ch in s:
    if(ch not in d):
        d[ch]=1
    else:
        d[ch]+=1
print(d)
