# this program will ask the user for a file name
# then displays the first five lines from that file


def main():
    # a variable asks user for file
    userfile = input( "Enter file name: " )
    userfile = userfile + '.txt'
    counter = 0

    # open the file from user
    userfile = open( userfile, 'r' )

    #read first line of file
    line = userfile.readline()

    # while the counter is less than 5
    # keep printing out lines from file
    while counter != 5:
        # strip the newline
        line = line.rstrip( '\n' ) 
        
        print( line )
        counter += 1

        # read the next number
        line = userfile.readline()

    # close the file
    userfile.close()

# call the main funtion
main()
        
