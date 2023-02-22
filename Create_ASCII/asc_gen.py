import argparse

def create_list (min, max, inc):
    """
    Create a list based on the min, max and the increment values.
    The min and max values is included.
    """
    values = []
    while min <= max:
        if min == 0:
            min += inc
            continue
        values.append(min)
        min += inc

    return values    

def read_list (filename):
    """
    Read a list from the given file.
    """
    values = []
    with open(filename) as value_file:
        for value in value_file.readlines():
            values.append(float(value))
    
    return values

def create_asc (values):
    """
    Create the ASCII timehistory file
    """
    nrOfFile = 0
    for value in values:
        if value < 0 :
            typeOfLoad = "Coast"
        else:
            typeOfLoad = "Drive"

        content = (f"\
BEGINN \n \
SPALTENBREITE = [ 16 ]\n \
SPALTENOFFSET = [ 1 ]\n \
KANALNAME = [ {typeOfLoad} ]\n \
LAENGE = [ 3 ]\n \
EINHEIT = [ 'Nm' ]\n \
MINIMUM = [ 0 ]\n \
MAXIMUM = [ {abs(value)}]\n \
ANFANG = [ 0.0 ]\n \
DELTA = [ 1 ]\n \
ENDE\n \
    0.000000e+00\n \
    {abs(value):.6e}\n \
    0.000000e+00")
        
        filename = f"TimeSeries_{typeOfLoad}_{nrOfFile:>03}.asc"
        ascii_file = open(filename, "w")
        ascii_file.write(content)
        ascii_file.close()
        print(f"{filename} has been written!")
        nrOfFile += 1

if __name__ == "__main__":

    parser = argparse.ArgumentParser(prog="asc_ge.py",
                            description="Create a Techware ASCII timeseries files based on the given values",
                            epilog="Ez meg mi lesz")
    
    parser.add_argument("-o", "--Output", nargs=3, type = float, help = "Show Output")
    parser.add_argument("-l", "--List", help = "Show list") 
    # Read arguments from command line
    args = parser.parse_args()
    
    print(len(vars(args)))

    if args.Output:
        print("Displaying Output as: % s" % args.Output)

    if args.List:
        print("Displaying Output as: % s" % args.List)
    #listOfValues = read_list("values.txt")
    #listOfValues = create_list(-10, 60, 10)

    #create_asc(listOfValues)

"""
Example of the Tecware-ASCII format:             
BEGIN                                          
SPALTENBREITE = [  15, 15]                     
SPALTENOFFSET = [  1, 1]                       
KANALNAME = [ 'Constant_1_nr1','Mx_pos' ]       
LAENGE = [  2, 2 ]                             
EINHEIT = [ 'n/a','MNm']                       
MINIMUM = [  1, 2.9403e-02]                    
MAXIMUM = [  1, 2.9954e-02]                     
ANFANG = [  0, 0]                              
DELTA = [  1.000000e-02, 1.000000e-02]         
ENDE                                           
    1.0000e+00      2.9954e-02                 
    1.0000e+00      2.9403e-02 

"""