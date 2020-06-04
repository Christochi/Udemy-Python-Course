# Program makes an HTTP request to Open Trivia API at each round of the game
# to get new question and presents it to the user to answer.
# At the end of each round, ask the user if he wants to play again.
# Keep playing until the user types "quit"
# Program tells the user if the answer is correct or not at each round and
# keep's the user's score

import json
import requests
import pprint
import random
import html

score = 0; # points gained at each round
play = "" # placeholder for holding user's decision to play again or not
question_counter = 0 # question counter


while play != "quit":
    # send HTTP requests to Trivia REST API
    url = requests.get( "https://opentdb.com/api.php?amount=1&category=18&difficulty=easy&type=multiple" )

    # status of the request
    #print( url.status_code )

    # convert json to dictionary/string
    qst = json.loads( url.text )
    # pprint.pprint( qst ) # to display qst in readable format

    # store answers
    answers = qst[ 'results' ][ 0 ][ 'incorrect_answers' ] # store incorrect answers
    correct_answer = qst[ 'results' ][ 0 ][ 'correct_answer' ] # store correct answer
    answers.append( correct_answer )
    random.shuffle( answers ) # shuffles the list of answers
    
    # display question.
    # 0 is the index of the list in results
    print( html.unescape( qst[ 'results' ][ 0 ][ 'question' ] ) )
    question_counter += 1 # increments by 1
    print( "\n" ) 

    # display answer
    answer_num = 1 # answer label
    for a in answers:
        print( str( answer_num ) + ":", html.unescape( a ) )
        answer_num += 1
        
    print( "\n" )
    
    valid_answer = False # flag for answer validation
    while valid_answer == False:
        user_answer = input( "Please type the number associated with your answer: " )  # prompt
        try:
            user_answer = int( user_answer )
            # checks if user_ answer is greater than the size of answers list
            # or answer number
            if user_answer > len( answers ) or user_answer <= 0:
                print( "Invalid Answer" )
            else:
                valid_answer = True # set flag to True
        except:
            print( "Invalid answer. Use only numbers. " )
            
    result = answers[ int(user_answer) - 1 ]

    # checks for the correct answer
    if result == correct_answer:
        print( "correct answer" ) # display
        score += 1 # increment by 1
    else:
        print( "incorrect answer" ) # display
        print( "The correct answer is",
                 html.unescape( qst[ 'results' ][ 0 ][ 'correct_answer' ] ) )

    # ask the user if they would like to continue playing
    print( "\n" )
    print( "Would you like to continue playing" )
    play = input( "Type quit to stop, type anything to continue: " ) # prompt
    print( "\n" )

print( "Your total point is", score, "out of", question_counter ) # print result
