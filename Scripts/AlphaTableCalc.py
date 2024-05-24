import string


def DotProduct(Vector1, Vector2):
    DotProduct = 0
    for i in range(0, len(Vector1)):
        DotProduct += Vector1[i] * Vector2[i]
    return DotProduct


def Magnitude(Vector):
    Magnitude = 0
    for i in range(0, len(Vector)):
        Magnitude += Vector[i] ** 2
    return Magnitude


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

NewVectors = [VecXNew, VecYNew, VecZNew]

OldVectors = [VecXOld, VecYOld, VecZOld]


for i in range(0, len(NewVectors)):
    for j in range(0, len(OldVectors)):

        magNew = Magnitude(NewVectors[i])
        magOld = Magnitude(OldVectors[j])

        dotProduct = DotProduct(NewVectors[i], OldVectors[j])

        angle = dotProduct / (magNew * magOld)

        strAngle: string = (
            str(dotProduct) + "/" + "sqrt(" + str(magNew) + "*" + str(magOld) + ")"
        )

        print("a_" + str(i+1) + str(j+1) + " = "+strAngle)
