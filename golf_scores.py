# This program will get data on each pleyer and
# store information in golf.txt

# import the random module
import random 

def main():

    try: 
        # state variables for name and score
        name = ''
        score = 0
        keep_adding = 'y'

        # open the file
        infile = open( 'golf.txt', 'w' )
       

        while keep_adding == 'y' or keep_adding == 'Y':
            # assign each player to a random id number
            player_num = random.randint( 1, 100 ) 

            #promtp for starting name and score
            name = input( "Player name: " )
            score = int( input( "Player Score: " ) )
            
            # write player data to file
            infile.write( "Player #" + str( player_num ) + ': ' +
                          str( name) + '\n' )
            infile.write( "Score: " + str( score ) + '\n\n' )

            keep_adding = input( "Would you like to continue " +
                                 "(y/n): " )

            # this adds an empty line
            print()

        # close the file
        infile.close()

    except IOError:
        print( "The file could not be found." )

    except Exception as err:
        print( err )

# call the main fucntion
main()
            
            
            

    
