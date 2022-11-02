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
    [1,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,0,1,0,0,0,0],
    [1,1,0,0,0,1,0,0,0,0],
    [1,0,0,0,0,1,1,1,1,0],
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
    [1,0,0,0,0,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,0,1,1,1],
    [1,1,1,1,1,1,1,1,1,1]
]

testPiece = [1, 5, 8, 9]
testPosition = [5,5]

aggHeight1 = nai.aggregate_height(playField1)
numHoles1 = nai.count_holes(playField1)

print("Aggregate Height: ", aggHeight1)
print("Number of Holes: ", numHoles1)

aggHeight2 = nai.aggregate_height(playField2)
numHoles2 = nai.count_holes(playField2)

print("Aggregate Height: ", aggHeight2)
print("Number of Holes: ", numHoles2)

#testCollision = nai.collision_check(playField1, testPiece, testPosition[0], testPosition[1])
testCollision = nai.collision_check(playField1, testPiece, testPosition[0], testPosition[1])
print("Collision? :", testCollision)