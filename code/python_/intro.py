"""
Introduction to Python tutorial covering the fundamental basics of Python
for new programmers.

Author(s):
    Michael Yao @michael-s-yao

Licensed under the MIT License. Copyright MDplus and the author(s) 2023.
"""
import numpy as np


# Hey you! Start the tutorial from here -->

def add(x: int, y: int) -> int:
    """
    This is a function called `add()`. Let's define this function by adding
    two integers `x` and `y` together to give us another integer.
    Input:
        x: an integer.
        y: an integer.
    Returns:
        x + y.
    """
    # Define a variable to be the sum of x and y.
    sum_of_x_and_y = x + y
    # Return this sum as the output from this function.
    return sum_of_x_and_y


# Let's try calling this function to compute 2 + 5.
print("What is the sum of x = 2 and y = 5?")
# We use the function that we wrote above to compute the sum of 2 and 5.
test_value_of_x = 2
test_value_of_y = 5
test_sum_of_x_and_y = add(test_value_of_x, test_value_of_y)
print("The sum of x = 2 and y = 5 is", test_sum_of_x_and_y)


def types_of_variables() -> None:
    """
    This function will help you understand the different types of data that
    a variable can represent.
    Input:
        None.
    Returns:
        None.
    """
    # In general, comments like this in Python are either prefaced by a `#`
    # symbol as you see here, or encased within """ quotation marks at their
    # beginning and end as you see above. Comments are not "actual" Python
    # code - rather, they are just helpful comments to help you and others
    # better understand your code.

    x_integer = 2  # Here, a variable called x_integer is set equal to 2.

    x_float = 2.5  # Here, a variable called x_float is set equal to 2.5.

    # Here, a variable called x_str is set equal to "Hi there!"
    x_str = "Hi there!"

    # Here, a variable called x_bool is set equal to False.
    x_bool = False

    # Let's print out the values of these variables that we've just defined.
    print("The type of variable that x_integer is is", type(x_integer))
    print("The type of variable that x_float is is", type(x_float))
    print("The type of variable that x_integer is float", type(x_str))
    print("The type of variable that x_integer is bool", type(x_bool))

    # We can also create lists of values as well.
    list_of_different_x = [2, 2.5, "Hi there!", False]
    print("We just created a new list", list_of_different_x)
    print(
        "The type of the variable list_of_different_x is",
        type(list_of_different_x)
    )
    # To retrieve the `i`th element in a list, you can call list_name[i].
    # Note that the index of an element starts at 0, so the first element in
    # the list is actually retrieved by writing list_name[0] instead of
    # list_name[1].
    print("The third element of our list is", list_of_different_x[2])

    # You can also create lists of variables too.
    new_list_of_different_x = [x_integer, x_float, x_str, x_bool]
    # This new list is exactly the same as the old list `list_of_different_x`
    # that we created above.

    # Notice that this function literally returns nothing.
    return


# Call the function `types_of_variables()`.
types_of_variables()


def for_looping(word: str) -> int:
    """
    Calculates the number of characters in a word using a `for` loop.
    Input:
        word: a word that you want to find the number of characters for.
    Returns:
        None.
    """
    total_number_of_characters = 0
    for character in word:
        # Each time we count a character, add 1 to the total number of
        # characters.
        total_number_of_characters = total_number_of_characters + 1
    return total_number_of_characters


# Let's use the function that we just wrote to calculate the length of the word
# `datathon`.
print("The length of the word `datathon` is", for_looping("datathon"))
# As a side note, another way to determine the length of a string or a list is
# to use the prebuilt `len()` function from Python.
print("The length of the word `datathon` is", len("datathon"))


