
from abc import ABC, abstractmethod 
  
class Polygon(ABC): 
  
    # abstract method 
    def noofsides(self): 
        pass
  
class Triangle(Polygon): 
  
    # overriding abstract method 
    def noofsides(self): 
        print("Triangle have 3 sides") 
  
class Pentagon(Polygon): 
  
    # overriding abstract method 
    def noofsides(self): 
        print("Pentagon have 5 sides") 
  
class Hexagon(Polygon): 
  
    # overriding abstract method 
    def noofsides(self): 
        print("Hexagon have 6 sides") 
  
class Quadrilateral(Polygon): 
  
    # overriding abstract method 
    def noofsides(self): 
        print("Quadrilateral have 4 sides") 
  
# Driver code 
R = Triangle() 
R.noofsides() 
  
K = Quadrilateral() 
K.noofsides() 
  
R = Pentagon() 
R.noofsides() 
  
K = Hexagon() 
K.noofsides() 
