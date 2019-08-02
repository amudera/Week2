class MyClass:

    listlength = 5

    def __init__(self):
        self.data = None
    
    def instance_method(self):
        return None
    
    def __getitem__(self,index, value): #to access elelments in a list or dictionary use for battleship e.g pick coordinates
        try: #return whatever self.data index is 
             return self.data[index]
        except IndexError: #if you dont specify what type of error you wont know if there are any other errors in there
            self.data.append(value) #if there is an elemet that is not in the list it will just appnd this data to the next line in the list
     #try except method 
    
    def __setitem__(self,index,value): #index = where you want to put it, value = what you want to put there
        self.data[index] = value

    

        



    @classmethod #can only be called from the class. NOT an instance method. Has to take the class itself as an argument
    def list_of_objects(cls):
        result = []
        for i in range(cls.listlength):
            new_object = cls()
            result.append(new_object)
        return result 
 
our_list = MyClass.list_of_objects()


