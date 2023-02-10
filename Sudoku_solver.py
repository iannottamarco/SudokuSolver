# Import libraries
import numpy as np
import pyautogui as pg
import time
import math



# Create empty list to be filled with the sudoku rows
grid = []


# Insert the 9 rows
def Create():

    """ This function is needed to get the Sudoku input by rows.
        The input required is every number of each row one by one, without commas.
        Example: 027390030 (then click enter and proceed with the following row). """

    while True:
        row = list(input('Please input the whole row of numbers without commas: '))
    
        if len(row) != 9: # Do not append the input if the lenght is not equal to 9
            print('You need to type 9 numbers!')
        else:
            ints = [] 

            [ints.append(int(n)) for n in row] # Separate the numbers and convert it to integer

            grid.append(ints) # Attach the list to the Sudoku "matrix" (actually is a list)

            if len(grid) == 9: # Close the loop when the "matrix" has 9 rows
                #print('Row ' + str(len(grid)) + ' complete')
                break
            #print('Row ' + str(len(grid)) + ' complete')

    time.sleep(3) # To give us some time to switch to the Sudoku after running the script


def Possible(y,x,n):

    """ Define a function that checks wheter that number (n) can fit into that (x,y) spot
    n = number from 1 to 9
    x = spot of the number in the row
    y = spot of the number in the column """

    global grid
    # Check the row
    for i in range(0,9): # row position is fixed [y] and [i] changes
        if grid[y][i]==n: 
            return False
    
    # Check the column
    for i in range(0,9):
        if grid[i][x] == n:
            return False
    
    # Check the box
    x0= (x//3)*3 # Return x location of the leftmost item in that box
    y0= (y//3)*3 # Return y location of the upper item in that box
        # Basically the code above brings every x,y coordinates you ingest to the upperleft location of the box where x,y are located

    for i in range(3): # 3 columns in the box
        for j in range(3): # 3 rows in the box
            if grid[y0+i][x0+j] == n:
                return False
    
    return True



def Print(matrix):

    # Reverse the solution of the Sudoku
    reversed_matrix = []

    for i, list in enumerate(matrix):
        if i%2 == 0:
            reversed_matrix.append(list)
        else:
            reversed_matrix.append(list[::-1])


    # Create string version of the matrix
    str_fin = []

    for lists in reversed_matrix:
        for num in lists:
            str_fin.append(str(num))
    

    # Put the numbers into the Sudoku
    counter = 0

    for i, num in enumerate(str_fin):
        
         # Press the key num (passing the string)
        if (math.floor(i/9))%2 == 0:
            pg.press(num)
            pg.hotkey('right')
            counter += 1
        
        # Press the key num (passing the string)
        elif (math.floor(i/9))%2 != 0:
            pg.press(num) 
            pg.hotkey('left')
            counter += 1

        # Press the down arrow to pass to the next row
        if (counter%9 == 0) and (counter != 81):
            pg.hotkey('down')

def Solve():
    global grid
    for y in range(9): # to iterate through rows
        for x in range(9): # to iterate trough columns
            if grid[y][x] == 0: # If the spot is empy in the grid
                for n in range(1,10):
                    if Possible(y,x,n): # Check using the possible function which number can we put there
                        grid[y][x] = n
                        Solve() # Backtracking if the choice made was wrong
                        grid[y][x] = 0 # Change latest grid created but we turn back the n to zero
                return # When there are no more empty spots left
    print('Solving...')
    print(np.matrix(grid))
    Print(grid)
    input('Do you want to see more solutions?')


Create() # Run the function to create the Sudoku

Solve() # Solve it