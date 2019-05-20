# the program should create a dictionary of codes and
# encrypt a file wfter reading its contents
# the string for holding encryptions

def main():
    codes = { 'a': '!', 'b':'&', 'c':'(',
              'd':'*', 'e':'^',
              'f':'$', 'g':'@', 'h':'`',
              'i':'~', 'j':'-',
              'k':'_', 'l':'=', 'm':'+',
              'n':'[', 'o':'{',
              'p':']', 'q':'}', 'r':'|',
              's':';', 't':':',
              'u':'\'', 'v':'?', 'w':'>',
              'y':'.', 'z':',', ' ':' '}

    # this string holds the 
    string = ''

    # open the file
    infile = open( 'encrypt.txt', 'r' )

    # read the first line
    line = infile.readline()

    while line != '':
        for letter in line.lower():
            if letter in codes.keys():
                string += codes[ letter ]

        # read the next line
        line = infile.readline()

    # close the file
    infile.close()

    # add string contents to anothwer file 
    outfile = open( 'decrypt.txt', 'w' )

    # for each line in string, write to decrypt.txt
    for line in string:
        outfile.write( line )

    # close the file 
    outfile.close()

#call main
main()
 

    
