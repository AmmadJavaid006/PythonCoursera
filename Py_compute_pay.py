hrs = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))

def computepay(a, b):

    if hrs > 40:
        pay = (b * 1.5) * (a - 40) + (b * 40)
    elif hrs <= 40:
        pay = a * b
    return pay

print("Pay", computepay(hrs, rate))