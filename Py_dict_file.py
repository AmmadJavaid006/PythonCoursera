fname = input("Enter File Name: ")
fhandle = open(fname)
lst = list()
count = dict()
big_val = 0
small_val = 0

for addr in fhandle:
    if addr.startswith("From") and not addr.startswith("From:"):
        addr = addr.split()
        lst.append(addr[1])
    else:
        continue
for mail in lst:
        count[mail] = count.get(mail, 0) + 1
    
big_val = max(count.values())
small_val = min(count.values())

#key = {i for i in count if count[i] == big_val}

for i in count:
    if count[i] == big_val:
        big_key = i
    if count[i] == small_val:
         small_key = i

""" for z in count:
    if count[z] == small_val:
        small_key = z  """
          
print(big_key, big_val)
print(small_key, small_val)