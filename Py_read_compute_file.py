fname = input("Enter File Name: ")
fhandle = open(fname)
count = 0
total = 0

for line in fhandle:

    if line.startswith("X-DSPAM-Confidence:"):
        
        t = line.find("0")
        number = float(line[t : ])
        count = count + 1
        total = total + number
avg = total/count
print("Average spam confidence:", avg)

