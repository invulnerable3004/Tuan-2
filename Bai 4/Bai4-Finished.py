from os import system
from copy import deepcopy

maze = list()
target_row = 0
target_col = 0
solutions = list()

#get maze from keyboard
def inputMaze():
    rows = input('Number of rows: ')
    rows = int(rows)
    cols = input('Number of cols: ')
    cols = int(cols)
    for i in range(rows):
        temp = list()
        for j in range(cols):
            print('maze[', i, ']', '[', j, '] = ', end='')
            val = input()
            while not val in '01' or val == '':
                print('Please only input value 0 or 1.')
                print('maze[', i, ']', '[', j, '] = ', end='')
                val = input()
            val = int(val)
            temp.append(val)
        maze.append(temp)

#print maze to screen
#input: a two-dimentional list
#output: that list printed on console
def outputMaze(a):
    for i in range(len(a)):
        for j in range(len(a[0])):
            print(a[i][j], '  ', end='')
        print('\n')
    
#check possible move
#input: coordinates of a position in the maze
#output: function returned True if that place can be reached by the mouse and returned False otherwise
def possibleMove(row, col, curr_maze):
    if row > len(maze)-1 or col > len(maze[0])-1 or row < 0 or col < 0: return False
    else: return curr_maze[row][col]==1 or curr_maze[row][col]=='T' 
    
#check if target hasn't been reached
#input: maze
#output: function returned True if the mouse hasn't reach the target yet and False otherwise
def isTargetAlive(a):
    for i in a:
        if 'T' in i: return True
    return False
    
#using backtrack algorithm to solve the task
#input: mouse's current coordinates, number or moves and current maze
#output: if the mouse can reach the target, append the solution to the solutions list as a tuple with the number of moves
def backTrack(mrow, mcol, moves, orig_maze):
    if not isTargetAlive(orig_maze):
        solutions.append((orig_maze, moves))
        return 0
    else:    
        for i in range(mrow-1, mrow+2):
            for j in range(mcol-1, mcol+2):
                if possibleMove(i, j, orig_maze):
                    copy_maze = deepcopy(orig_maze)
                    copy_maze[i][j]='M'
                    backTrack(i, j, moves+1, copy_maze)
                
#output all of the solutions and the best solution to screen
def outputSolutions():
    if len(solutions)==0:
        print("\nThe mouse can't get to that target")
    else:
        print('\nHere are the solutions:')
        for i in solutions:
            print('\n')
            outputMaze(i[0])
        print('\nHere is the best solution:\n')
        solutions.sort(key = lambda x: x[1]) #sorting list base on the number of moves
        outputMaze(solutions[0][0]) #after being sorted, the first object of the list will contain the shortest way
        print('It costs at least ', solutions[0][1], ' moves to get to the target.')
    
inputMaze()

#input mouse's first position
print('Maze built at base 0') #tell the user that first row (column) is at index 0
row = input('Mouse at row number: ')
row = int(row)
col = input('Mouse at column number: ')
col = int(col)
while row > len(maze)-1 or col > len(maze[0])-1:
    print('\nThat position is not even in the maze.')
    print('Please type in a valid position.\n')
    row = input('Mouse at row number: ')
    row = int(row)
    col = input('Mouse at column number: ')
    col = int(col)
maze[row][col] = 'M'

#input target's position
target_row = input('Target at row number: ')
target_row = int(target_row)
target_col = input('Target at column number: ')
target_col = int(target_col)
while target_row > len(maze)-1 or target_col > len(maze[0])-1:
    print('\nThat position is not even in the maze.')
    print('Please type in a valid position.\n')
    target_row = input('Target at row number: ')
    target_row = int(target_row)
    target_col = input('Target at column number: ')
    target_col = int(target_col)
maze[target_row][target_col] = 'T'

#main program
system('cls')
print('First position of the mouse in the maze:\n')
outputMaze(maze)
backTrack(row, col, 0, maze)
outputSolutions()
input('PRESS <ENTER> TO EXIT PROGRAM')