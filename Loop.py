# # for loop example
# for names in ["Dora", "seth", "Doe"]:
#     print(f"Hello {names}")

# for loop with range function example where it starts from 5 to 50 with a step of 10
# for number in range(5, 50, 10):
#     print(f"Hello number {number}")


# nested for loop example 
# names = ["Dora", "seth", "Doe"]
# verbs = ["runs", "jumps", "talks"]
# this iterates through each verb for every name
# for verb in verbs:
#     for name in names:
#         print(f"This {name}  {verb}  ")
# #  this iterates through each name for every verb
# for name in names:
#     for verb in verbs:
#         print(name + " " + verb + "." )


students = [
    {"name" : "Potato", "house" : "Red", "age" : 12},
    {"name" : "Pot", "house" : "Blue", "age" : 13},
    {"name" : "Po", "house" : "Green", "age" : 14}
]

for student in students: 
   print(student["age"])


# n = int(input("what number?"))

# for _ in range(n):
#     print ("Take")