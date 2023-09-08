import os.path
import sys

fname = input("Enter the filename whose contents are to be sorted: ")

if not os.path.isfile(fname):
    print("File", fname, "doesn't exist")
    sys.exit(0)

infile = open(fname, "r")
myList = infile.readlines()
print(myList)


lineList = []
for line in myList:
    lineList.append(line.strip())

lineList.sort()

outfile = open("sorted.txt", "w")
for line in lineList:
    outfile.write(line + "\n")

infile.close()  
outfile.close()  

if os.path.isfile("sorted.txt"):
    print("\nFile containing sorted content sorted.txt created successfully")
    
print("sorted.txt contains", len(lineList), "lines")
print("Contents of sorted.txt")
print("=====================")

rdFile = open("sorted.txt", "r")
for line in rdFile:
    print(line, end="")
