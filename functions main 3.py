calculation_to_unit=24
name_of_unit="hours"
def days_to_units(num_of_days,custom_message):
    print(f"{num_of_days} days are {num_of_days * calculation_to_unit} {name_of_unit}")
    print(custom_message)

def scope_check():
    print(name_of_unit)
    
days_to_units(20,"awesome!")
days_to_units(35,"looks good!")
days_to_units(50,"nice")
days_to_units(110,"great")