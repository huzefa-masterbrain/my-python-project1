calculation_to_unit = 24
name_of_unit = "hours"


def days_to_units(num_of_days, custom_message):
    print(f"{num_of_days} days are {num_of_days * calculation_to_unit} {name_of_unit}")
    print(custom_message)


def scope_check(num_of_days):
    my_var="variable inside function"
    print(name_of_unit)
    print(num_of_days)
    print(my_var)


scope_check(20)