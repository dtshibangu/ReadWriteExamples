# this program reads and displays the contents
# of the philosophers.tct file.
def main():
    # open a file named philosophers.txt
    infile = open( 'philosophers.txt', 'r' )

    # read the file's content
    file_contents = infile.read()

    # close the file
    infile.close()

    # print the data that was read into
    # memory
    print( file_contents )

# call the main function
main()
