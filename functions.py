
# names = ["Dora", "seth", "Doe"]
# verbs = ["runs", "jumps", "talks"]
# # this iterates through each verb for every name
# def nested_loops(n, v):
#     for v in names:
#         for n in verbs:
#           print(f"{v} {n}")
# nested_loops(names, verbs)

#  function to get initials from first and last name
# def get_names_initial(first, last):
# #     # first [0:1] gets the first character of the first string 
#     name = first[0].upper() + last[0].upper()
#     return name
# first_name = input("Enter your first name: ")
# last_name = input("Enter your last name: ")
# print(f"Your initials are " +  get_names_initial( first_name, last_name))

# function to get initials from first and last name with an option to force uppercase
def message(message_1, force_uppercase = False):
    if force_uppercase:
        initial = message_1 [0:1].upper()
        return initial
    else:
        initial = message_1 [0:1]
        return initial
    
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

# print("Your initials are " + message(first_name, True) + message(last_name, True))
print("Your initials are " + message (first_name, True), message (last_name, True))



# def get_ini(first, last = False):
#     if last:
#         ini = first[0:1].upper()
#         return ini
#     else:
#         ini = first[0:1]
#         return ini

# first_name = input("Please input first name " )
# last_name =  input("Please input last name " )

# print(get_ini(first_name, True) + get_ini(last_name, True))

# first = input("Please input first name " )
# last =  input("Please input last name " )

# def get_ini(ini, forced_uppercase = False):
#     init = ini[0]
#     if forced_uppercase:
#         return init.upper()
#     else:
#         return init
# print(f"Your initials are   {get_ini(first, True)} {get_ini(last, True)}")



