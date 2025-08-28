file_path = "C:/Users/kumar/OneDrive/Desktop/Python_Works/python_works/file_operation/employee.csv"

fr = open(file_path,"r")

all_employees  =  []

for line in fr:

    line = line.rstrip('\n')

    data = line.split(",")

    dictionary = {"id" : data[0],"name":data[1],
                  
                  "department":data[2],"salary":data[3],

                  "email":data[4],"location":data[5]
                  
                   }
    all_employees.append(dictionary)

print(all_employees)


# get all employee name



