
# Homework 2, Tedious Sigma Sum Calculation


newAxisIndex = input("Enter the new axis index: ")
oldAxisIndex = input("Enter the old axis index: ")

print("In this case S = Sigma")

print("S'_" + str(newAxisIndex) + str(oldAxisIndex) + " * A" + " = ")

for i in range(0, 3):
    for j in range(0, 3):

        oldSigma = "S_" + str(i+1) + str(j+1)
        firstAlpha = "a_" + str(newAxisIndex) + str(i+1)
        secondAlpha = "a_" + str(oldAxisIndex) + str(j+1)

        print(" + " + oldSigma + " * " + firstAlpha + " * " + secondAlpha + " * A")
