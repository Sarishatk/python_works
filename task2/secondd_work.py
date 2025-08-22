# First Repeated Character
# Input: "programming


word = "programming"
reapted_character = set()
for i in word:
    if i in reapted_character:
        print("the first repeated character is ",i)
        break
    else:
        reapted_character.add(i)


# Generate First N Prime Numbers (starting from 13)
# Input: 5 → Output: 13, 17, 19, 23, 29




# Find Factorial of a Number
# Input: 5 → Output: 120

# Check Armstrong Number
# Input: 153 → Output: True (since 1³+5³+3³=153)

# Find GCD of Two Numbers
# Input: 48, 18 → Output: 6