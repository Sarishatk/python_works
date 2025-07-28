maths = int(input("Enter you are scored mark of maths : "))
java = int(input("Enter you are scored mark of java : "))
os = int(input("Enter you are scored mark of os : "))
total_scored = maths + java + os
if total_scored>140:
    print("good")
elif total_scored>130 and total_scored<140:
    print("average")
elif total_scored<130:
    print("poor")
else:
    print("you are a fool!!")