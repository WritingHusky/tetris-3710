import new_ai as nai

# aggregate height = 11 + 8 + 3 + 3 + 3 + 6 + 4 + 4 + 4 + 4 = 50
# holes = 1 + 1 + 1 + 1 + 1 + 1 = 6
# completed lines = 0
# bumpiness = [3, 5, 0, 0, 3, 2, 0, 0, 0, 13]
playField1 = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [1,0,0,0,0,0,0,0,0,0],
    [1,0,0,0,0,0,0,0,0,0],
    [1,0,0,0,0,0,0,0,0,0],
    [1,1,0,0,0,0,0,0,0,0],
    [1,1,1,1,1,1,1,1,1,1],
    [0,1,0,0,0,1,0,0,0,0],
    [1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,0,0,0],
    [1,1,1,1,1,1,0,1,1,0],
    [1,1,0,1,1,1,1,1,1,0]
]

# aggregate height = 11 + 8 + 3 + 3 + 3 + 6 + 4 + 4 + 4 + 4 = 50
# holes = 1 + 1 + 0 + 0 + 0 + 0 + 1 + 0 + 0 + 0 = 3
# completed lines = 2
# bumpiness = [3, 5, 0, 0, 3, 2, 0, 0, 0, 13]
playField2 = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [1,0,0,0,0,0,0,0,0,0],
    [1,0,0,0,0,0,0,0,0,0],
    [1,0,0,0,0,0,0,0,0,0],
    [1,1,0,0,0,0,0,0,0,0],
    [1,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,0,1,0,0,0,0],
    [1,1,0,0,0,1,0,0,0,0],
    [1,0,0,0,1,1,1,1,1,1],
    [1,1,1,1,1,0,0,0,1,1],
    [1,1,1,1,1,0,0,0,1,1],
    [1,1,1,1,1,0,0,0,1,1]
]

testPiece = [1, 5, 8, 9]
testPosition = [5,5]

aggHeight1 = nai.aggregate_height(playField1)
numHoles1 = nai.count_holes(playField1)

print("Aggregate Height: ", aggHeight1)
print("Number of Holes: ", numHoles1)

aggHeight2 = nai.aggregate_height(playField2)
numHoles2 = nai.count_holes(playField2 , aggHeight2)

print("Aggregate Height: ", aggHeight2)
print("Number of Holes: ", numHoles2)

'''
#testCollision = nai.collision_check(playField1, testPiece, testPosition[0], testPosition[1])
testCollision = nai.collision_check(playField1, testPiece, testPosition[0], testPosition[1])
print("Collision? :", testCollision) 
'''

figures = [
    [[1, 5, 9, 13], [4, 5, 6, 7]],
    [[4, 5, 9, 10], [2, 6, 5, 9]],
    [[6, 7, 9, 10], [1, 5, 6, 10]],
    [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],
    [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],
    [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],
    [[1, 2, 5, 6]],
]

figure = figures[0]
positions = nai.h_generate_positions(playField2, figure)
numRotations = len(positions)
print("Number of Rotations: ", numRotations)
print(positions)

completedLines1 = nai.completed_lines(playField1)
print("Completed Lines: " , completedLines1)

score = nai.f(aggHeight1, numHoles1, 3, completedLines1)
print("Score: ", score)
