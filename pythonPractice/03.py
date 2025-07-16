# numbers =[1, 5, 3, 8, 4, 0]

# numbers.sort()
# print(numbers)

# names = {"rahul":0, "natlie":1, "raj":2, "kavi":3}
# grade = {"rahul":"A", "natlie":"B", "raj":"C", "kavi":"D"}

# students = (numbers, names)

# print(students)

#functions
# def <func name> (para)
#     statements
# return task

# def greet():
#     print("hello!!")

# greet()

# def get_max(num1, num2) ->int:
#     if(num1>num2):
#         return num1
#     else:
#         return num2
    
# print(get_max(4,9))
# vow = "aeiou"
# def vowels(tex: str) ->int:
#     count = 0
#     for char in tex.lower():
#         if char in "aeiou":
#             count = count+1
#     return count

# print(vowels("Hello world"))

# def sum_numbers(list) ->int:
#     sum = 0
#     for num in list:
#         sum+=num
#     return sum

# print(sum_numbers([1,2,3,4,5]))

# def get_min_max(list) ->int:
#     return min(list), max(list)

# print(get_min_max([3, 5, 1, 9, 7]))

# words = "this is a test this is not for fun".split()
# def word_frequency(words: str):
#     freq={}
#     count1= count2=count3=count4= count5= count6=count7=0
#     for word in words:
#         if word == "this":
#             count1+=1
#         elif word == "is":
#             count2+=1
#         elif word == "a":
#             count3+=1
#         elif word =="test":
#             count4+=1
#         elif word == "not":
#             count5+=1
#         elif word == "for":
#             count6+=1
#         elif word == "fun":
#             count7+=1

#     freq = {"this":count1, "is":count2, "a":count3, "test":count4, "not":count5, "for":count6, "fun":count7}

#     return freq

# print(word_frequency(words))

# def word_frequency(words: str):
#     freq={}
#     for word in words:
#          freq[word] = freq.get(word, 0) + 1

#     return freq
# print(word_frequency(words))

data = [
{"id": 1, "name": "Alice"}, 
  {"id": 2, "name": "Bob"},
 {"id": 1, "name": "Charlie"}, 
 {"id": 3, "name": "Alice"}
 ]

seen_name = set()
unique = []

def remove_duplicate(data):
    for item in data:
        if item["name"] not in seen_name:
            unique.append(item)
            seen_name.add(item["name"])

    print(unique)

remove_duplicate(data)
        

