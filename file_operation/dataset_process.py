file_path = "C:/Users/kumar/OneDrive/Desktop/Python_Works/python_works/file_operation/dataset.csv"
fr = open(file_path,"r")
dataset = []
for lines in fr:
    data =   data = lines.rstrip("\n").split(",")
    