# num = 0
# tot = 0.0
# while True:
#     sval = input('enter a number: ')
#     if sval == 'done':
#         break
#     try:
#         fval = float(sval)
#     except:
#         print('Invalid input')
#         continu
#     print(fval)
#     num += 1
#     tot += fval

# print('ALL donE')
# print(tot,num,tot/num)

largest = None
smallest = None
while True:
    num = input("Enter a number: ")

    if num == "done":
        break

    try:
        not_num = float(num)

    except:
        print('Invalid input')
        continue

    num = int(num)
    if largest == None:
        largest = num
        smallest = num
        #print('first')

    elif num > largest:
        largest = num
        #print('largest')

    elif num < smallest and num < largest:
        smallest = num
        #print('small')



print("Maximum is", largest)
print("Minimum is", smallest)



print("Maximum", largest)
print("minimum", smallest)