age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult.")
    if (age >= 60):
        print("You are a senior citizen.")
    else:
        print("You are not a senior citizen.")
else:
    print("You are not an adult.") 
if age >= 18 and age < 60:
    print("You are able to drive cars and bikes.")