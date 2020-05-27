# AND operators are written as "and" in python
# OR operators are written as "or" in python

print( "Program calculates the BMI of a person" )
print( "\n" )

h = float( input( "Please height in metres: " ) )
w = float( input( "Please weight in kg: " ) )

BMI = w / ( h ** 2 )
print( "your BMI is", round( BMI, 2 ) )

if ( BMI <= 18.5 ):
    print ( "and you're underweight" )
elif ( BMI > 18.5 and BMI <= 24.9 ):
    print ( "and you've Normal weight" )
elif ( BMI > 24.9 and BMI <= 29.9 ):
    print ( "and you're Overweight" )
else:
    print ( "and you're Obese" )
    
              
