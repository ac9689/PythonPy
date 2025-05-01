my=[4,6,5,"helloworld",3.14] # List with mixed data types
del my[1]
#my.extend(my[1:10])  # Example: Extending the list with a slice of itself
my.insert(1, 2)  # Example: Inserting an element at index 1
my[2]= 88
print(my)
my_dict = {   # Dictionary to store user information
    "name": "Alice",
    "age": 25,
    "city": "Delhi"
}
for key, value in my_dict.items():
    print(key, value)
    
    
    
book = {         # Dictionary to store book information
    "title": "Python Basics",
    "author": "John Smith",
    "isbn": "978-1-23456-789-7",
    "available": True,
    "copies": 3
}

# Accessing book info
print("Book Title:", book["title"])

# Updating availability
book["available"] = False

# Adding a new field
book["shelf"] = "A3"

# Display full book info
print("\nBook Details:")
for key, value in book.items():
    print(f"{key}: {value}")

