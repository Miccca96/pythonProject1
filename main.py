import math
import fileinput
from shapes import Rectangle, Square
def print_diagonal(hypotenuse):
    print(f"Diagonal of this rectangle is {hypotenuse}")
def decide_class(sides):
    if(sides[0] == sides[1]):
        return "Square"
    return "Rectangle"

def get_class(class_name):
    class_object = globals()[class_name]
    return class_object

def is_point_in_rectangle(A,B,C,X):
    min_x = min(A[0], B[0], C[0])
    max_x = max(A[0], B[0], C[0])
    min_y = min(A[1], B[1], C[1])
    max_y = max(A[1], B[1], C[1])

    if min_x <= X[0] <= max_x and min_y <= X[1] <= max_y:
        print(f"{X[0],X[1]} point is in rectangle")
    else:
        print(f"{X[0],X[1]} point is not in rectangle")
def calculate_distance(coordinate1, coordinate2):
    return math.sqrt((coordinate2[0] - coordinate1[0])**2 + (coordinate2[1] - coordinate1[1])**2)
def is_rectangle(A,B,C,X):
    if A == B or B == C or A == C:
        print("Two point are the same so rectangle can't be formed")
        return

    side_a = calculate_distance(B, C)
    side_b = calculate_distance(A, C)
    side_c = calculate_distance(A, B)

    hypotenuse = max(side_a,side_b,side_c)

    sides = [s for s in (side_a,side_b,side_c) if s != hypotenuse]

    if(len(sides)<2):
        print("Not enough sides for a rectangle")
        return


    if(round(hypotenuse**2) == (sides[0]**2 + sides[1]**2)):
        print(f"Points {A},{B},{C} can form a rectangle")

        is_point_in_rectangle(A, B, C, X)

        class_name = decide_class(sides)
        shape_obj = get_class(class_name)()
        shape_obj.type_of_rectangle()


        print_diagonal(hypotenuse)

    else:
        print("Given coordinates can not form rectangle")



if __name__ == '__main__':

    coordinates = []
    file = "coordinates.txt"
    for line in fileinput.input(files=file):
        coordinate = eval(line.strip())
        coordinates.append(coordinate)

    is_rectangle(coordinates[0],coordinates[1],coordinates[2],coordinates[3])