def modules() -> None:
    """
    Let's try using modules! In this example, we'll utilize functions written
    in the `numpy` module.
    Input:
        None.
    Returns:
        None.
    """
    # A great guide on Python modules and why they're important can be found
    # here: https://docs.python.org/3/tutorial/modules.html

    # In this example, we'll use the numpy module, which you can read more
    # about here: https://numpy.org/doc/stable/
    # We will use the functions provided by the numpy module to sum only all
    # of the positive numbers in an array.

    # First, we use a numpy function to generate a random list of 100
    # integers between -10 and 10.
    # Read more about the np.random.randint function here:
    # https://numpy.org/doc/stable/reference/random/generated/numpy.random.randint.html  # noqa
    numbers = np.random.randint(low=-10, high=(10 + 1), size=100)
    print("Our list of number is", numbers)
    # numbers = [-7, 5, 6, ..., 0, -9, 10]
    # Read more about the np.where function here:
    # https://numpy.org/doc/stable/reference/generated/numpy.where.html
    only_positive = np.where(numbers > 0, numbers, 0)
    # only_positive = [0, 5, 6, ..., 0, 0, 10]
    # `only_positive` now only contains the positive numbers from the list,
    # and is zero everywhere else in the list.
    sum_of_only_positive_numbers = np.sum(only_positive)
    # sum_of_only_positive_numbers = 0 + 5 + 6 + ... + 0 + 0 + 10
    print(
        "The sum of only the positive numbers from the list is",
        sum_of_only_positive_numbers
    )
    return None


modules()


class Patient:
    def __init__(self, name: str, age: int):
        """
        The last thing that we have to talk about are Python classes. The idea
        behind classes is that they are representations of common objects that
        have certain properties and also things that they can do. In defining
        the attributes and functions associated with a class, we use the
        special keyword `self` to refer to the particular Patient object. A
        more detailed tutorial on classes can be found here:
        https://www.w3schools.com/python/python_classes.asp
        Args:
            name: the name of the patient that we want to create.
            age: the age of the patient that we want to create.
        """
        # The __init__() function is a special function for a class that is
        # called every time a new Patient Object is created. In this case, we
        # know from the function's arguments that a Patient object is defined
        # by their name and their age. We want to store these properties
        # for the patient when the patient is created. To do this, we can do
        self.name = name
        self.age = age
        self.diagnoses = []  # A list to keep track of the patients' diagnoses.

    def get_age(self) -> int:
        """
        Returns the age of the patient. Notice that this function is only
        defined for Patient's, and even though this function doesn't take any
        arguments, we still include `self` as an argument. In general, we
        always include `self` as the first argument in a function definition
        for a class.
        Input:
            None.
        Returns:
            The age of the patient.
        """
        # Attributes of the class, such as the patient's age, can be accessed
        # using `.`'s. In other words, anytime you see something like `x.y`,
        # you know that `y` is a property/attribute/component of `x`.
        return self.age

    def change_name(self, new_name: str) -> None:
        """
        Changes the name of the patient to a new name.
        Input:
            new_name: the new name of the patient.
        Returns:
            None.
        """
        old_name = self.name
        self.name = new_name
        print("Changed the name of the patient from", old_name, "to", new_name)
        return

    def add_diagnosis(self, new_diagnosis: str) -> None:
        """
        Adds a new diagnosis to the patient.
        Input:
            new_diagnosis: the new diagnosis to add to the patient chart.
        Returns:
            None.
        """
        # The append() method can be used to add a new variable to the end of
        # an existing list.
        self.diagnoses.append(new_diagnosis)


# Now that we have defined our Patient class. Let's create a patient: a 27
# year-old named Alice.
new_patient = Patient(name="Alice", age=27)
# What is the Alice's age again?
print(new_patient.name, "is", new_patient.get_age(), "years old.")
# Let's change Alice's name to "Amazing Alice".
new_patient.change_name("Amazing Alice")
# Finally, we can add a new diagnosis of "Being Amazing" to Amazing Alice's
# chart.
new_patient.add_diagnosis(new_diagnosis="Being Amazing")

# That's the end of the tutorial! Feel free to reach out with any questions
# or comments.
