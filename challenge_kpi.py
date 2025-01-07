# Get user name
valid_name, valid_salary, validy_bonus = False, False, False

while not valid_name:
    try:

        name = input("Enter your name: ")
        if len(name) == 0:
            raise ValueError("Your name shouldn't be empty.")

        elif any(char.isdigit() for char in name):
            raise ValueError("Your name could not have numbers.")

        else:
            print(f"Hello, {name}")
            valid_name = True

    except ValueError as e:
        print(e)

while not valid_salary:
    try:
        salary = float(input(f"{name.capitalize()}. What is your salary? "))
        if salary < 0:
            raise ValueError("Your salary could not be negative.")
        else:
            valid_salary = True
    except ValueError as e:
        print("Entry invalid for your salary. Please, insert a number")

while not validy_bonus:
    try:
        bonus = float(input(f"{name.capitalize()}. What is your bonus percentage?"))
        if bonus < 0:
            raise ValueError("Your bonus could not be negative.")
        else:
            validy_bonus = True
    except ValueError as e:
        print("Entry invalid for your bonus. Please, insert a number")


print(f"Hello, {name.capitalize()}! Your total salary + bonus is is {int(1000 + (salary * bonus)):.2f}")