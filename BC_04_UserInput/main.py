# input() = A function that prompts the user to enter data.
#           Returns the entered data as a string.

#print("Enter your name: ", end="")        
#name = input()

name = input("Enter your name: ")

#print("Enter your age: ", end="")        
#age = int(input())

age = input("Enter your age: ")
age = int(age)
ageNextYear = age + 1

year = int(input("Enter year were you born: "))

gpa = float(input("Enter your GPA: "))

#human = bool(input("You are a human (true/false): "))

human = input("You are a human (true/false): ").lower().strip()

print(f"Your name is {name}.")
print(f"You are {age} years old. Next year you will be {ageNextYear} ")
print(f"You were born in {year}.")
print(f"Your GPA is {gpa}.")
print(f"I am a {human} human.")
