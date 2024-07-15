import re
fname = input("Enter File Name: ")
fhandle = open(fname)

lines = [line.strip() for line in fhandle] # Stores each line in 'Lines'
sen = re.findall("[0-9]+", str(lines)) # By the help of Reguar Expression we find all the Numbers

nums = [int(num) for num in sen] # Changes the numbers into Int's (Integers)

print(sum(nums))

############################## Another way to do this with 'For Loop' ##############################

import re

fname = input("Enter File Name: ")
fhandle = open(fname)
lst = list()
sum = 0

for line in fhandle: # Finds all the Numbers
    sen = re.findall("[0-9]+", line)
    lst.append(sen)

lstclone = lst.copy()
lstclone.clear()

for filter in lst: # Filters the list means removes "[]"
    if filter == []:
        continue
    else:
        lstclone.append(filter)

for nums in lstclone: # Sums all the numbers up
    for finalnums in nums:
        sum += int(finalnums)

print(sum)