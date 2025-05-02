a = int(input('enter the number for a : '))
b = int(input('Enter the number for b : '))
c = int(input('Enter the number for c : '))
if a>=b and a>=c:
    print('a is greater')
elif b>=a and b>=c:
    print('b is greater')
else:
    print('c is greater')