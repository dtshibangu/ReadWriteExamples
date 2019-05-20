# thisi program calcuates the number of correct
# answers and displays the output

def main():
    # create a list of user answers
    answers_list = []
    # create a list for correct answers
    correct_list = [ 'A', 'C', 'A', 'A', 'D',
                     'B', 'C', 'A', 'C', 'B',
                     'A', 'D', 'C', 'A', 'D',
                     'C', 'B', 'B', 'D', 'A' ]

    #create constants for data
    QUESTIONS = 20

    # accumulator for correct answers
    right = 0

    # read answers from text file
    infile = open( 'student_answers.txt', 'r' )

    # read the first line
    answers = infile.readline()

    # read each line and append to answer list
    while answers != '':
        answers = answers.rstrip( '\n' ) 
        answers_list.append( answers )

        # read the next line
        answers = infile.readline()

    # close the file
    infile.close()

    # match both lists and add correct
    # answers to tally
    for index in range( QUESTIONS ):
        if answers_list[ index ] == correct_list[ index ]:
            right += 1
            print( "Correct: #", index+1, sep='' )
            
        else:
            print( "Wrong: #", index+1, sep='' )
            print( "Correct Answer:", correct_list[ index ] )
            print()

    # if score is 15 or over, then they pass
    print( "\nYour score is: ", right, "/", QUESTIONS, sep='' ) 
    if right >= 15:
        print( "You passed!" )
    else:
        print( "You failed, kid." )

# call the main function
main()

'''CHALLENGE = GROUP TASKS INTO FUNCTIONS'''
            

    
    
