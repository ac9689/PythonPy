import math_operations

while True:
    result_add = math_operations.multiply(5, 6)
    print(result_add)
    
    # Option to exit the loop
    user_input = input("Type 'exit' to stop the loop: ")
    if user_input.lower() == 'exit':
        break