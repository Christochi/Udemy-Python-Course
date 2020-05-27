# Program helps the user to type faster
# Gives user a word and ask user to write it 5 times
# Check number of seconds it took user to type the word at each round
# tells the user how many mistakes were made and display a chart with the
# typing speed evolution during 5 rounds

import time as t
import matplotlib.pyplot as plt

word = "awake" # word that will be typed
words = [] # list of words typed
typing_speed = [] # list of typing speed in seconds
counter = 1 # loop counter
err_count = 0 #  typing error counter

# while loop to make sure the user types 5 times
while counter < 6:
    print( "Please type this word:", word, "5 times" ) # message
    start_speed = t.time()
    typed_word = input( "Please type word: " ) # prompt
    end_speed = t.time()
    speed = end_speed - start_speed
    
    # if the word is wrongly type, err_counter increments
    if word != typed_word.lower():
        err_count += 1

    words.append( typed_word ) # add the typed word to the list
    typing_speed.append( speed ) # add the typing speed to the list
    
    #speed = round(time_now, 2) # stores typing speed in sec
    print( "In round", counter, "" + word, "was typed in", str( speed ) + "s" ) # result
    
    counter += 1

print( "You made", err_count, "mistake(s)" )
print( words )

# plot the chart
plt.plot( words, typing_speed ) # plot the chart
plt.ylabel( "Words typed" )
plt.title( "Typing Speed Chart" )
plt.show() # display chart


 
