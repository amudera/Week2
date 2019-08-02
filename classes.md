## More Classes Practice

Make the following classes:

* Create a Person class that contains `first_name` and `last_name` as attributes
    * Create Student and Teacher subclasses. Student should have `gpa` (a float) and `classes` (a list of strings) as attributes. Teacher should have `tenure` (a bool) and `subject` (a string) as attributes

    * Write a method for the Student class that updates its GPA, and a method for Teacher that can create a new attribute, `students`, and assign it a list of Student objects

* Create a Food class that has the attributes `name`, `healthy` (a bool) and `price` (a float).
    * Create a ShoppingList class that has a single attribute, `shopping_list`, that defaults to an empty list. Write a method `add_to_list()` that will create and add instances of the Food class to `shopping_list`
    * Create a method view_list() that will print the name and price of each item in the shopping list, as well as their total price.
