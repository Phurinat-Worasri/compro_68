weight = input("Enter your weight in kilograms: ")
weight = float(weight)

height = input("Enter your height in meters: ")
height = float(height)

bmi = weight / (height ** 2)
print("Your BMI is: " + str(bmi))