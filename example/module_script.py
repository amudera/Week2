class Person:
    classname = "Person"

    def __init__ (self, firstname,lastname):
        self.firstname = firstname
        self.lastname = lastname

class Teacher(Person):
    def __init__(self,name,tenure,subject):
        super().__init__(name)
        self.tenure = tenure
        self.subject = subject

    def new_attribute(self):

class Student(Person):
    def __init__(self,name,gpa,classes):
        super().__init__(name)
        self.gpa = float(0.0)
        self.classes = classes

    def gpa(self,grade):
        total = 0
        for i in grade('A','B','C','D','E','F'):
            if grade == 'A':
                total = total + 4.0
            elif grade == 'A-':
                total = total + 3.7
            elif grade == 'B+':
                total = total + 3.3
            elif grade == 'B':
                total = total + 3.0
            elif grade == 'B-':
                total = total + 2.7
            elif grade == 'C+':
                total = total + 2.3
            elif grade == 'C':
                total = total + 2.0
            elif grade == 'C-':
                total = total + 1.7
            elif grade == 'D+':
                total = total + 1.3
            elif grade == 'D':
                total = total + 1.0
            elif grade == 'E':
                total = total + 0.0
            elif grade == 'F':
                total = total + 0.0
        return self.gpa

class Food:
    

class Fruit:
    _type = "produce"
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour
    
    def __repr__(self):
        return "<Fruit Object: {},colour={}>".format(self.name,self.colour)
        
    
class ShoppingList: 
    def __init__(self):
        self.items = []
    
    def add(self,item):
        self.items.append(item) #adding something to the list

class GroceryList(ShoppingList):

    def add(self,name,colour):
        new_fruit = Fruit(name, colour)
        self.items.append(new_fruit) #only going to add new fruit to the list

    def show_items:
        for i in self.items: 
            print(i.colour,i.name) #for every fruit object this will print teh colour and name corresponding to it


our_list = GroceryList()
our_list.add('Strawberry','red')
our_list.add("Banana","yellow")

our_list.show_items()

