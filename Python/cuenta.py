
def element2(a,b):
    numerador=a*b
    denominador=a+b
    rest=numerador/denominador

    return str(rest)


def element3(a,b,c):
    numerador=a*b*c
    denominador= (a*b)+(b*c)+(c*a)
    rest=numerador/denominador

    return str(rest)

def element4(a,b,c,d):
    numerador=a*b*c*d
    denominador=(a*b*c)+(b*c*d)+(a*c*d)+(a*b*d)
    rest=numerador/denominador

    return str(rest)


def element5(a,b,c,d,e):
    numerador=a*b*c*d*e  
    denominador=(a*b*c*d)+(b*c*d*e)+(a*c*d*e)+(a*b*d*e)+(a*b*c*e)
    rest=numerador/denominador

    return str(rest)


def element6(a,b,c,d,e,f):
    numerador=a*b*c*d*e*f 
    denominador=(a*b*c*d*e)+(a*b*c*d*f)+(a*b*c*e*f)+(a*b*d*e*f)+(a*c*d*e*f)+(b*c*d*e*f)
    rest=numerador/denominador

    return str(rest)


r1=220
r2=89.81
r3=523.48
r4=1
r5=1
r6=1

r12=element2(r1,r2)
r123=element3(r1,r2,r3)
# r1234=element4(r2,r3,r4,r5)
# r12345=element5(r1,r2,r3,r4,r5)
# r123456=element6(r1,r2,r3,r4,r5,r6)


print('Ra='+ r12)
print('Rb='+ r123)
# print('Rc='+ r1234)
# print('Rd='+ r12345)


