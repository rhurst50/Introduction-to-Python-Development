class Car:
    """
    This is a documentation string that is used to define the class.
    Finally he showed how to use it versus the lab he had us look at
    earlier in the course. I digress, this is the area that you would
    use to describe the new class that you are creating. As info these
    look alot like a function but in this case they are a method. THe difference is that a method can be
    atttacehd to an object.
    In this example we will say:
    Car models a car with tires an an engine
    """
    def __init__(self, engine, tires):
        self.engine = engine
        self.tires = tires

    def description(self):
        print(f"A car with an {self.engine} engine and a {self.tires} tire configuration")

    def wheel_circumference(self):
        if len(self.tires) > 0:
            return self.tires[0].circumference()
        else:
            return(0)

    def inwidth(self):
        return self.tires[0].inch_width()
        """
        Can put a doc string here for instance the init he said has to be followed by (self) which is hte instance we are creating
        see https://micropyramid.com/blog/understand-self-and-__init__-method-in-python-class/
        for more details
        """

