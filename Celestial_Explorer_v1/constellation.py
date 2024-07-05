import math 
import turtle


#creat planets and add them to a list
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
    



class solar_system:
    planets = [] 
    
##Inserting planets to the solar_system
    def __init__(self):
        self.planets = []
        

    def insert_planet(self, planet):
        self.planets.append(planet)

    ## print planets
    def print_planets(self):
        for planet in self.planets:
            print(planet)

    ## Draw the solar system 
    def draw_planets(self):
        t = turtle.Turtle()
        screen = turtle.Screen()
        screen.setworldcoordinates(-1000, -1000, 1000, 1000)
        t.speed(0)
        
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




class Constellation:

    R=696340

    def __init__(self, name=None, radius=0):
        self.root = Star(name,radius) if name else None
        
        

    def insert(self, name, radius):
        if self.root is None:
            self.root = Star(name, radius)

        else:
            self._insert(self.root, name, radius)


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


    def inorder_traversal(self, node):
        values = []
        if node:
            values = self.inorder_traversal(node.smaller)
            values.append(node.name)
            values += self.inorder_traversal(node.bigger)
        return values

    

    @classmethod
    def draw_star(cls, t, radius, position , color):
        t.penup()
        t.goto(position)
        t.pendown()
        t.dot(radius/400 , color)
    
    def draw(self):
        # Initialize turtle
        t = turtle.Turtle()
        screen = turtle.Screen()
        screen.setworldcoordinates(-1000, -1000, 1000, 1000)
        t.speed(0)
        
        def _draw(current_node, position=(0, 0),level=0 , color="yellow"):
            if current_node:
                # Scale radius for drawing
                new_radius = (current_node.radius / (Constellation.R/1000)) * 50
                
                # Draw the current star
                self.draw_star(t, new_radius, position , color)
                
                #defining offset to draw the stars seperatly
                offset = 200 / (level + 1)
                smaller_position = (position[0] - offset, position[1] - 100)
                bigger_position = (position[0] + offset*3 , position[1] - 100)

                # Draw smaller and bigger stars recursively
                _draw(current_node.smaller, smaller_position, level + 1, "blue")
                _draw(current_node.bigger, bigger_position, level + 1 , "red")
        
        _draw(self.root)
        screen.exitonclick()





#print( constellation.search(695.7))  
#print( constellation.search(500.0))  
#print( constellation.inorder_traversal(constellation.root))
#print(constellation.root)


"""constellation=Constellation("Sun",696340)
constellation.insert("Proxima Centauri",107280)
constellation.insert("Alpha Centauri B", 60268)
constellation.insert("Betelgeuse", 8870)
constellation.insert("sirius", 1190741)
#Star.number_of_stars
#constellation.draw()"""



"""solar = solar_system()
solar_system_planets = [
    Planet("Mercury", 3.3011e23, 2439.7, 0.39, (0, 0, 0), 88, "Sun","gray50"),
    Planet("Venus", 4.8675e24, 6051.8, .72, (0, 0, 0), 224.7, "Sun","darkKhaki"),
    Planet("Earth", 5.972e24, 6371, 1, (0, 0, 0), 365.25, "Sun","blue"),
    Planet("Mars", 6.4171e23, 3389.5, 1.52, (0, 0, 0), 687, "Sun","red"),
    Planet("Jupiter", 1.8982e27, 69911, 5.2, (0, 0, 0), 4333, "Sun","chocolate"),
    Planet("Saturn", 5.6834e26, 58232, 9.54, (0, 0, 0), 10759, "Sun","khaki"),
    Planet("Uranus", 8.6810e25, 25362, 19.2, (0, 0, 0), 30687, "Sun","lightblue1"),
    Planet("Neptune", 1.02413e26, 24622, 30.6, (0, 0, 0), 60190, "Sun","deepskyblue"),
    Planet("Pluto", 1.30900e22, 1188.3, 39, (0, 0, 0), 90560, "Sun","brown1")  
]


for planet in solar_system_planets:
    solar.insert_planet(planet)"""

#solar.print_planets()
#solar.draw_planets()



