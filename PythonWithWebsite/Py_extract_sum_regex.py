fname = input("Enter File Name: ")
fhandle = open(fname)

lines = [line for line in fhandle]

print(lines)