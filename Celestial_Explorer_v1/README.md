# Project Description:

Celestial Explorer is a small project that makes exploring the sky more fun, the V1 of the project have 2 modules : view module and constellation module which provide below features:

1- using the module "View" that uses AstronomyAPI ( https://docs.astronomyapi.com/ ) and logtitude/latitude for Amman,  you can get the moon phase for a specific date to track the moon phase, and the time of its rising and setting. simply you need to import the module view and send the request:
 View.Moon_Phase("date format yyyy-mm-dd")

 2- The view module can also retirn a picture of a constellation as per user request for specific date, for example below command will display a picture of Andromeda constellation on 6th of July:
 View.constellations("2024-07-06","and")

2- using the module "constellation" , you can list the planets in our solar system and its radiuses, also you can view the planets around the sun to give you a good perspective of the planets sizes compared to each other, you can also add planets and creat your own solar_system.

3- Using the module "constellation" you can also insert stars to a Tree of stars that uses our sun as reference and sorts the stars based on its size compared to the sun, then you can view the inserted stars in a scaled screen to see the different of sizes between the stars.

## requirnments:

The code uses math and turtle libraries, also it uses a list of other libraries that are all included in the environment attached to this file .

## Limitations:
Due to the way the jupyter notebook runs the loops , running the turtle screen in a jupytor notebook will cause some issues, so please run the code using .py file. 

