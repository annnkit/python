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

try:
    with open("missing.txt", "r") as f:
        print(f.read())

except FileExistsError:
    print("file not found")

