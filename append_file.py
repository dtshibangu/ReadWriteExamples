# this program adds datat to the existing
# philosophers.txt file
def main():
    # open a file named philosophers.txt
    outfile = open( 'philosophers.txt', 'a' )

    # write data that is to be added via
    # the write function 
    outfile.write( 'Socrates\n' )
    outfile.write( 'Aristotle\n' )
    outfile.write( 'Plato\n' )

    #  close the file
    outfile.close()

# call the main function
main()
