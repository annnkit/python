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

