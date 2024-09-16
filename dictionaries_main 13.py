
def days_to_units(num_of_days,conversion_unit):
    if conversion_unit =="hours":
       return f"{num_of_days} days are {num_of_days * 24} hours"
    elif conversion_unit=="minutes":
        return f"{num_of_days} days are {num_of_days * 24 * 60} minutes"
    else:
        return"unsupported unit"


def validate_and_execute():
  try:
      user_input_number = int(days_and_unit_dictionary["days"])
      if user_input_number > 0:
         calculation_value = days_to_units(user_input_number,days_and_unit_dictionary["unit"])
         print(calculation_value)
      elif user_input_number == 0:
         print("you enter a 0,please enter a valid positive number")
      else:
        print("you entered a negative number,no conversion for you!")
  except ValueError:
        print("your inpt is not a valid number.")

user_input =""
while user_input!="exit":
 user_input = input("Hey user,enter a number of days and convertion unit!\n")
 days_and_unit=user_input.split(":")
 print(days_and_unit)
 days_and_unit_dictionary={"days":days_and_unit[0],"unit":days_and_unit[1]}
 print(days_and_unit_dictionary)
 print(type(days_and_unit_dictionary))
 validate_and_execute()


# my_list=["20","30","100"]
# print(my_list[2])

# my_dictionary={"days":20,"unit":"hours","message":"all good"}
# print(my_dictionary["message"])
"""message="enter some value"
days=20
price=9.99
valid_number=True
exit(exit_input)=False
lists_of_days=[20,40,20,100]
lists_of_months=["january","february","june"]
set_of_days={20,45,100}
days_to_units={"days":10,"unit:hours"}"""