# f = open("file.txt", "r")
# text = f.read()
# print(text,"\n")
# f.close()

# import os
# if os.path.exists("file.txt"):
#     print("file exits")
# else:
#     print("does not exists")

# import os
# os.remove("file.txt")

# if os.path.exists("file.txt"):
#     print("file exits")
# else:
#     print("does not exists")

# try:
#     with open("missing.txt", "r") as f:
#         print(f.read())

# except FileExistsError:
#     print("file not found")

# with open("file.txt", "w") as f:
#     name = input("name: ")
#     f.write(name + "\n")

# with open("file.txt", "a") as f:
#     f.write(" and the file has been appended")

# from datetime import datetime
# with open("file.txt", "a") as log:
#     log.write(f"logged at {datetime()}\n")

# settings = {}
# with open("file.txt", "r") as f:
#     for line in f:
#         if "=" in line:
#             key, value = line.strip().split("=")
#             settings[key] = value  
        
# print(settings)

# with open("user_input.txt", "w") as f:
#     input1 = input("say something: ")
#     input2 = input("more: ")
#     input3 = input("one last time: ")
#     f.write(input1 + "\n" + input2 + "\n" + input3 + "\n")

# from datetime import datetime
# with open("log.txt", "a") as log:
#     log.write(f"logged at {datetime.now()} \n")



# n = input("number of students: ")

# f = open("student.txt", "w")
# grades = {}
# for i in range(n):
#     name = input("name: ")
#     subject = input("subject: ")
#     marks = input("marks: ")
#     f.write = (f"Name: {name}, Subject: {subject}, Marks: {marks}")
    
# f.close()

# f = open("student.txt", "r")
# text = f.read()
# print(text)

# count = 0
# for i in grades:
#     count+=1

# print(count)

# sum = 0
# for i in grades:
#     sum += i[marks]
# avg = sum/count
# print(avg)
# f.close()


# f = open("bank.txt", "w")
# balance = input("enter deposit amount: ")
# withdraw = input("enter withdrawl amount: ")
# f.close()

# f = open("bank.txt", "r")
# text = f.read()
# print(text)
# f.close()

# villain = ["arlong", "crocodile", "lucci", "moria", "katakuri", "doflamingo"]

# index = int(input("enter the villain number: "))
# try:
#     print(villain[index])
# except IndexError:
#     print("wrong index!")
# except ValueError:
#     print("wrong value!!")

# print("End of program! ")

# class AgeTooLowError(Exception):
#     def __init__(self, age):
#         self.age =age
#         super().__init__(f"age too low to register")

# age = int(input("Enter age: "))

# if age<18:
#     raise AgeTooLowError(age)
# else:
#     print("registration successful")

# try:
#     raise AgeTooLowError(age)
# except AgeTooLowError as e:
#     print("custom Execption caught: ", e)

# import logging

# logging.basicConfig(filename="log.txt", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# logging.info("program started")

# try:
#     x = 20/0
# except ZeroDivisionError as e:
#     logging.error("Error occured: %s", e)

import logging
class LoginError(Exception):
    pass

logging.basicConfig(filename="login.log", level=logging.ERROR)

username = input("Enter username: ")
if username != "admin":
    error = LoginError("unauthorized access attempt ")
    logging.error("login failed: %s", error)
    raise error
else:
    print("WElcome, admin!")