# Example 1: Basic if-else
x = 10
if x > 5:
    print("x is greater than 5")
else:
    print("x is 5 or less")

# Example 2: if-elif-else
y = 20
if y < 10:
    print("y is less than 10")
elif y == 20:
    print("y is equal to 20")
else:
    print("y is greater than 10 but not 20")

# Example 3: Nested if-else
z = 15
if z > 10:
    if z % 2 == 0:
        print("z is greater than 10 and even")
    else:
        print("z is greater than 10 and odd")
else:
    print("z is 10 or less")

# Example 4: Ternary operator (short if-else)
a = 5
result = "Positive" if a > 0 else "Non-positive"
print(f"a is {result}")

# Example 5: Using logical operators
b = 7
if b > 0 and b < 10:
    print("b is a single-digit positive number")
else:
    print("b is not a single-digit positive number")

# Example 6: Checking membership
fruits = ["apple", "banana", "cherry"]
if "apple" in fruits:
    print("Apple is in the list")
else:
    print("Apple is not in the list")

# Example 7: Comparing strings
name = "Alice"
if name == "Alice":
    print("Hello, Alice!")
else:
    print("You are not Alice")