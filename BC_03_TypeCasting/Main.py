# Typecasting = the process of changing the data type one type to another.
#               str(), int(), float(), bool()

name = "Daniel"
empty = ""
age = 53
gpa = 3.2
is_student = True


print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))

# typecast (convert) gpa variable from float to integer and print value
gpa = int(gpa)
print(f"The gpa variable is now of type: {type(gpa)} with a value of {gpa}.")

# typecast (convert) age from int to float
age = float(age)
print(f"The age variable is now of type {type(age)} with a value of {age}.")

# typecast (convert) age variable from int to string and print value.
age = str(age)
print(f"The age variable is now of type {type(age)} with a value of {age}.")

# The following would fail because you can't add 1 to a string.
#age += 1
#print(age)

# This works because i'm concatenating two strings (53.0 and 1)
age += "1"
print(age)

# typecast a string to a boolean gives an output of True if the string is not empty
name = bool(name)
print(name)

empty = bool(empty)
print(empty)