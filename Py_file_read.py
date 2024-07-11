fname = input("Enter File Name: ")
fhandle = open(fname)

inp = fhandle.read()

inp = inp.rstrip()

print(inp.upper())