####################################################################
# Created by: Akos Matiny TDRHS4                                   #
#             akos.matiny@zf.com                                   #
# Desription:                                                      #
#    This script collect the femMeshStarin output file "*.hwascii" #
#    in a user defined folder and it filter the damage values.     #
#    The d>0 damage values are collected in a excel file.          #
#    Plese run the script in the dierctory wich contains           #
#    the hwascii files.                                            #
# Required additional module:                                      #
#    xlsxwriter --> for export data to excel                       #
# To install module use:                                           #
#       pip install xlsxwriter                                     #
####################################################################
import os
from tkinter import N
import xlsxwriter

def CheckExcelFile():
    try:
        with xlsxwriter.Workbook('Damage.xlsx') as workbook:
            return True
    except xlsxwriter.exceptions.FileCreateError:
        return False

# Export to excel with xlsxwriter
def WriteToExcel (AllResults, FileNames, nrOfFile):
    with xlsxwriter.Workbook('Damage.xlsx') as workbook:
        for i in range(nrOfFile):
            SheetName = FileNames[i][:-8]
            if len(SheetName) > 31:
                tempName = SheetName[:27] + ("_%.3d" % (i+1))
                print(SheetName,' is renamed to ',tempName)
                SheetName = tempName
            worksheet = workbook.add_worksheet(SheetName)
            worksheet.write('A1','Node')
            worksheet.write('B1', 'Damage')
            for row_num, data in enumerate(AllResults[i]):
                worksheet.write_row(row_num+1, 0, data)
    print('Damage.xlsx',' has been written!')    

def main():
    if not CheckExcelFile():
        print("Unable to open the Damage.xlsx file!!!\nCheck the permmission or the closed state! ")
        input("Press Enter to continue...")
        return -1
    # Collecting the hwascii file in the folder
    ListofFiles = []
    results=[]
    for x in os.listdir():
        if x.endswith(".hwascii"):
            # Add only the hwascii files to the list
            ListofFiles.append(x)
    # If there are not hwascci files the script end
    if not ListofFiles:
        print("No hwascii file in directory")
        input("Press Enter to continue...")
        return 0

    # Open the files
    Nrfiles = 0
    for ResFile in ListofFiles:
        countRow=0
        Row=0
        node, damage = [], []
        with open(ResFile) as f:
            print(ResFile,'is opened')
            next(f) # Skip the first row of the file
            isDamage=True
            for line in f.readlines():
                # Coolect the node numbers and values for d>0
                if line[0] != '$' and isDamage:
                    fields = line.split()
                    if float(fields[1]) > 0:
                        node.append(int(fields[0]))
                        damage.append(float(fields[1]))
                        Row+=1
                # Checking and skiping the frirst section heder
                elif line[0] == '$' and countRow < 5:
                    countRow +=1
                    #print('elsoheader', line)
                # Break for loop if the damage section is finish
                else:
                    #print('end')
                    isDamage=False
                    break
            print('Found',Row,'d>0 value')
            # Collection the results
            nodeDam = [[0 for i in range(2)] for j in range(Row)]
            for i in range(Row):
                nodeDam[i][0]=node[i]
                nodeDam[i][1]=damage[i]
            results.append(nodeDam)
            Nrfiles +=1

    # Write node - damage to excel file
    WriteToExcel(results, ListofFiles, Nrfiles)
    print(Nrfiles)
    print(len(ListofFiles))
    input("Press Enter to continue...")


if __name__ == "__main__":
    main()

