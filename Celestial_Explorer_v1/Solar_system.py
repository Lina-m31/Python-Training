import View
import constellation as cs


##Creat a solar system using our solar system planets

solar = cs.solar_system()
solar_system_planets = [
    cs.Planet("Mercury", 3.3011e23, 2439.7, 0.39, (0, 0, 0), 88, "Sun","gray50"),
    cs.Planet("Venus", 4.8675e24, 6051.8, .72, (0, 0, 0), 224.7, "Sun","darkKhaki"),
    cs.Planet("Earth", 5.972e24, 6371, 1, (0, 0, 0), 365.25, "Sun","blue"),
    cs.Planet("Mars", 6.4171e23, 3389.5, 1.52, (0, 0, 0), 687, "Sun","red"),
    cs.Planet("Jupiter", 1.8982e27, 69911, 5.2, (0, 0, 0), 4333, "Sun","chocolate"),
    cs.Planet("Saturn", 5.6834e26, 58232, 9.54, (0, 0, 0), 10759, "Sun","khaki"),
    cs.Planet("Uranus", 8.6810e25, 25362, 19.2, (0, 0, 0), 30687, "Sun","lightblue1"),
    cs.Planet("Neptune", 1.02413e26, 24622, 30.6, (0, 0, 0), 60190, "Sun","deepskyblue"),
    cs.Planet("Pluto", 1.30900e22, 1188.3, 39, (0, 0, 0), 90560, "Sun","brown1")  
]

for planet in solar_system_planets:
    solar.insert_planet(planet)



## Creating constellation of 5 stars inclusing the sun 

constellation=cs.Constellation("Sun",696340)
constellation.insert("Proxima Centauri",107280)
constellation.insert("Alpha Centauri B", 60268)
constellation.insert("Betelgeuse", 8870)
constellation.insert("sirius", 1190741)


## get the moon phase for a specific date and get the viw of a specific constellation 

#View.Moon_Phase("2024-07-15")
#View.constellations("2024-07-06","and")
#print(cs.Star.number_of_stars)
#constellation.draw()
#solar.draw_planets()
#solar.print_planets()


