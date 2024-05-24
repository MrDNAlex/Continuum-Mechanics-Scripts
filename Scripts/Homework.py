# Homework 2, Tedious Sigma Sum Calculation

# Prompts the user for the Index of the New Axis (X = 1, Y = 2, Z = 3)
newAxisIndex = input("Enter the new axis index: ")

# Prompts the user for the Index of the Old Axis (X = 1, Y = 2, Z = 3)
oldAxisIndex = input("Enter the old axis index: ")

# Prints A Statement to the User Saying that S = Sigma
print("In this case S = Sigma")

# Prints the Left side of the Equation
print("S'_" + str(newAxisIndex) + str(oldAxisIndex) + " * A" + " = ")

# Loops through each Sigma and Alpha and Prints the Additions for the Eqaution 
for i in range(0, 3):
    for j in range(0, 3):

        oldSigma = "S_" + str(i+1) + str(j+1)
        firstAlpha = "a_" + str(newAxisIndex) + str(i+1)
        secondAlpha = "a_" + str(oldAxisIndex) + str(j+1)

        print(" + " + oldSigma + " * " + firstAlpha + " * " + secondAlpha + " * A")
