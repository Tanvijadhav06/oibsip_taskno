name=input("Enter your name: ")
weight=int(input("enter your weight in kilograms: "))
height=float(input("enter your height in centimeters: "))
BMI = weight / (height/100)**2 
print(BMI)


if BMI <= 18.5:  
    print(name+" , You are underweight.")  
elif BMI <= 24.9:  
    print(name+" , You are normal weight.")  
elif BMI <= 29.9:  
    print(name +" , You are overweight.")  
else:  
    print(name +" ,You are obese.")  