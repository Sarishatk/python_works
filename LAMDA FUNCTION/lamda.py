# addition of two numbers
add = lambda n1,n2:n1+n2
print(add(2,4))



# cube

cube = lambda n1:n1**3
print(cube(4))

# last digit max(127,345)

last_d_max = lambda n1,n2:  n1 if n1%10>n2%10 else n2

print(last_d_max(127,345))