from re import I
from syslog import LOG_LOCAL0
#from tetris import Figure

def check_position():
    #  is any portion of the piece off the grid?
    #
    #  is there a collsion?
    #     if either of these is true, then it is not a valid position.
    return

def generate_positions():
    """Generate all the possible positions that are possible
        Returns a list of all the positions relative point (0,0)"""
    # finds state space 
    # determines all potential final placements of the piece on the board

    return

#copied code from tetris.py and modified it for our use. Notably, the for loop
#xpos and ypos are position of the figure on the playField
def collision_check(playField, figure, xpos, ypos): 
    intersection = False

    height = len(playField)
    width = len(playField[0])

    #print(playField)
    #print(figure)
    #print(xpos)
    #print(ypos)

    for i in range(4):
        for j in range(4):
            if i * 4 + j in figure:
               if i + ypos > height - 1 or \
                       j + xpos > width - 1 or \
                       j + xpos < 0 or \
                       playField[i + ypos][j + xpos] > 0:
                   intersection = True
    return intersection

def find_best_place():
    """Function to evaluate the different possible positions and find the best according to the modifiers
        Returns the position of the best placement from a list of positions"""
    # takes data from generate_positions and returns the best position using f()
    return


def f():
    """The evaluation function of a state
        Returns a value 0<x<10? on how good the state is"""
    # decision based on statistics
    return


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

def count_holes(playField):
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

    holeCount = zeroCount - ( totalCells - aggregate_height(playField) )

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
    
    return 0
