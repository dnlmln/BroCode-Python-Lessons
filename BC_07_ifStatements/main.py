age = int(input("Enter your age: "))


if age < 2:
    print("You are a baby.")
elif age < 4:
    print("You are a todler.")
elif age < 12:
    print("You are a child")
elif age < 20:
    print("You are a teenager.")
else:
    print("You are an adult.")