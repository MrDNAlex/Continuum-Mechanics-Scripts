import TransformationLawStressBalance

# Prints A Statement to the User Saying that S = Sigma
print("In this case S = Sigma")

for i in range(0, 3):
    for j in range(0, 3):
       print("\n\n")
       TransformationLawStressBalance.TransformationStressBalance(i+1, j+1)
