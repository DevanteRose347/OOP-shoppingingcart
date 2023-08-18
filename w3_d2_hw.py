### Exercise 1 - Turn the shopping cart program from last week into an object-oriented program

# The comments in the cell below are there as a guide for thinking about the problem. 
# However, if you feel a different way is best for you and your own thought process, 
# please do what feels best for you by all means.
# Create a class called cart that retains items and 
# has methods to add, remove, and show
class Item:
    def __init__(self, name, quantity, cost,):
        self.name = name
        self.quantity = quantity
        self.cost = cost
    def __repr__(self):
        return f"{self.quantity} {self.name} cost {self.quantity * self.cost}"
class Cart:
    

    def __init__(self):
         self.items = {}
        

    def add_item(self, item):
        self.items[item.name] = item
            
            
        
    def remove_item(self,name):
        del self.items[name]



    def show_item(self): 
         print(self.items)  


        
my_cart = Cart()
d_cart = Cart()
milk = Item('milk', 1, 3.50)
bread = Item('bread', 2, 1.75 )
juice = Item('lemonade',3, 2.10)
print(juice)
chicken = Item('fried', 2, 10.50) 
my_cart.add_item(milk) 
print(my_cart.items)
my_cart.remove_item('milk')
my_cart.show_item()
d_cart.add_item(bread)
d_cart.show_item()





### Exercise 2 - Write a Python class which has two methods get_String and print_String. 
# get_String accept a string from the user and print_String print the string in upper case

class D_strings ():

    def __init__(self, string):
        self.string = string

    def get_String(self):
        return self.string
    
    def print_String_uppercase(self):
        print(self.string.upper())

word = D_strings("king")

word.get_String()
word.print_String_uppercase()

