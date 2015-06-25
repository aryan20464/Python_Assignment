__author__ = 'acer'
def compute_pay(h,r):
    if h <= 40:
        pay = h * r
    elif h> 40:
        pay = 40 * r + (h-40) * (r * 1.5)
    return(pay)

hrs = input("Enter Hours:")
h = float(hrs)
rate = input("enter rate")
r = float(rate)
p = compute_pay(h,r)
print(p)