# this program writes three lines of data
# to a file
def main():
    # open a file named philosophers.rtf
    outfile = open( 'philosophers.txt', 'w' )

    # write the names of three philosophers
    # to the file
    outfile.write( "John Locke\n" )
    outfile.write( "David Hume\n" )
    outfile.write( "Edmund Burke\n" )

    # close the file
    outfile.close()

# call main function
main()
