import string

# Calculates the Dot Product between 2 Vectors
def DotProduct(Vector1, Vector2):
    DotProduct = 0
    for i in range(0, len(Vector1)):
        DotProduct += Vector1[i] * Vector2[i]
    return DotProduct

# Calculates the Magnitude of a Vector
def Magnitude(Vector):
    Magnitude = 0
    for i in range(0, len(Vector)):
        Magnitude += Vector[i] ** 2
    return Magnitude

# Prompts a user to enter the values for a vector
def AskForVector():
    x = float(input("Enter the x value of the vector: "))
    y = float(input("Enter the y value of the vector: "))
    z = float(input("Enter the z value of the vector: "))
    return x, y, z

print("Enter the Values for the New reference Axis X Vector")
VecXNew = AskForVector()

print("Enter the Values for the New reference Axis Y Vector")
VecYNew = AskForVector()

print("Enter the Values for the New reference Axis Z Vector")
VecZNew = AskForVector()

print("Enter the Values for the Old reference Axis X Vector")
VecXOld = AskForVector()

print("Enter the Values for the Old reference Axis Y Vector")
VecYOld = AskForVector()

print("Enter the Values for the Old reference Axis Z Vector")
VecZOld = AskForVector()

# Stores the Array of New Vectors
NewVectors = [VecXNew, VecYNew, VecZNew]

# Stores the Array of Old Vectors
OldVectors = [VecXOld, VecYOld, VecZOld]

# Loops through each New Vector and Old Vector and Calculates the Angle between them
for i in range(0, len(NewVectors)):
    for j in range(0, len(OldVectors)):

        # Gets the Magnitude of the New and Old Vectors
        magNew = Magnitude(NewVectors[i])
        magOld = Magnitude(OldVectors[j])

        # Calculates the Dot Product of the New and Old Vectors
        dotProduct = DotProduct(NewVectors[i], OldVectors[j])

        # Calculates the Angle between the New and Old Vectors
        angle = dotProduct / (magNew * magOld)

        # Formats the Angle into a String
        strAngle: string = str(dotProduct) + "/" + "sqrt(" + str(magNew) + "*" + str(magOld) + ")"

        # Prints the Angle between the New and Old Vectors
        print("a_" + str(i+1) + str(j+1) + " = "+strAngle)
