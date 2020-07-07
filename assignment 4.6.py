def computepay(h,r):
    
    if h > 40:
        p = 40*r+(h-40)*1.5*r
    else:
        p = h * r
    return p
    
h = float(input("Enter Hours:"))
r = float(input("Enter rate per hour:"))

p = computepay(h,r)
print("Pay",p)
