print( "Program asks user for a number, converts it to miles and prints the result" )
# 1 mile = 1.609344 km

km = float( input( "Please enter num of kilometres: " ) )

miles = km / 1.609344

print( "the result is ", round( miles, 2 ), "miles" )
