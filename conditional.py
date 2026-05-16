# price = input("Enter the price: ")
# if float(price) >= 1:
#     tax = .07
#     print("The tax is:", float(price) * tax)
# else:
#     tax = 0
#     print("No tax applied.", tax )


# country  = input("Enter your country: ")
# if country.lower() == "usa":
#     print("NBA is popular there.")   
# else:
#     print("you are not american")

# def check_tax():
#      country = ["usa", "canada", "mexico"]
#      country_input = input("Enter your country: ").strip().lower()
#      if country_input not in country:
#          tax = 0
#          print("No tax applied, tax is", tax)
#          return
#      province_list = ["ca", "ny", "tx"]
#      province = input("Enter your province: ").strip().lower()
        
#      if country_input in country and province in province_list:
#             tax = .07
#             print("The tax is:", tax)
         
# check_tax()


# the 'and' keyword checks for multiple conditions
# gpa = float(input("Enter your GPA: "))
# credits_completed = float(input("Enter the percentage of credits completed (0 to 1):") ) 
# if gpa >= 3.0 and credits_completed >= .70:
#     honors_program = True
# else:
#     honors_program = False
# if honors_program:
#     print("You are  eligible for the honors program.")



# gpa = float(input("What is your GPA? "))
# Percentage = float(input ("What is your percentage "))

# if gpa >= 4 or Percentage == 0.5:
#     honors_program =  True
# else :
#     honors_program = False
# if honors_program:
#     print ("Congrats on your graduation")
# else:
#     print("Register for a re-sit")

def soc ():
    score = int(input("Enter your score: "))

# if score (90):
#     print("A")
# elif score >= 80:
#     print("B")
# elif score >= 70:
#     print("C")
# elif score >= 60:
#     print("D")
# else :
#     print("F")

# Using match case statement to 
    match score:
        case   90 | 100 | 120:
            print("A")
        case 80|70:
            print("B")
        case _:
            print("F")
soc()