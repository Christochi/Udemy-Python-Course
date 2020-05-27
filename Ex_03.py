import math

print( "Program ask the user for radius and calculates the area and circumference of a circle" )

radius = float( input( "Please enter radius: " ) )

print( "Area =", round( ( math.pi * ( radius ** 2 ) ), 2 ) )
print( "Circumference =", round( ( 2 * math.pi * radius ), 2) )
