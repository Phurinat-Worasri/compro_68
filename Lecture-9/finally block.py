try:
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))

    result = numerator / denominator
    print(f"The result is: {result}")

except ZeroDivisionError:
    print("Error: you cannot divide by zero.")

except ValueError:
    print("Error:Invalid input. Please enter numeric values.")

finally:
    print("Execution completed, whether an exception occurred or not.")

print("End of program")
