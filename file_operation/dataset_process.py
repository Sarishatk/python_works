file_path = "C:/Users/kumar/OneDrive/Desktop/Python_Works/python_works/file_operation/dataset.csv"
fr = open(file_path,"r")
dataset = []
for lines in fr:
    data =   data = lines.rstrip("\n").split(",")
    dictionary = {"jobId":data[0],"Company Name":data[1],
                  "Job Title":data[2],"Location":data[3],
                  "Job Type":data[4],"Salary":data[5],
                  "Posted Date":data[6]}
    dataset.append(dictionary)
print(dataset)
