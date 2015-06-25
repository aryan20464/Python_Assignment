__author__ = 'acer'
largest = None
smallest = None
while True:
    try:
        num = input("Enter a number: ")
        if num == "done" : break
        val = int(num)
        if smallest == None and largest == None:
            smallest=val
            largest=val
        else:
            if val<smallest:
                smallest=val
            if val>largest:
                largest=val
    except ValueError:
        print("Invalid input")
print("Maximum is", largest)
print("Minimum is", smallest)