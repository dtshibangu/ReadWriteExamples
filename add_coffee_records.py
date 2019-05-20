# This program add coffee inventory records to
# the coffee.txt file

def main():
    # create a variable to control the loop
    another = 'y'

    # open the coffee.txt file in append mode
    coffee_file = open( 'coffee.txt', 'a' )

    # add records to the file
    while another == 'y' or another == 'Y':
        # get the other coffee record data
        print( "Enter the following coffee data:" )
        descr = input( "Descrption: " )
        qty = int( input( "Quantity (in pounds):" ) )

        # append the data to the file
        coffee_file.write( descr + '\n' )
        coffee_file.write( str( qty ) + '\n' )

        # determine whether the user wants to add
        # another record to the file
        print( "Do you want to add another file?" )
        another = input( "Y = yes, anything else = no: " )

    # close the file
    coffee_file.close()
    print( "Data appende to coffee.txt" )

# call the main function
main()
