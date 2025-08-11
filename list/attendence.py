# holiday - h
# present - p 
# leave -l
# find total working days

attendance = ["H","P","P","P","P","L","H","H","P","P","P","P","L","H"]
total_working_day = 0
for at in attendance:
    if at != 'H':
        total_working_day+=1
print(total_working_day)
        
