# -	Age Group Classifier: Write a program that accepts a 
# person's age and classifies them as Child(0–12), Teen (13–19), Adult (20–59), Senior (60+). 
# Include input validation for negative values. 


age = int(input("Enter your age: "))

if age < 0:
    print("Enter a valid age")
elif age <= 12:
    print("You are a child")
elif age <= 19:
    print("You are a teen")
elif age <= 59:
    print("You are an adult")
else:
    print("You are a senior")


