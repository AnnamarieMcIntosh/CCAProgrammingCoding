class Person:
    '''
    This class defines the data and methods associated with a person
    '''
    def __init__(self, name, age):
        '''Person class initializer or constructor.'''
        self.name = name   # instance variable / data attribute
        self.__age = age   # 'private' data attribute

    # getter and setter methods
    def get_name(self):
        '''Getter method for name attribute.'''
        return self.name

    def get_age(self):
        '''Setter method for age attribute.'''
        return self.__age

    def set_age(self, age):
        '''Getter method for age attribute.'''
        self.__age = age
            
    # more class methods for person
    def sing(self):
        '''Method to make the Person object sing.'''
        pass
    
    def feed(self, food):
        '''Method to feed the Person object.'''
        pass
    
    # special  method, defines system str() conversion for our new type!
    def __str__(self):
        '''str conversion for Person objects.'''
        return self.name + ", " + str(self.__age)

    
