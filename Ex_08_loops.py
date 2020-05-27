import random

print( "Program asks the user 8 names of people and stores them in a list.",
           "Picks a random name and prints it." )

#count = 1 # loop counter
nameList = [] # list of names

#while count <= 8: (alternative with while loop )
for count in range( 0, 8 ):
    names = input( "Please enter 8 names: " )
    nameList.append( names )
    #count += 1

people = random.randint( 0, 7 )
print( "Random person:", nameList[people] )

print( "--------------------" )

print ( "Program creates a guess game with the names of the colors." )

# list of colours
colours = [ "red", "blue", "green", "yellow", "white" ]
guess = "yes"
num = random.randint( 0, len( colours) - 1 )

while guess == 'yes':
    guess = input( "Please guess a colour from this list [ red, blue, green, yellow, white ]: " )

    if ( guess.lower() == colours[ num ] ):
        guess = input( "correct guess. Would you like to play again (yes/no): " )

        if (guess.lower() == 'no'):
            break
    else:
        guess = input( "wrong guess. Would you like to play again (yes/no): " )

        if (guess.lower() == 'no'):
            break



