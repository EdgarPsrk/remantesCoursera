def estrellaDelta(a,b,c):
    rt= a*b+b*c+c*a
    rab= rt/c
    rbc= rt/a
    rca= rt/b
    rt= str(rt)
    rab= str(rab)
    rbc= str(rbc)
    rca= str(rca)
    print('valor Rt:' + rt)
    print('valor Rab:' + rab)
    print('valor Rbc:' + rbc)
    print('valor Rac:' + rca)


r1= float(input("dime Ra: "))
r2= float(input('dime Rb: '))
r3= float(input('dime Rc: '))

estrellaDelta(r1,r2,r3)