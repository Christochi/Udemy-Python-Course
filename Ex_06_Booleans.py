# never store boolean values in a variable with quotation marks because it becomes
# a string

# It is True, not true and False, not false with a small letter "f"

# comparison operators: >, <, ==, !=, >=, <=

# if, elif, else statements are written like this:
# if (num1 > num2):
#    print(...)
# elif (num1 > num2):
#    print(...)
# else:
#    print(...)

print( "Programs asks a user for age and compares it with another age already stored" )
print( "\n" )

myAge = 29
yAge = int( input( "Please enter your age: " ) )

if ( myAge > yAge ):
    print( "you're younger" )
elif ( myAge < yAge ):
    print( "you're older" )
else:
    print( "We are the same age" )

