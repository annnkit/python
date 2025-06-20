# class Animal:
#     def make_sound(self):
#         print("make a sound")

# class Dog(Animal):
#     def make_sound(self):
#         return "Dog barks"
    
# class cat(Animal):
#     def make_sound(self):
#         return "cat meow!"
    
# class Cow(Animal):
#     def make_sound(self):
#         return "cow moo!"
    
# def make_animal_sound(animal_obj):
#     print(animal_obj.make_sound)
#     print(animal_obj.make_sound())


# c1 = Dog()
# c2 = cat()
# c3 = Cow()

# make_animal_sound(c1)
# make_animal_sound(c2)
# make_animal_sound(c3)

# class BankAccount:
#     def __init__(self, account_holder, balance):
#         self.__account_holder = account_holder
#         self.__balance = balance
        
#     def get_acc(self):
#         return self.__account_holder
        
#     def get_bal(self):
#         return self.__balance
        
#     def account_type(self):
#         return "hello"

    
# class SavingsAccount(BankAccount):
#     def account_type(self):
#         return "Saving account"
    
    
    
# class CurrentAccount(BankAccount):
#     def account_type(self):
#         return "Current account"
        
# b1 = SavingsAccount("aniket", 50000)
# b2 = CurrentAccount("vinay", 78000)

# bank_accs = [b1, b2]

# for acc in bank_accs:
#     print(acc.account_type())

# from abc import ABC, abstractmethod

# class Dish(ABC):
#     def __init__(self, name, price):
#         self._name = name
#         self._price = price

#     @abstractmethod
#     def prepare_dish(self):
#         pass

#     @abstractmethod
#     def get_ingredients(self):
#         pass

#     def serve_dish(self):
#         print("Serving the dish...")

#     def get_name(self):
#         return f"Serving dish: {self._name}"
    
#     def get_price(self):
#         return f"Price: ₹{self._price}"


# class Pizza(Dish):
#     def __init__(self, name, price):
#         super().__init__(name, price)

#     def prepare_dish(self):
#         print(f"{self._name} is being prepared...")

#     def get_ingredients(self):
#         print("Ingredients: water, flour-dough, cheese, sauce, toppings")


# class Restaurant:
#     def order_dish(self, dish: Dish):
#         if dish:
#             print("Customer ordered:", dish.get_name())
#             print(dish.get_price())
#             dish.get_ingredients()
#             dish.prepare_dish()
#             dish.serve_dish()
#         else:
#             print("That dish is currently not available.")


# lpu_rest = Restaurant()
# farm_house = Pizza("Farm House Pizza", 290)
# lpu_rest.order_dish(farm_house)


# class shape:
#     def __init__(self, color):
#         self.__color = color

#     def get_color(self):
#         return self.__color


# class circle(shape):
#     def area(r):
#         return "area"
    
# class sqaure(shape):
#     def area(s):
#         return "area"
    
# def get_area(s):
#     print(s.area())

# s1 = circle(2)
# s2 = sqaure(3)

# get_area(s1)

from abc import ABC, abstractmethod
class SocialMedia(ABC):
    @abstractmethod
    def post_content():
        pass


class insta(SocialMedia):
    def post_content(self):
        print("posting photo with filter")

class twitter(SocialMedia):
    def post_content(self):
        print("stwitting with hashtag")

class linkedin(SocialMedia):
    def post_content(self):
        print("sharing professional update")

i = insta()
t = twitter()
l = linkedin()


i.post_content()
t.post_content()
l.post_content()