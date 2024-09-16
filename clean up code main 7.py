calculation_to_units = 24
name_of_unit="hours"

def days_to_units(num_of_days):
    if num_of_days > 0:
       return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"
    elif num_of_days == 0:
        return "you entered a 0,please enter a valid positive number"


def validate_and_execute():
    if user_input.isdigit():
        user_input_number = int(user_input)
        calculation_to_units = days_to_units(user_input_number)
        print(calculation_to_units)
    else:
        print("your input is not a number")

user_input=input("Hey user,enter a number of days and i will convert it to hours!\n")
validate_and_execute()
