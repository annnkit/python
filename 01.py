# print("hello world")
# k = 10
# float(k)
# print(k)

# y = str(False)
# print(type(y))

# #float -> string
# float_to_string = str(5.089)
# print(type(float_to_string))


# #typeCasting
# i = 890.09
# float(i)
# print(i)

# #tupples
# numbers = (1,5,3,6,3)
# print(max(numbers))

# #tuplle *unpacking(:grab some values and assign rest to another variable)
# a, b, *c = numbers
# print(*c)

# cities = ("bejing", "tokyo", "delhi", "mumbai")
# a, b, *c = cities
# print(*c)

# print(cities.index("tokyo"))


#dictionary
# grades = {"Name":"rahul", "grade":"A", "age" : 20}
# print(grades.get("age"))
# print(grades.get("Name"))
# print(grades.keys())
# print(grades.values())
# print(grades.items())

# student = {"name":"vinay", "age":20, "grade":"A"}
# print(student.get("name"))
# print(student.pop("age"))
# print(student.items())

#SET(mutable, unordered)
my_set = {"ankit","vinay","raj"}
print(my_set)

empty = {}
print(empty)

print(len(my_set))
print(my_set.issubset("ankit"))
print(my_set.issuperset("ankit"))
print(my_set.union("ankit"))
print(my_set.intersection("ankit"))