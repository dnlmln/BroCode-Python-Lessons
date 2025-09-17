age = int(input("Enter your age?: "))

if age >= 18:
    print("You qualify for a credit card.")
elif age < 0:
    print("You haven't been born yet.")
else:
    print("You are not yet 18.")