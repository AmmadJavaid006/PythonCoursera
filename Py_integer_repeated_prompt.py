largest_num = None
smallest_num = None

while True:
    num = input("Enter Number or 'Done' for exit: ")

    if num == "Done" or num == "done" or num == "DONE":
        #print("DONE")
        break
    
    try:
        num = int(num)

        if smallest_num is None:
            largest_num = num
            smallest_num = num
        elif num < smallest_num:
            smallest_num = num
        elif num > largest_num:
            largest_num = num
    
    except:
        print("Invalid input")

print("Maximum is", largest_num)
print("Minimum is", smallest_num)


