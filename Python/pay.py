def computepay(h, r):
    if h >= 40:
        rest = 40*r
        h-=40 
        rateE = 1.5*r
        extra = h*rateE
        rest+=extra
    else:
        rest = r*h
    return rest

hrs = float(input("Enter Hours:"))
rate = float(input("Enter rate:"))
p = computepay(hrs, rate)
print("Pay", p)