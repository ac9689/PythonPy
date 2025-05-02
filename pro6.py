# user input
name = input("enter the name : ")
print("hello", name)
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)
    
person = {'name': 'John', 'age': 30, 'city': 'New York'}
for key, value in person.items():
    print(f'{key}: {value}')
    
for i in range(5):
    print(i)
else:
    print("Loop completed without a break.")
    
numbers = [i for i in range(10) if i % 2 == 0]
print(numbers)