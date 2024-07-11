fname = input("Enter file name: ")
fhandle = open(fname)
lst = list()

for line in fhandle:
    words = line.rstrip().split()
    for elements in words:
        if elements in lst:
            continue
        else:
            lst.append(elements)

print(sorted(lst))

########## Can Also be Written As ##########

fname = input("Enter file name: ")
fhandle = open(fname)
lst = list()

for line in fhandle:
    words = line.split()
    for elements in words:
        if not elements in lst:
            lst.append(elements)
        else:
            continue

print(sorted(lst))