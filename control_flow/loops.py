# Python Loops Examples

# 1. For Loop with Range
print("1. Basic for loop with range:")
for i in range(5):  # 0 to 4
    print(f"Count: {i}")

# 2. For Loop with List
print("\n2. For loop with a list:")
fruits = ["apple", "banana", "cherry", "date"]
for fruit in fruits:
    print(f"Fruit: {fruit}")

# 3. For Loop with Enumeration
print("\n3. For loop with enumeration:")
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

# 4. While Loop
print("\n4. While loop:")
count = 0
while count < 5:
    print(f"While count: {count}")
    count += 1

# 5. Nested Loops
print("\n5. Nested loops:")
for i in range(3):
    for j in range(2):
        print(f"({i}, {j})", end=" ")
    print()  # New line after each inner loop

# 6. Loop with Break
print("\n6. Loop with break:")
for i in range(10):
    if i == 5:
        break
    print(f"Before break: {i}")

# 7. Loop with Continue
print("\n7. Loop with continue:")
for i in range(7):
    if i % 2 == 0:  # Skip even numbers
        continue
    print(f"Odd number: {i}")

# 8. For Loop with Dictionary
print("\n8. For loop with dictionary:")
person = {"name": "John", "age": 30, "city": "New York"}
for key in person:
    print(f"{key}: {person[key]}")

# 9. For Loop with items() for Dictionary
print("\n9. For loop with dictionary items():")
for key, value in person.items():
    print(f"{key} -> {value}")

# 10. While Loop with else
print("\n10. While loop with else:")
count = 0
while count < 3:
    print(f"While count: {count}")
    count += 1
else:
    print("While loop completed successfully")

# 11. For Loop with else
print("\n11. For loop with else:")
for i in range(3):
    print(f"For count: {i}")
else:
    print("For loop completed successfully")

# 12. List Comprehension (a compact way to create lists)
print("\n12. List comprehension:")
squares = [x**2 for x in range(5)]
print(f"Squares: {squares}")

# 13. Using zip to iterate through multiple lists simultaneously
print("\n13. Using zip:")
names = ["Alice", "Bob", "Charlie"]
ages = [24, 30, 35]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")