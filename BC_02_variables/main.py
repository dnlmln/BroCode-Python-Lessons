# Variables = A container for values (String

# Strings
first_name = "Daniel Milani"
food = "pizza"
email = "dan@pizza.com"

# integers
age = 53
quantity = 3

# floats (double)
price = 10.99
gpa = 3.2

# boolean
is_student = False
for_sale = True

print(first_name)
print("My name is " + first_name)
print(f"My name is {first_name} and i like {food} and my email is {email}.")
print(f"I am {age} years old and buying {quantity} items for ${price}.")
print(f"My GPA is {gpa}")
print(f"You are a student is {is_student}")

if is_student:
    print("You are a student.")
else:
    print("You are not a student")

if for_sale:
    print("That item is for sale.")
else:
    print("That is is not for sale")