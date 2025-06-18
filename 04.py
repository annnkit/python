# class person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def intro(self):
#         print(f"hello my name is {self.name} and i am {self.age} years old.")

# p1 = person("aniket", 21)
# p1.intro()

# class employee:
#     def __init__(self, id, name, salary):
#         self.name = name
#         self.id = id
#         self.salary = salary

#     def increement(self):
#         print(self.salary*2)

# e1 = employee( 107, "vinay", 78000)
# e1.increement()

# class calculator:
#     def __init__(self,a, b):
#         self.a = a
#         self.b = b

#     def add(self):
#         return self.a+self.b
#     def sub(self):
#         return self.a- self.b
#     def multiply(self):
#         return self.a*self.b
#     def divide(self):
#         return self.a/self.b
    
# c1 = calculator(5, 4)
# print(c1.add())
# print(c1.sub())
# print(c1.multiply())
# print(c1.divide())

# class rectangle:
#     def __init__(self, l, b):
#         self.l = l
#         self.b = b

#     def para(self):
#         return 2*self.l*self.b
    
#     def area(self):
#         return self.l*self.b
    
# r1 = rectangle(3, 5)
# print(r1.para())
# print(r1.area())

# class student:
#     def __init__(self, name, roll, marks):
#         self.name = name
#         self.roll = roll
#         self.marks = marks

#     def if_pass(self):
#         if(self.marks>=40):
#             print("pass")
#         else:
#             print("fail")

# s1 = student("ajay", 6, 45)
# s2 = student("vineet", 2, 32)
# s3 = student("anshika", 5, 76)

# s1.if_pass()
# s2.if_pass()
# s3.if_pass()


# class Book:
#     def __init__(self, title, author, price):
#         self.title = title
#         self.author = author
#         self.price = price

# def priced_books(books):
#     for book in books:
#         if book.price>=500:
#             print(book.title)



# b1 = Book("one piece", "oda", 500)
# b2 = Book("bleach", "aizen", 408)
# b3 = Book("rich dad poor dad", "robert kiyosaki", 590)

# books = [b1, b2, b3]

# priced_books(books)

class movie:
    def __init__(self, name, rating, genre):
        self.name = name
        self.rating = rating
        self.genre = genre

def filter_movie(movies, Genre):
    for movie in movies:
        if movie.genre == Genre:
            print(movie.name)

m1 = movie("steel troops", 7.1, "sci fi")
m2 = movie("ye bhi tha nobita wo bhi tha nobita", 7.8, "adventure")
m3 = movie("incenption", 9.1, "sci fi")

movies = [m1, m2, m3]

filter_movie(movies, "sci fi")