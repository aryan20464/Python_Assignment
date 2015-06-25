__author__ = 'acer'
hrs = input("Enter Hours:")
h = float(hrs)
rate = input("enter the rate")
r = float(rate)
if h <= 40.0:
    print(r * h)
elif h > 40:
    print(r * 40 + (h-40) * r*1.5)
