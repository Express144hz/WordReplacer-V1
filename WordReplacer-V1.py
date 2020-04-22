# Created by Express | 22/04/2020 | 17:07
# Program for word suppression based on search.

import os
import sys
import fileinput

text = input("Text to search :")
replace = input("Text to replace :\n")
files = input("File directory : ")

File = open( files, 'r+' )
match = 0

for line in fileinput.input( files ):
    if text in line :
        match += 1
    else:
        continue
    File.write( line.replace( text, replace ) )

print('{} Matchs Found !'.format(str(match)))
File.close()

input('\nPress Enter to exit :')