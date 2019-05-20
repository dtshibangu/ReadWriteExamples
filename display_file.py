# this program displays the contents
# of the file

def main():
    # get the name of the file
    filename = input( "Enter name of file: " )

    try:
        # open the file
        infile = open( filename, 'r' )

        # read contenst of file
        contents = infile.readline()

        # display file's content
        print( contents )

        # close the file
        infile.close()
        
    except IOError:
        print( "An error occured while trying to read" )
        print( "the file", filename ) 

# call the main fucntion
main()
