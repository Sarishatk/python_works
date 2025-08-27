dile_path = "C://Users//kumar//OneDrive//Desktop//Python_Works//python_works//file_operation//greetings.text"
fw = open(dile_path,"w")
greeting_list = ["good morning","good afternoon","good eveneing"]
for g in greeting_list:
    fw.write(g+"\n")