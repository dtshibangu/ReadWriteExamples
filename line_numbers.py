# this program returns the contents 
# of a given file, including line numbers

def main():
    # a variable asks user for file
    userfile = input( "Enter file name: " )
    userfile = userfile + '.txt'
    line_num = 1

    # open the file from user
    userfile = open( userfile, 'r' )

    #read first line of file
    line = userfile.readline()

    # while the counter is less than 5
    # keep printing out lines from file
    while line != '':
        # strip the newline
        line = line.rstrip( '\n' ) 

        # print line number with content
        print( str(line_num) + ':', line ) 

        # read the next number
        line = userfile.readline()
        # increase line number by 1
        line_num += 1

    # close the file
    userfile.close()

# call the main funtion
main()
        
