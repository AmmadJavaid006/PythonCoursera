fname = input("Enter File Name: ")
fhandle = open(fname)
count = 0
lst = list()

for addr in fhandle:
    if addr.startswith("From") and not addr.startswith("From:"):
        addr = addr.split()
        lst.append(addr[1])
        count += 1
        
    else:
        continue

for i in lst:
    print(i)

print("There were", count, "lines in the file with From as the first word")

