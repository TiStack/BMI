def calcBMImetric (weight, height):
    #calculates the BMI 
    BMI = weight/pow(height,2)

    return BMI
    

def calcBMIimperial (weight, height):
    #calculates the BMI
    BMI = (weight/pow(height,2))*703

    return BMI


def main():
    # Decide if you are using the metric or imperial system
    choose = input("Are you preferring the metric or imperial system to calculate your BMI? Type 'm' for metric or 'i' for imperial: ")
    
    if choose == 'm':
        kg = input("Enter your weight in kg (e.g., 80.9): ")
        while not kg.replace('.', '', 1).isdigit():
            kg = input("Please enter a valid number: ")
        m = input("Enter your height in meters (e.g., 1.75): ")
        while not m.replace('.', '', 1).isdigit():
            m = input("Please enter a valid number: ")
        
        # Convert inputs to float and calculate BMI
        kg = float(kg)
        m = float(m)
        BMI = calcBMImetric(kg, m)
        print(f"Your weight is {kg} kg and your height is {m} meters. Your current BMI is: {BMI:.2f}")
        if BMI <= 18.5:
            print("Your are underweight!")
        elif BMI > 18.5 and BMI <= 25:
            print("Your weight is in a healthy range!")
        elif BMI > 25 and BMI <= 30:
            print("You are overweight!")
        else:
            print("You should see a doctor!")

    elif choose == 'i':
        lbs = input("Enter your weight in lbs (e.g., 160.8): ")
        while not lbs.replace('.', '', 1).isdigit():
            lbs = input("Please enter a valid number: ")
        inches = input("Enter your height in inches (e.g., 66): ")
        while not inches.replace('.', '', 1).isdigit():
            inches = input("Please enter a valid number: ")
        
        # Convert inputs to float and calculate BMI
        lbs = float(lbs)
        inches = float(inches)
        BMI = calcBMIimperial(lbs, inches)
        print(f"Your weight is {lbs} lbs and your height is {inches} inches. Your current BMI is: {BMI:.2f}")
        if BMI <= 18.5:
            print("Your are underweight!")
        elif BMI > 18.5 and BMI <= 25:
            print("Your weight is in a healthy range!")
        elif BMI > 25 and BMI <= 30:
            print("You are overweight!")
        else:
            print("You should see a doctor!")

    else:
        print("Invalid choice. Please type 'm' or 'i'.")

# Run the program
main()
