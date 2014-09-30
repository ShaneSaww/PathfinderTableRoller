#!/usr/bin/env python
#############################################
# Pathfinder.py a program that reads input from a text file and rolls on it. 
# This program is created to help test random race creation/ revive lists. This list can have many rolling tables that call other rolling tables. 
# More details on the FF exist in the FF. 
#Created by: Shane
#
#Future Goals: Some sort of UI, better error handling. 
#############################################

import random
import os
import collections
###
## This function is used to roll a D100. A D100 can only roll from 1 - 100 NO ZEROs
## Passed Variables are OPT and CHANCE, both should be arrays with OPT has all the possibility and CHANCE has the chances of those. 
## OPT = HUMAN,DWARF,HAFLING                CHANCE = 50, 75 ,100 
## With the example above Human comes in on a roll 1-50, Dwarf from 5-75, and Halfing from 75-100
#
def PickTable(opt,chance):
    roll,x = random.randint(1,100),0
    if roll == 100:
        roll = 99
    for n in opt:
        if roll <= chance[x]:
            return(n)
        else:
            x=x+1
##DEFINE VARIBLES 
raceopt = []
racechance = []
tablelist = []
tableopt = []
tablechance = []
tablepick = " "
racewinner = []
rolls = 0
racecount = []
flagg = 0
## Open FF with the input and one for output
## I should add some error handling here. 
f = open('C:/pyt/RollInput.txt')
fw = open('C:/pyt/RollOutput.txt', 'w')

for line in f:
    if line[0] == '#': ## Check for commented lines in the FF
        continue
    if flagg == 0:
        rolls = int(line) ## The first line in the file is how many times you want to roll on the table(s)
        flagg = 1 ## done with first line, NEVER COME BACK
        continue
    line = line.rstrip('\n') ## Remove any new line chars from the line. 
    if line == '--New Table':
        continue ## do nothing if it's a table start. 
    elif line == '--End Table':
		# In this part we are creating a table of table values and chances so we can roll on everything later
		# The advantage of doing this is if the table list in the FF is out of order we don't have to read over everything. 
        #Add racechance/raceopt into a array for later
		#Once you are at the end of the table store table values.
		#I should move this to the end of the for loop...
        tableopt.append(raceopt)
        tablechance.append(racechance)
        raceopt = []
        racechance = []
    else:
        if not line[0].isdigit():
            tablelist.append(line)
			## If the line has no digit at the start this means we table name! Store this value to come back into it. 
        else:
			## Start creating the chance and value parts of the two arrays needed to roll on.
            raceopt.append(int(line[:2]))
            racechance.append(line[3:])
## This below loop we go pick one race each time through and the input(rolls) is set in the FF.
## the rolls value is how many times we want to pick a value from the list. 
for x in range(0,rolls):
## Now we have all the table names, values, and chance. LETS ROLL!
    for x, table in enumerate(tablelist):
        if tablepick == ' ':
			## First time in here. Roll on the top most/ first table. 
            tablepick = PickTable(tablechance[x],tableopt[x])
        elif tablepick in tablelist:
			## The value rolled from before is another table, lets find that table and roll on it. 
            i = tablelist.index(tablepick)
            tablepick = PickTable(tablechance[i],tableopt[i])
        else:
			## We rolled a value and that value is not a table. We can press forward. 
            continue
	# We picked a winner, lets store it  then finish the outside loop. 
    racewinner.append(tablepick)
    tablepick = ' '
## convert the racewinner array into a set so we can do some quick counting
raceset = set(racewinner)
## we will count how many times each race won, and what percent it was selected. 
for qk in raceset:
    racecount.append(str(qk +" was rolled " + str(racewinner.count(qk)) + " times Which is a " + str((racewinner.count(qk)/rolls)*100) +"% "))
for qk in racecount:
    fw.write(str(qk) + str())
    fw.write("\n")
fw.write("-----------------------------------------------------------\n")
for ele in racewinner:
    fw.write(ele + "\n")
    
## Close up all the files.
f.close
fw.close
    


    
    