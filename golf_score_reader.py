# this program reads records from golf.txt file
# and displays them

def main():
    # define variables of fields
    name = ''
    score = 0

    try:
        # open the file
        infile = open( 'golf.txt', 'r' )

        # read the first record
        name = infile.readline()

        while name != '':
             # read the score data
            score = str( infile.readline() ) 

            # strip the newline
            name = name.rstrip( '\n' )
            score = score.rstrip( '\n' )

            # print the results to shell
            print( name )
            print( score ) 

            # read the next data
            name = infile.readline()
    
        # close the file
        infile.close()

    except IOError:
        print( "That file cannot be found.")
    except Exception as err:
        print( err )

# call the main function
main()

    
             
    
            
            

            
        
