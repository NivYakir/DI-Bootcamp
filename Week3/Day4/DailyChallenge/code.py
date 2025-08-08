import math

class Circle:
    def __init__(self, radius=None, diameter=None):
        if (radius is None and diameter is None) or (radius is not None and diameter is not None):
            raise ValueError("You must provide either a radius or a diameter, but not both.")

        if radius is not None:
            if not isinstance(radius, (int, float)) or radius <= 0:
                raise ValueError("Radius must be a positive number.")
            self._radius = radius

        else:
            if not isinstance(diameter, (int, float)) or diameter <= 0:
                raise ValueError("Diameter must be a positive number.")
            self._radius = diameter / 2
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, num):
        if not isinstance(num, (int, float)) or num <= 0:
            raise ValueError("Radius must be a positive number.")
        self._radius = num

    @property
    def diameter(self):
        return self._radius * 2
    
    @diameter.setter
    def diameter(self, num):
        if not isinstance(num, (int, float)) or num <= 0:
            raise ValueError("Diameter must be a positive number.")
        
        self._radius = num / 2

    @property
    def area(self):
        return (self.radius ** 2) * math.pi
    
    @property
    def circumference(self):
        return self.radius * 2 * math.pi
    
    def __str__(self):
        return f"Circle with a radius of {self.radius}"
    
    def __repr__(self):
        return f"Circle(radius={self.radius})"
    
    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle(radius=self.radius + other.radius)
        
        elif isinstance(other, (int, float)) and other > 0:
            return Circle(radius=self.radius + other)
        
        else:
            raise ValueError("Can only add another Circle or a positive number.")
    
    def __iadd__(self, other):
        if isinstance(other, Circle):
            self.radius += other.radius

        elif isinstance(other, (int, float)) and other > 0:
            self.radius += other

        else:
            raise ValueError("Can only add another Circle or a positive number.")
        
        return self
    
    def __lt__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        
        return self.radius < other.radius
    
    def __gt__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        
        return self.radius > other.radius

    def __eq__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        
        return self.radius == other.radius




    
c1 = Circle(5)
c2 = Circle(3)
c3 = Circle(8)

print(c1)
print(repr(c1))
print(c1 + 3)
print(c1 > c2)
print(c1 == c2)

my_list = []
my_list.append(c1)
my_list.append(c2)
my_list.append(c3)

my_list.sort()
for c in my_list:
    print(str(c))