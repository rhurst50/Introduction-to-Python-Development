import math

class Tire:
    """
    Tire attributes that would be used with a car or truck
    these attributes follow hte dimension/build values communcated on the
    sidewall and can be converted into somethiong more useful.
    """
    def __init__(self, tire_type, width, ratio, diameter, brand='', construction='R'):
        self.tire_type = tire_type
        self.width = width
        self.ratio = ratio
        self.diameter = diameter
        self.brand = brand
        self.construction = construction

    def circumference(self):
        """
        The circumference is Pi * Diameter. To figure out the diameter in inches you must

        >>> tire = Tire('P', 205, 65, 15)
        >>> tire.circumference()
        80.1
        """
        #side_wall_inches = (self.width * (self.ratio / 100)) / 25.4 COMMENTED THIS AOUT AS HE DELETED IT IN CHAPTER 7.3 SINCE WE ARE CALLING THE SIDEWALL INCHA CALCAULATING FROM THE SNOWTIRE CLASS BELOW.
        #total_diameter = (side_wall_inches * 2 + self.diameter) THIS WAS THE ORIGINAL PRE CHAPTER 7.3
        total_diameter = self._side_wall_inches() * 2 + self.diameter
        return round(total_diameter * math.pi, 1)

    def inch_width(self):
        tire_in_width = (self.width / 25.4)
        return(tire_in_width)

    def __repr__(self):
        """
        represents the tire's info in the standard notation on the side of the tire
        """
        return (f"{self.tire_type}{self.width}/{self.ratio}"
                + f"{self.construction}{self.diameter}")

    def _side_wall_inches(self):
         return (self.width * (self.ratio / 100)) / 25.4



'''
example of inheritance from chapter 7.3. TO create a sub class you create a new classs and call out the primary class
in () after it like hte example below:
'''

class snowTire(Tire):
    def __init__(self, tire_type, width, ratio, diameter, chain_thickness, brand='', construction='R'):
        #Tire.__init__(self, tire_type, width, ratio, diameter, brand, construction) HE INITIALLY GAVE THIS EXAMPLE LINE TO SHOW THAT WE ARE MANUALLY PULLING THE OBJECTS DOWN FROM THE TIRE CLASS ABOVE TO GET US THINKING AOBUT IT
        super().__init__(tire_type, width, ratio, diameter, brand, construction) # THIS EXAMPLE HE DID AFTER THE COMMENTED ONE  ABOVE HE STATES THAT IF WE EVER CHANGE THE PARENT CLASS TITLE, IT WILL POPULATE HTE SELF.VALUES PROPERLY
        self.chain_thickness = chain_thickness

    def circumference(self): # overriding the original circumference above
        '''
        the circumfrence of a tire with the chain thickness added in inches.

        >>> tire = snowTire('P', 205, 65, 15, 2)
        >>> tire.circumference()
        92.7
        '''
        total_diameter = (self._side_wall_inches() + self.chain_thickness) * 2 + self.diameter
        return round(total_diameter * math.pi, 1)

    def __repr__(self):
        return super().__repr__() + " (Snow)"
