weight = int(input("Enter the weight in kg: "))
height = float(input("Enter the height in m: "))
calculated_BMI = weight / (height ** 2)
print(f"Calculated BMI for the person in weight {weight} and in height {height} is {calculated_BMI}")

#Lec-27 Assignment
if calculated_BMI >= 18.5:
    if calculated_BMI > 25.0:
        if calculated_BMI < 30.0:
            print("your are OverWeighted (pre-obese)")
        elif calculated_BMI < 35.0:
            print("your are OverWeighted (obese-class1)")
        elif calculated_BMI < 40.0:
            print("your are OverWeighted (obese-class2)")
        elif calculated_BMI >= 40.0:
            print("your are OverWeighted (obese-class3)")
    else:
        print("your are in Normal Weight")
else:
    print("your are Under Weight")