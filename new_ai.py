from re import I
from syslog import LOG_LOCAL0
#from tetris import Figure

def generate_positions(playField, figures):
    """Generate all the possible positions that are possible
        Returns a list of all the positions relative point (0,0)"""
    # finds state space 
    # determines all potential final placements of the piece on the board

    # do we really need to generate every last position possible, or can we just find the positions right before the collision occurs?

    # start with rotation 1
    # A. place piece at 0,0
    # 1. test if collision
    # 1a. If no collision, then add to list
    # 1b. If collision, continue
    # 2. move right
    # 3. repeat 1-2 until we collide or hit the bottom
    # B. if there's no more rotations, we're done
    #   otherwise, switch to next rotation and repeat from A

    # deficiencies:
    # will place a piece into holes when they are large enough. how do we deal with this?
    # Go down then right instead. 
    # When we collide on the way down, finish that column and move right.

    fieldHeight = len(playField)
    fieldWidth = len(playField[0])
    numRotations = len(figures)

    Positions = []

    r = 0
    x = 0
    y = 0

    for r in range(numRotations):
        RotationPositions = []
        for x in range(fieldWidth): #columns
            
            for y in range(fieldHeight): #rows
                if not (collision_check(playField, figures[r], x, y)) :
                    RotationPositions.append([x,y])
                else:
                    break
        Positions.append(RotationPositions)
    
    return Positions


def collision_check(playField, figure, xpos, ypos): 
    #copied code from tetris.py and modified it (changed variable names) for our use.
    #xpos and ypos are position of the figure on the playField

    intersection = False

    height = len(playField)
    width = len(playField[0])

    for i in range(4):
        for j in range(4):
            if i * 4 + j in figure:
               if i + ypos > height - 1 or \
                       j + xpos > width - 1 or \
                       j + xpos < 0 or \
                       playField[i + ypos][j + xpos] > 0:
                   intersection = True
    return intersection

def h_generate_positions(playField, figures):
    """Generate all the possible positions that are possible
        Returns a list of all the positions relative point (0,0)"""
    # finds state space
    # determines all potential final placements of the piece on the board

    # do we really need to generate every last position possible, or can we just find the positions right before the collision occurs?

    # start with rotation 1
    # A. place piece at 0,0
    # 1. test if collision
    # 1a. If no collision, then add to list
    # 1b. If collision, continue
    # 2. move right
    # 3. repeat 1-2 until we collide or hit the bottom
    # B. if there's no more rotations, we're done
    #   otherwise, switch to next rotation and repeat from A
    # Heuristics: A piece cannot be suspended in mid-air.
    #           We ignore those invalid positions.

    fieldHeight = len(playField)
    fieldWidth = len(playField[0])
    numRotations = len(figures)

    validPositions = []
    currentValidPosition = []

    r = 0
    x = 0
    y = 0

    for r in range(numRotations):
        validRotationPositions = []
        for x in range(fieldWidth): #columns
            
            for y in range(fieldHeight): #rows
                if not (collision_check(playField, figures[r], x, y)) :
                    currentValidPosition=[x,y]
                else:
                    if (currentValidPosition not in validRotationPositions):
                        validRotationPositions.append(currentValidPosition)
                    break

        validPositions.append(validRotationPositions)
    
    return validPositions

def place_on_playfield(playField, figure, position):

    return playField
    

def find_best_place (playField, figure, weights=None):  #weights to be passed to f()
    """Function to evaluate the different possible positions and find the best according to the modifiers
        Returns the position of the best placement from a list of positions"""
    # takes data from generate_positions and returns the best position using f()
    if weights is None:
        weights = [0.25, 0.25, 0.25, 0.25]
    placements = []  
    
    # find all the valid places
    validPositions = h_generate_positions(playField, figure)
    
    # iterate through the validPositions list. deal with each rotations separately.
    numRotations = len(validPositions)
    for rotation in range(numRotations):
        for position in validPositions[rotation]:
            # place position on playField
            newPlayfield = place_on_playfield(playField, figure, position)

            aggHeight = aggregate_height(newPlayfield)
            numHoles = count_holes(newPlayfield, aggHeight)  
            amtBumpy = bumpiness(newPlayfield)
            completedLines = completed_lines(newPlayfield)

            # call f() to determine the "score" of the placement            
            placementScore = f(aggHeight, numHoles, amtBumpy, completedLines, weights) 
            placement = [position, rotation]
            placements.append([placementScore, placement])

    # find the best (lowest) scoring placement and return that
    bestPlacement = [rotation,position]  # [r,[x,y]]

    return  bestPlacement  # best place returned


def f(aggHeight, numHoles, amtBumpy, completedLines, weights):
    """The evaluation function of a state
        Returns a value 0<x<10? on how good the state is"""
    # decision based on statistics

    score = (aggHeight * weights[0]) + (numHoles * weights[1]) + (amtBumpy * weights[2]) + ( (4 - completedLines) * weights[3])

    return score


def set_mod():
    """Change the modifiers used to the new values"""


def run_ai():
    """Driver class
        Input: figure, field
        Returns the position for the figure
        (Potential for mutil threading for time limit but this is extra)"""

def aggregate_height(playField):
    # Calculate aggregate height
    # Argument: array (play field)
    # Returns: integer (aggregate height)

    # The height of each column is the actual height - number of zeros (excl. holes)
    # so, count the zeros, subtract the total number of holes, then
    # subtract that number from the total number of cells which can be calculated
    # by the length of the list of lists times the length of the inside lists.

    numRows = len(playField)
    numCols = len(playField[0])
    zerocount = 0
    aggHeight = 0
    
    for i in range(numCols):
        for j in range(numRows):

            if (playField[j][i] == 0):
                zerocount += 1
            else:
                break

        aggHeight += (numRows - zerocount)
        zerocount = 0

    return (aggHeight)

def count_holes(playField, aggregateHeight = -1 ):
    # count the number of holes in the playField
    # holes are defined as infilled cells that cannot be accessed.
    # For this, we determine how many empty cells are in the entire playfield
    # then we subtract the total number of cells and add back in the aggregate height
    # this gives us an admittedly inaccurate, but close, number of holes.

    zeroCount = 0
    hole = 0
    holeCount = 0
    
    totalCells = len(playField) * len(playField[0])

    for row in playField:
        zeroCount += row.count(hole)

    if (aggregateHeight < 0):
        holeCount = zeroCount - ( totalCells - aggregate_height(playField) )
    else:
        holeCount = zeroCount - ( totalCells - aggregateHeight )

    return holeCount

def bumpiness(playField):
    #
    # return an array the same length of the number of columns
    # first n entries are the differences between adjacent columns.
    # the final entry is the average bumpiness or sum of the bumpiness
    return 0

def completed_lines(playField): 
    # 
    # applied once a piece is placed.
    # look for lines that have no empty cells
    
    numRows = len(playField)
    numCols = len(playField[0])
    compLines = 0
    for i in range(numRows):
        line = True
        for j in range(numCols):
            if(playField[i][j] == 0):
                line = False
                break
        if(line == True):
            compLines+=1
    return compLines
