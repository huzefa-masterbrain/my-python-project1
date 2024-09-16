calculation_to_units = 24
name_of_unit="hours"
def days_to_units(num_of_days):
    if num_of_days > 0:
       return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"


def validate_and_execute():
  try:
      user_input_number = int(user_input)
      if user_input_number > 0:
         calculation_value = days_to_units(user_input_number)
         print(calculation_value)
      elif user_input_number == 0:
         print("you enter a 0,please enter a valid positive number")
      else:
        print("you entered a negative number,no conversion for you!")
  except ValueError:
        print("your inpt is not a valid number.")

while True:
 user_input=input("Hey user,enter a number of days and i will convert it to hours!\n")
 validate_and_execute()
