words = ["hello","hai","madam","racecar","pangaram"]
file_path = "C://Users//kumar//OneDrive//Desktop//Python_Works//python_works//file_operation//word.txt"
fw = open(file_path,"w")
for items in words:
    if items == items[::-1]:
        fw.write(items+"\n")