__author__ = 'acer'
gr = float(input("enter grade"))
if gr>1.0 or gr<0.0:
    print("Error")
elif gr>=0.9:
    print("A")
elif gr>=0.8:
    print("B")
elif gr>=0.7:
    print("C")
elif gr>=0.6:
    print("D")
elif gr<0.6:
    print("F")
else:
    print("asdklfj")