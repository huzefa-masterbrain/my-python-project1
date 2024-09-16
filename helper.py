import main_helper
# import logging

# logger=logging.getLogger("main")
# logger.error("error happened in the app")


user_input =""
while user_input!="exit":
 user_input = input("Hey user,enter a number of days and convertion unit!\n")
 days_and_unit=user_input.split(":")
 print(days_and_unit)
 days_and_unit_dictionary={"days":days_and_unit[0],"unit":days_and_unit[1]}
 print(days_and_unit_dictionary)
 main_helper.validate_and_execute(days_and_unit_dictionary)
