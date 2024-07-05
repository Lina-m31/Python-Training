import math 
import turtle


#creat planets:
class Planet:
    
    def __init__(self,name,mass,radius,Distance,velocity,Orbital_Period,star,color):

        self.name=name
        self.mass=mass
        self.radius=radius
        self.Distance=Distance
        self.velocity=velocity
        self.Orbital_Period=Orbital_Period
        self.star=star
        self.color=color
    

    def __str__(self): 
        return f"planet  {self.name} that orbits {self.star} "
    


## add the planets to a list as solar_system and perfomr methods on them
class solar_system:
    planets = [] 
    
##Inserting planets to the solar_system
    def __init__(self):
        self.planets = []
        

    def insert_planet(self, planet):
        self.planets.append(planet)

    ## print planets names
    def print_planets(self):
        for planet in self.planets:
            print(planet)

    ## Draw the solar system using turtle 
    def draw_planets(self):
        t = turtle.Turtle()
        screen = turtle.Screen()
        screen.setworldcoordinates(-1000, -1000, 1000, 1000)
        t.speed(0)
        
        ##use the class method from Constellation project to draw the sun
        Constellation.draw_star(t, (6963.40*3) , (0, 0), "yellow")

        for index, planet in enumerate(self.planets):
            angle = 360 / len(self.planets) * index
            distance_from_sun = 500
            x = distance_from_sun * math.cos(math.radians(angle))
            y = distance_from_sun * math.sin(math.radians(angle))
            t.penup()
            t.goto(x, y)
            t.pendown()
            t.dot(planet.radius/900 , planet.color)  # Scale the planet radius for drawing
            t.write(planet.name, align="center", font=("Arial", 8, "normal"))

        
        screen.exitonclick()



#creat a star
class Star:

    position=(0,0,0)
    velocity=(0,0,0)
    number_of_stars=0

    def __init__(self,name,radius):
        self.name=name
        self.radius=radius
        self.smaller=None
        self.bigger=None
        Star.number_of_stars = Star.number_of_stars + 1


    def __str__(self): 
        return f"Star  {self.name}  "



#Creat constellation of stars using tree method 
class Constellation:
    R=696340

## Creat the main star , in our case it will be the sun
    def __init__(self, name=None, radius=0):
        self.root = Star(name,radius) if name else None
        
        
 ## adding stars to the constellation
    def insert(self, name, radius):
        if self.root is None:
            self.root = Star(name, radius)

        else:
            self._insert(self.root, name, radius)

# The stars will be added based on its size compared to the sun, if smaller than the sun it bill be added to smaller
# if bigger it will be added to bigger 
    def _insert(self, current_node, name, radius):

        if radius < current_node.radius:
            if current_node.smaller:
                self._insert(current_node.smaller, name, radius)
            else:
                current_node.smaller = Star(name, radius)
        elif radius > current_node.radius:
            if current_node.bigger:
                self._insert(current_node.bigger, name, radius)
            else:
                current_node.bigger = Star(name, radius)
        else:
            print("Star already added")


## search if specific star is exist based on its radius
    def search(self, radius):
        current_node = self.root
        while current_node:
            if radius < current_node.radius:
                current_node = current_node.smaller
            elif radius > current_node.radius:
                current_node = current_node.bigger
            else:
                return True
        return False


## print the stars inorder
    def inorder_traversal(self, node):
        values = []
        if node:
            values = self.inorder_traversal(node.smaller)
            values.append(node.name)
            values += self.inorder_traversal(node.bigger)
        return values

    
## methods to draw the stars based on its size
    @classmethod
    def draw_star(cls, t, radius, position , color):
        t.penup()
        t.goto(position)
        t.pendown()
        t.dot(radius/400 , color)
    
    def draw(self):
        # Initialize turtle parameters
        t = turtle.Turtle()
        screen = turtle.Screen()
        screen.setworldcoordinates(-1000, -1000, 1000, 1000)
        t.speed(0)
        
        def _draw(current_node, position=(0, 0),level=0 , color="yellow"):
            if current_node:
                # Scale radius for drawing
                new_radius = (current_node.radius / (Constellation.R/1000)) * 50
                self.draw_star(t, new_radius, position , color)
                
                #defining offset to draw the stars seperatly
                offset = 200 / (level + 1)
                smaller_position = (position[0] - offset, position[1] - 100)
                bigger_position = (position[0] + offset*3 , position[1] - 100)

                # Draw smaller and bigger stars recursively
                _draw(current_node.smaller, smaller_position, level + 1, "blue")
                _draw(current_node.bigger, bigger_position, level + 1 , "red")
        
        _draw(self.root)  #which is the sun
        screen.exitonclick()





