import random

# Exercise 1: Temperature

class Temperature:
    def __init__(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be a valid integer or float")
        self.value = value

class Celsius(Temperature):
    def __init__(self, value):
        super().__init__(value)
    
    def to_kelvin(self):
        return Kelvin(self.value + 273.15)
    
    def to_fahrenheit(self):
        return Fahrenheit((self.value * 9/5) + 32)
    
    def __str__(self):
        return f"{self.value} degrees Celsius"


class Fahrenheit(Temperature):
    def __init__(self, value):
        super().__init__(value)
    
    def to_celsius(self):
        return Celsius((self.value - 32) * 5/9)
    
    def to_kelvin(self):
        return Kelvin(((self.value - 32) * 5/9) + 273.15)
    
    def __str__(self):
        return f"{self.value} degrees Fahrenheit"

class Kelvin(Temperature):
    def __init__(self, value):
        super().__init__(value)
    
    def to_celsius(self):
        return Celsius(self.value - 273.15)
    
    def to_fahrenheit(self):
        return Fahrenheit(((self.value - 273.15) * 9/5) + 32)
    
    def __str__(self):
        return f"{self.value} degrees Kelvin"
    

# # Exercise 2: In the Quantam Realm

# class QuantumParticle:
#     def __init__(self, x, y, p):
#         self.x = x
#         self.y = y
#         self.p = p

#     def _disturbance(self):
#         self.x = random.randint(1, 100000)
#         self.y = random.random()
#         print("Quantum Interferences!!")

#     def position(self):
#         self._disturbance()
#         return self.x
    
#     def momentum(self):
#         self._disturbance()
#         return self.y
    
#     def spin(self):
#         self._disturbance()
#         self.p = random.choice([-0.5, 0.5])
#         return self.p
    
#     def __repr__(self):
#         return f"QuantumParticle(x={self.x}, y={self.y}, p={self.p})"


import random

class QuantumParticle:
    def __init__(self, x, y, p):
        self.x = x  # position
        self.y = y  # momentum
        self.p = p  # spin

    def _disturbance(self):
        """Applies quantum disturbance: changes position and momentum randomly."""
        self.x = random.randint(1, 10000)
        self.y = random.uniform(0, 1)
        print("Quantum Interferences!!")

    def position(self):
        self._disturbance()
        return self.x

    def momentum(self):
        self._disturbance()
        return self.y

    def spin(self):
        self._disturbance()
        self.p = random.choice([0.5, -0.5])
        return self.p

    def __repr__(self):
        return (
            f"<QuantumParticle | Position: {self.x}, "
            f"Momentum: {self.y:.4f}, Spin: {self.p}>"
        )