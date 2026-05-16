# #Library imports for date manipulation
# from datetime import datetime, timedelta

# # birthday = datetime.now()
# birth_date = input("Enter your birthdate (YYYY-MM-DD): ")
# #using strptime to parse string into date object
# birthday = datetime.strptime(birth_date, "%Y-%m-%d").date()
# # print("My birthday is:", birthday)
# #timedelta to represent one day 
# time_delta = timedelta(days=1)
# birthday_eve = birthday - time_delta
# print("My birthday eve was:", birthday_eve)



from datetime import datetime, timedelta

birthday_date = input("Enter birthday in this format (YYYY-MM-DD)")

birth = datetime.strptime(birthday_date, "%D-%m-%y").date()
print("Birthday is ", birth)

# time_delta = timedelta(days = 1)
# birth_prev_days = birth - time_delta
# print("A days before my birthdays is", birth_prev_days)