path = "C://Users//kumar//OneDrive//Desktop//Python_Works//python_works//file_operation//greetings.text"
fa = open(path,"a")
fruits = ["orange","apple","banana"]
for items in fruits:
    fa.write(items+'\n' )