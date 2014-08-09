import csv
from pprint import pprint
import re

ifile  = open('C:/Users/oganel/Desktop/chaigan.csv', "rt")
ofile  = open('C:/Users/oganel/Desktop/not_yet_called.csv', "wt", newline='')    
writer = csv.writer(ofile, delimiter= ',', quotechar='"', quoting=csv.QUOTE_ALL, dialect='excel')




def CleanNumber(number):
    return number

def CleanNumbers(RoughNumbers):
    cleannumbers = []
    for row in RoughNumbers:
        cleannumbers.append(CleanNumber(row[0]))
    return cleannumbers
         
def RemoveUnneeded(cleannumbers):   
        pass

# takes the numbers adds phone formatting        
def FormatOutput(cleannumbers):
        pass
  
def RemoveDuplicates(cleannumbers):
    pass
    
def WriteToFile (cleannumbers):
    for number in cleannumbers:
        writer.writerow([number])

RoughNumbers = csv.reader(ifile)
cleannumbers = CleanNumbers(RoughNumbers)
RemoveUnneeded(cleannumbers)
FormatOutput(cleannumbers)
RemoveDuplicates(cleannumbers)
WriteToFile(cleannumbers)
ifile.close()
ofile.close()