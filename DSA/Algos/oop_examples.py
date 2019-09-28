"""
This file is for compiling different object oriented design principles.

Including some other random related stuff.
"""

class Dogs(object):
    """Abstracting dogs."""
    species = "mamals"
    def __init__(self, age):
        """Initialising dog instance with at least its age."""
        self.age = age
        self.name = ""
    def set_age(self, age):
        """Edit access to protected age instance attribute."""
        self.age = age
    def get_age(self):
        """Read access to protected age instance attribute."""
        return self.age

class DogPark(object):
    """A class to hold a collection of dogs, confined to a certain physical place."""
    def __init__(self):
        """Store the collection with a HashTable for easy info ret."""
        self.dog_members = {}
        self.location = ""
    def get_oldest_dog(self):
        """Retrieve oldest dog in the park."""
        return max(self.dog_members[x] for x in self.dog_members)
    def add_dog(self, dog):
        """Add dog object into park, use name as key and object addr as value in HT."""
        self.dog_members[dog.name] = dog
