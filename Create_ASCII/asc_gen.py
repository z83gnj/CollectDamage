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
            min = value
            max = 0
        else:
            typeOfLoad = "Drive"
            min = 0
            max = value

        content = (f"\
BEGINN \n \
SPALTENBREITE = [ 16 ]\n \
SPALTENOFFSET = [ 1 ]\n \
KANALNAME = [ {typeOfLoad} ]\n \
LAENGE = [ 3 ]\n \
EINHEIT = [ 'Nm' ]\n \
MINIMUM = [ {min} ]\n \
MAXIMUM = [ {max}]\n \
ANFANG = [ 0.0 ]\n \
DELTA = [ 1 ]\n \
ENDE\n \
    0.000000e+00\n \
    {value:.6e}\n \
    0.000000e+00")
        
        filename = f"TimeSeries_{int(abs(value))}_{typeOfLoad}_{nrOfFile:>03}.asc"
        ascii_file = open(filename, "w")
        ascii_file.write(content)
        ascii_file.close()
        nrOfFile += 1

def main ():
    #listOfValues = read_list("values.txt")
    listOfValues = create_list(-10, 60, 40)

    create_asc(listOfValues)

if __name__ == "__main__":
    main()
    
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